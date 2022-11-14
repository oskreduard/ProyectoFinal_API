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
    response = requests.delete(url, headers=headers)                   #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/usuario/<string:id>/rol/<string:id_rol>",methods=['PUT'])
def AsignarRolUsuario(id,id_rol):                                    #BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/usuario/'+id + '/rol/'+id_rol                             #Change the URL
    response = requests.put(url, headers=headers)     #Change the Method
    json = response.json()
    return jsonify(json)