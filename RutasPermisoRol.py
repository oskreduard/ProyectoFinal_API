import requests as requests
from flask import Flask
from flask import jsonify
from flask import request
import json

from __main__ import app
from __main__ import url_backend_security


@app.route("/permiso-rol",methods=['GET'])
def getPermisosRoles():
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/permiso-rol'                        #Change the URL
    response = requests.get(url, headers=headers)        #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/permiso-rol/rol/<string:id_rol>/permiso/<string:id_permiso>",methods=['POST'])
def crearPermisosRoles(id_rol,id_permiso):
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/permiso-rol/rol/'+id_rol+'/permiso/'+id_permiso                     #Change the URL
    response = requests.post(url, headers=headers)     #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/permiso-rol/<string:id>",methods=['GET'])
def getPermisoRol(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/permiso-rol/'+id                   #Change the URL
    response = requests.get(url, headers=headers)                   #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/permiso-rol/<string:id>/rol/<string:id_rol>/permiso/<string:id_permiso>", methods=['PUT'])
def modificarPermisoRol(id,id_rol, id_permiso):
    headers = {"Content-Type": "application/json; charset=utf-8"}  # Always the same
    url = url_backend_security + '/permiso-rol/' + id + '/rol/' + id_rol + '/permiso/' + id_permiso  # Change the URL
    response = requests.put(url, headers=headers)  # Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/permiso-rol/<string:id>",methods=['DELETE'])
def deletePermisoRol(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_security + '/permiso-rol/'+id                   #Change the URL
    response = requests.delete(url, headers=headers)                   #Change the Method
    json = response.json()
    return jsonify(json)

