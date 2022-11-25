import requests as requests
from flask import Flask
from flask import jsonify
from flask import request
import json

from __main__ import app
from __main__ import url_backend_registraduria


@app.route("/candidato",methods=['GET'])
def getCandidatos():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = url_backend_registraduria + '/candidato'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/candidato",methods=['POST'])
def crearCandidato():
    data = request.get_json()                                       #BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_registraduria + '/candidato'                        #Change the URL
    response = requests.post(url, headers=headers,json=data)        #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/candidato/<string:id>",methods=['GET'])
def getCandidato(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}   #Always the same
    url = url_backend_registraduria + '/candidato/'+id                   #Change the URL
    response = requests.get(url, headers=headers)                   #Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/candidato/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()  # BodyRequest if needed
    headers = {"Content-Type": "application/json; charset=utf-8"}  # Always the same
    url = url_backend_registraduria + '/candidato/'+id      # Change the URL
    response = requests.put(url, headers=headers, json=data)  # Change the Method
    json = response.json()
    return jsonify(json)

@app.route("/candidato/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = url_backend_registraduria + '/candidato/' + id
    response = requests.delete(url, headers=headers)

    return {"Msj": "Delete exitoso"}

@app.route("/candidato/<string:id>/partido/<string:id_partido>",methods=['PUT'])
def asignarPartidoACandidato(id,id_partido):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = url_backend_registraduria + '/candidato/' + id + '/partido/' + id_partido
    response = requests.put(url, headers=headers)
    json = response.json()
    return jsonify(json)
@app.route("/candidato/cedula/<string:cedula>",methods=['GET'])
def buscarCandidatobyCedula(cedula):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = url_backend_registraduria + '/candidato/cedula/' + cedula

    print(url)
    response = requests.get(url, headers=headers)
    print(response)
    json = response.json()
    if json=={}:
        return {"Resultado": "No se encuentran el Candidato o el Partido indicados"},401
    else:
        return jsonify(json)