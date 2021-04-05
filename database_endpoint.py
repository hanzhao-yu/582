from flask import Flask, request, g
from flask_restful import Resource, Api
from sqlalchemy import create_engine, select, MetaData, Table
from flask import jsonify
import json
import eth_account
import algosdk
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import load_only

from models import Base, Order, Log
engine = create_engine('sqlite:///orders.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

app = Flask(__name__)

#These decorators allow you to use g.session to access the database inside the request code
@app.before_request
def create_session():
    g.session = scoped_session(DBSession) #g is an "application global" https://flask.palletsprojects.com/en/1.1.x/api/#application-globals

@app.teardown_appcontext
def shutdown_session(response_or_exc):
    g.session.commit()
    g.session.remove()

"""
-------- Helper methods (feel free to add your own!) -------
"""

def log_message(d)
    log_object = Log( message=d)
    g.session.add(log_object)
    g.session.commit()

"""
---------------- Endpoints ----------------
"""

@app.route('/trade', methods=['POST'])
def trade():
    if request.method == "POST":
        content = request.get_json(silent=True)
        print( f"content = {json.dumps(content)}" )
        columns = [ "sender_pk", "receiver_pk", "buy_currency", "sell_currency", "buy_amount", "sell_amount", "platform" ]
        fields = [ "sig", "payload" ]
        error = False
        for field in fields:
            if not field in content.keys():
                print( f"{field} not received by Trade" )
                print( json.dumps(content) )
                log_message(content)
                return jsonify( False )

        error = False
        for column in columns:
            if not column in content['payload'].keys():
                print( f"{column} not received by Trade" )
                error = True
        if error:
            print( json.dumps(content) )
            log_message(content)
            return jsonify( False )

        #Your code here
        sig = content["sig"]
        pk = content["payload"]["sender_pk"]
        msg = json.dumps(content["payload"])
        platform = content["payload"]["platform"]
        result = True
        if platform == 'Ethereum':
            eth_encoded_msg = eth_account.messages.encode_defunct(text=msg)
            if eth_account.Account.recover_message(eth_encoded_msg,signature=sig) == pk:
                result = True
            else:
                result = False
        else:
            if algosdk.util.verify_bytes(msg.encode('utf-8'),sig,pk):
                result = True
            else:
                result = False
        if result == True:
            order = {}
            order['sender_pk'] = content["payload"]["sender_pk"]
            order['receiver_pk'] = content["payload"]["receiver_pk"]
            order['buy_currency'] = content["payload"]["buy_currency"]
            order['sell_currency'] = content["payload"]["sell_currency"]
            order['buy_amount'] = content["payload"]["buy_amount"]
            order['sell_amount'] = content["payload"]["sell_amount"]
            order_obj = Order( sender_pk=order['sender_pk'],receiver_pk=order['receiver_pk'], buy_currency=order['buy_currency'], sell_currency=order['sell_currency'], buy_amount=order['buy_amount'], sell_amount=order['sell_amount'] )
            g.session.add(order_obj)
            g.session.commit()
        else:
            log_message(msg)
        #Note that you can access the database session using g.session

@app.route('/order_book')
def order_book():
    #Your code here
    result = {1}
    #Note that you can access the database session using g.session
    return jsonify(result)

if __name__ == '__main__':
    app.run(port='5002')
