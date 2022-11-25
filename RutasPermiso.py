import requests as requests
from flask import Flask
from flask import jsonify
from flask import request
import json

from __main__ import app
from __main__ import url_backend_security


@app.route("/permiso",methods=['GET'])
def getPermisos():
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/permiso'                        #Change the URL
    response = requests.get(url, headers=headers)        #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/permiso",methods=['POST'])
def crearPermisos():
    data = request.get_json()                                       #BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/permiso'                        #Change the URL
    response = requests.post(url, headers=headers,json=data)     #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/permiso/<string:id>",methods=['GET'])
def getPermiso(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/permiso/'+id                   #Change the URL
    response = requests.get(url, headers=headers)                   #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/permiso/<string:id>",methods=['PUT'])
def modificarPermiso(id):
    data = request.get_json()                                       #BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/permiso/'+id                              #Change the URL
    response = requests.put(url, headers=headers,json=data)     #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/permiso/<string:id>",methods=['DELETE'])
def deletePermiso(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/permiso/'+id                   #Change the URL
    response = requests.delete(url, headers=headers)                   #Change the Method
    return {"Msj": "Delete exitoso"}

