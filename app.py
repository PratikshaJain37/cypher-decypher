from flask import Flask, render_template, request
import numpy as np

from helpers.additive import *
from helpers.multiplicative import *
from helpers.hilldigraph import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


encryption_cyphers = ['Additive', 'Multiplicative', 'Hill Digraph']
@app.route("/encryption")
def encryption():
    return render_template('encryption.html')

@app.route("/decryption")
def decryption():
    return render_template('decryption.html')





@app.route('/encryption/additive_cypher')
def e_additive():
    return render_template('input_encrypt.html', type_of_cypher = 'additive')

@app.route('/encryption/additive_cypher', methods=['POST'])
def e_additive2():
    key = request.form.get('key', type=int)
    text = request.form.get('text')
    text = datacleaning(text)
    text = additive_encrypt(text,key)
    return render_template('output_encrypt.html',output = text, IsValidKey = True)
    

@app.route('/decryption/additive_decypher')
def d_additive():
    return render_template('input_decrypt.html')

@app.route('/decryption/additive_decypher', methods=['POST'])
def d_additive2():
    text = request.form.get('text')
    text = datacleaning(text)
    output = additive_decrypt(text)
    return render_template('output_decrypt.html', output = output)





@app.route('/encryption/multiplicative_cypher')
def e_multipicative():
    return render_template('input_encrypt.html', type_pf_cypher = 'multiplicative')

@app.route('/encryption/multiplicative_cypher', methods=['POST'])
def e_multipicative2():
    key = request.form.get('key', type=int)
    text = request.form.get('text')
    
    if valid_key_multiplicative(key):
        text = datacleaning(text)
        text = multiplicative_encrypt(text,key)
        return render_template('output_encrypt.html',output = text, IsValidKey = True)
    else:
        return render_template('output_encrypt.html',IsValidKey = False)
    
@app.route('/decryption/multiplicative_decypher')
def d_multiplicative():
    return render_template('input_decrypt.html')

@app.route('/decryption/multiplicative_decypher', methods=['POST'])
def d_multiplicative2():
    text = request.form.get('text')
    text = datacleaning(text)
    output = multiplicative_decrypt(text)
    return render_template('output_decrypt.html', output = output)





@app.route('/encryption/hilldigraph_cypher')
def e_hilldigraph():
    return render_template('input_encrypt.html', type_of_cypher = 'hilldigraph')

@app.route('/encryption/hilldigraph_cypher', methods=['POST'])
def e_hilldigraph2():
    a = request.form.get('a', type=int)
    b = request.form.get('b', type=int)
    c = request.form.get('c', type=int)
    d = request.form.get('d', type=int)
        
    text = request.form.get('text')
    
    isvalidkey,key = valid_key_hilldigraph(a,b,c,d)

    if isvalidkey:
        text = datacleaning_digraph(text)
        text = hilldigraph_encrypt(text,key)
        return render_template('output_encrypt.html',output = text, IsValidKey = True)
    else:
        return render_template('output_encrypt.html',IsValidKey = False)





if __name__ == "__main__":
    app.run(debug=False)
