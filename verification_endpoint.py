from flask import Flask, request, jsonify
from flask_restful import Api
import json
import eth_account
import algosdk

app = Flask(__name__)
api = Api(app)
app.url_map.strict_slashes = False

@app.route('/verify', methods=['GET','POST'])
def verify_eth(sig, pk, msg):
    eth_encoded_msg = eth_account.messages.encode_defunct(text=msg)
    if eth_account.Account.recover_message(eth_encoded_msg,signature=sig) == pk:
        return True
    return False

def verify_alg(sig, pk, msg):
    if algosdk.util.verify_bytes(msg.encode('utf-8'),sig,pk):
        return True
    return False

def verify():
    content = request.get_json(silent=True)

    sig = content.sig
    pk = content.payload.pk
    msg = content.payload.message
    platform = content.payload.platform

    if platform == 'Ethereum:
        result = verify_eth(sig, pk, msg)
    else:
        result = verify_alg(sig, pk, msg)
    #Check if signature is valid
    return jsonify(result)

if __name__ == '__main__':
    app.run(port='5002')
