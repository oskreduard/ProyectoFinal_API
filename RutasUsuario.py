import re

import requests as requests
from flask import Flask
from flask import jsonify
from flask import request
import json

from __main__ import app
from __main__ import url_backend_security


@app.route("/usuario",methods=['GET'])
def getUsuarios():
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/usuario'                        #Change the URL
    response = requests.get(url, headers=headers)        #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/usuario",methods=['POST'])
def crearUsuarios():
    data = request.get_json()                                       #BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/usuario'                        #Change the URL
    response = requests.post(url, headers=headers,json=data)     #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/usuario/<string:id>",methods=['GET'])
def getUsuario(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/usuario/'+id                   #Change the URL
    response = requests.get(url, headers=headers)                   #Change the Method
    json = response.json()
    return jsonify(json)
@app.route("/usuario/email/<string:email>",methods=['GET'])
def getUsuariobyEmail(email):
    print(email)
    for l in email:
        if re.search('\\d', l):
            email = email.replace(l, "")
    print(email)
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = url_backend_security + '/usuario/email/'+email
    response = requests.get(url, headers=headers)
    json = response.json()
    if response.status_code == 401 or response.status_code == 400:
        return jsonify({"msg": "Not email found"}), 401
    else:
        return jsonify(json)
@app.route("/usuario/<string:id>",methods=['PUT'])
def modificarUsuarios(id):
    data = request.get_json()                                       #BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/usuario/'+id                              #Change the URL
    response = requests.put(url, headers=headers,json=data)     #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/usuario/<string:id>",methods=['DELETE'])
def deleteUsuario(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/usuario/'+id                   #Change the URL
    response = requests.delete(url, headers=headers)
    return {"Msj": "Delete exitoso"}

@app.route("/usuario/<string:id>/rol/<string:id_rol>",methods=['PUT'])
def AsignarRolUsuario(id,id_rol):                                    #BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/usuario/'+id + '/rol/'+id_rol                             #Change the URL
    response = requests.put(url, headers=headers)     #Change the Method
    if response == {}:
        return jsonify({"msg": "Not email found"}), 401
    else:
        json = response.json()
        return jsonify(json)
