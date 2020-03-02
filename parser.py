# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:40:35 2020

@author: vitor
"""

import re
import json

class Gparser():
    
    def __init__(self):
        self.path_games_log = 'C:/desenvolvimento/teste_enext/python/import/games.log'
        self.path_json = 'C:/desenvolvimento/teste_enext/python/export/game_log.json'
        self.matchs = []
        self.players = []
        self.dados_json = {}
        
    def carrega_arquivo(self,path):
        # Carregando arquivo Games.log
        try:           
            with open(path, 'r') as f:        
                games_log = f.readlines()
            return games_log
        
        except Exception as e:
            print('Ocorreu um erro ao abrir o arquivo games.log')
            print('O erro é: ' + str(e))
            
    def final_filter(self,game_log):
        # Mapeando indices que indicam o final de cada partida.
        indices = []
        for i,conteudo in enumerate(game_log):
            if (re.search(r'ShutdownGame',conteudo)):
                indices.append(i)

        return indices
    
    def init_filter(self,game_log):
        # Mapeando indices que indicam o inicio de cada partida.
        indices = []
        for i,conteudo in enumerate(game_log):
            if (re.search(r'InitGame',conteudo)):
                indices.append(i)

        return indices
            
    
    def agrupar_partidas(self,log,inicio,final):
        # Separando o log de cada partida
        for i in range(0,len(inicio)-1):
            self.matchs += [log[inicio[i]:final[i]]] 
            
            for ind,conteudo in enumerate(self.matchs[-1]):                
                if ind > 0 and (re.search(r'InitGame',conteudo)):
                    del inicio[i+1]
    
    def agrupar_players(self,indice,match_info):
        # Agrupando players de cada partida
        players_match=[]
        
        for info in match_info:
            if re.search(r'n\\(.*?)\\t',info):
                player = re.findall(r'n\\(.*?)\\t',info)
                players_match += player
        self.players += [[indice,list(set(players_match))]]
    
    def info_kills(self,indice,match_info):
        # Total de kills e Contagem de kills para cada player dentro de uma partida
        total_mortes = 0
        players_info = dict(map(lambda x: [x,0],self.players[indice][1]))
        
        for info in match_info:
    
            if re.search(r'Kill',info):
                total_mortes += 1
                
                matou = re.findall(r'[0-9]: (.*?) killed',info)[0]
                morreu = re.findall(r'killed (.*?) by',info)[0]
                
                if matou != '<world>':
                    players_info[matou] += 1
                else:
                    players_info[morreu] -= 1
                
        return [total_mortes,players_info]
    
    def estrutura_json(self,id_partida,info_kills):
        # Estruturando partidas para adicionar em um arquivo json
        id_game = 'game_'+str(id_partida)
        total_kills = {'Total_Kills':info_kills[0]}
        players_game = {'Players':self.players[id_partida][1]}
        kills = {'kills':info_kills[1]}
        dados_partida = [total_kills,players_game,kills]
        
        self.dados_json[id_game] = dados_partida
        

###########################################################################################
        

if __name__ == '__main__':
    
    gp = Gparser()
    
    glog = gp.carrega_arquivo(gp.path_games_log)
    
    index_init = gp.init_filter(glog)
    index_final = gp.final_filter(glog)
    
    
    gp.agrupar_partidas(glog,index_init,index_final)
    
    del index_init,index_final
    
    # Preparação para arquivo Json
    for i,match in enumerate(gp.matchs):
        gp.agrupar_players(i,match)
        kills = gp.info_kills(i,match)
        gp.estrutura_json(i,kills)
    
    try:
    # Exportação para Json
        dados_json = gp.dados_json
        dados_json = json.dumps(dados_json, indent=4, sort_keys=False)
    
        with open(gp.path_json,'w') as f:
            f.truncate()
            f.write(dados_json)
    except Exception as e:
        print('Ocorreu um erro exportar o arquivo games.log')
        print('O erro é: ' + str(e))







