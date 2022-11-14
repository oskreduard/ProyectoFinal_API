import requests as requests
from flask import Flask
from flask import jsonify
from flask import request
import json

from __main__ import app
from __main__ import url_backend_registraduria


@app.route("/mesa",methods=['GET'])
def getMesas():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = url_backend_registraduria + '/mesa'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/mesa",methods=['POST'])
def crearMesa():
    data = request.get_json()                                       #BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_registraduria + '/mesa'                        #Change the URL
    response = requests.post(url, headers=headers,json=data)        #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/mesa/<string:id>",methods=['GET'])
def getMesa(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_registraduria + '/mesa/'+id                   #Change the URL
    response = requests.get(url, headers=headers)                   #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/mesa/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()  # BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}  # Always the same
    url = url_backend_registraduria + '/mesa/'+id      # Change the URL
    response = requests.put(url, headers=headers, json=data)  # Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/mesa/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = url_backend_registraduria + '/mesa/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)
