# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:36:44 2020

@author: vitor
"""

from flask import Flask, jsonify
import json
import os.path

path_json = 'C:/desenvolvimento/teste_enext/python/export/game_log.json'

# Carregando arquivo Json
def abrir_json():
    if os.path.exists(path_json):
        # Carrega Json
        try:
            with open(path_json,'r') as f:
                dados_json = json.load(f)
            return dados_json
        except Exception as e:
            print('Ocorreu algum erro na execução do script.')
            print('O erro é: ' + str(e))
    else:
        print('Arquivo não encontrado!')
        print('Verifique se a pasta é a correta ou se o script Parser.py gerou o json.')
    
# Iniciando 
app = Flask(__name__)

# Criação das Rotas
@app.route('/', methods=['GET'])
def home():
    games_json = abrir_json()
    instrucoes = '<center>Total de jogos: ' + str(len(games_json.keys()))
    instrucoes += '<br> Ids iniciam do 0. Exemplo de IDs:'
    instrucoes += '<br> "game_0", "game_1"'
    instrucoes += '<br> Para trazer o json do game, deve adicionar o id da partida na url. Exemplo:'
    instrucoes += '<br> "localhost:5000/game_0" ou "localhost:5000/game_1"</center>'
    return instrucoes,200

@app.route('/<string:id_game>', methods=['GET'])
def game_per_id(id_game):
    games_json = abrir_json()
    verifica = len(list(filter(lambda x: x == id_game,list(games_json.keys()))))
    if verifica != 0:
        return jsonify(games_json[id_game]),200
    else:
        return 'Ocorreu um erro, verifique o id do game',500

# Iniciando API 
if __name__ == '__main__':
    app.run()


