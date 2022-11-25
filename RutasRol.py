import requests as requests
from flask import Flask
from flask import jsonify
from flask import request
import json

from __main__ import app
from __main__ import url_backend_security


@app.route("/rol",methods=['GET'])
def getRoles():
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/rol'                        #Change the URL
    response = requests.get(url, headers=headers)        #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/rol",methods=['POST'])
def crearRoles():
    data = request.get_json()                                       #BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/rol'                        #Change the URL
    response = requests.post(url, headers=headers,json=data)     #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/rol/<string:id>",methods=['GET'])
def getRol(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/rol/'+id                   #Change the URL
    response = requests.get(url, headers=headers)                   #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/rol/<string:id>",methods=['PUT'])
def modificarRoles(id):
    data = request.get_json()                                       #BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/rol/'+id                              #Change the URL
    response = requests.put(url, headers=headers,json=data)     #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/rol/<string:id>",methods=['DELETE'])
def deleteRol(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/rol/'+id                   #Change the URL
    response = requests.delete(url, headers=headers)                   #Change the Method

    return {"Msj": "Delete exitoso"}

