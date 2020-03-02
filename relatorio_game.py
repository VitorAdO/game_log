# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 22:17:02 2020

@author: vitor
"""

import json
import os.path

path_json = 'C:/desenvolvimento/teste_enext/python/export/game_log.json'

if os.path.exists(path_json):
    # Carrega Json
    try:
        
        with open(path_json,'r') as f:
            dados_json = json.load(f)     
        
        # Relatorio de cada partida
        for game in dados_json:
            total_mortes = str(dados_json[game]['Total_Kills'])
            kills = dados_json[game]['Kills']
            
            # Ordenando ranking de jogadores por partida
            ranking_game = sorted(kills.items(), key=lambda item: item[1], reverse=True)
            
            # Cabecalho da partida
            relatorio ='\n'+ game + ' teve ' + total_mortes + ' mortes. \nSegue ranking da partida: '
            
            print(relatorio)
            
            # Imprimindo ranking de jogadores
            list(map(lambda x: print('    '+x[0] + ': ' + str(x[1])),ranking_game))
    except Exception as e:
        print('Ocorreu algum erro na execução do script.')
        print('O erro é: ' + str(e))

else:
    print('Arquivo não encontrado!')
    print('Verifique se a pasta é a correta ou se o script Parser.py gerou o json.')
