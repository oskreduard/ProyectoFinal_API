import requests as requests
from flask import Flask
from flask import jsonify
from flask import request
import json

from __main__ import app
from __main__ import url_backend_registraduria


@app.route("/resultado",methods=['GET'])
def getResultados():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = url_backend_registraduria + '/resultado'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/resultado/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['POST'])
def crearResultado(id_candidato,id_mesa):
    data = request.get_json()                                       #BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_registraduria + '/resultado/candidato/'+ id_candidato +'/mesa/'+id_mesa      #Change the URL
    response = requests.post(url, headers=headers,json=data)        #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/resultado/<string:id>",methods=['GET'])
def getResultado(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_registraduria + '/resultado/'+id                   #Change the URL
    response = requests.get(url, headers=headers)                   #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/resultado/<string:id>/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['PUT'])
def modificarResultado(id,id_candidato,id_mesa):
    data = request.get_json()  # BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}  # Always the same
    url = url_backend_registraduria + '/resultado/'+ id +'/candidato/'+ id_candidato +'/mesa/'+id_mesa
    response = requests.put(url, headers=headers, json=data)  # Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/resultado/<string:id>",methods=['DELETE'])
def eliminarResultado(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = url_backend_registraduria + '/resultado/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)
