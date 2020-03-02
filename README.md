# game_log
Projeto que irá realizar um parser do arquivo que gera todas as informações de cada partida do game Quake 3 Arena.

# Linguagem

	Linguagem: Python
	Versão: 3.7.3

# Bibliotecas utilizadas
	re
	os.path
	json
	flask
	jsonify
	
	Caso não possua essas bibliotecas instaladas em sua maquina, por favor, realizar a instalação para que o script execute corretamente.

# Overview scripts
#  parser.py (TASK 1)
	Gera arquivo JSON.
		Importação do arquivo games.log;
		Encontrar os indices de cada inicio de game;
			O que marca o inicio de cada jogo é a palavra 'InitGame'.
		Encontrar os indices de cada final de game;
			O que marca o fim de cada jogo é a palavra 'ShutdownGame'
		Agrupar as partidas de acordo com os indices passados;
			Obs: Caso exista algum InitGame que não tenha um ShutdownGame, será retornado todos os dados até o próximo ShutdownGame. 
		Para cada partida é realizada o Agrupamento de Player, Informações das Kills e é montado uma variavel com a estrutura dos dados para o json;
		Transformar a variavel em arquivo Json.

# relatorio_game.py (TASK 2)
	Imprimi relatório.
		Importação do arquivo games_log.json;
		Para cada partida é separado os valores que serão mostrados no relatório em uma variavel;
		Montado a string com todos os dados do relatório;
		Realização do print dessa string.
# api.py
	Rotas para puxar dados do JSON.
		Criação de função que importará os dados do json;
		Iniciar flask
		Criar rotas
			Uma rota (/) conterá instruções sobre a API
			E a outra (/<string:id_game>) trará dados dos games que serão consultados.

# Instruções
	Para a execução dos scripts "api.py" e "relatorio_game.py" é necessário que o arquivo "game_log.json" esteja criado. Para isso, o arquivo "parser.py" deve ser o PRIMEIRO script a ser rodado.
#  parser.py ("/parser.py")
		Abrir o código em um editor de texto;
		Informar o CAMINHO do arquivo "games.log" na variavel "self.path_games_log";
			A importação do arquivo é necessária para se realizar o parse;
			Ex: 'C:/desenvolvimento/teste_enext/python/import/games.log'.
		Informar o CAMINHO do arquivo "game_log.json" na variavel "self.path_json";
			Esse caminho é importante para que o arquivo JSON seja exportado para uma pasta desejada;
			Ex: 'C:/desenvolvimento/teste_enext/python/export/game_log.json'.

# relatorio_game.py ("/relatorio_game.py")
		Abrir o código em um editor de texto;
		Informar o CAMINHO do arquivo "game_log.json" na variavel "path_json";
			A importação do arquivo é necessária para a exibição de um relatório;
			Ex: 'C:/desenvolvimento/teste_enext/python/import/games.log'.
			
# api.py ("api/api.py")
	
		Abrir o código em um editor de texto;
		Informar o CAMINHO do arquivo "game_log.json" na variavel "path_json";
			A importação do arquivo é necessária para o funcionamento da API;
			Ex: 'C:/desenvolvimento/teste_enext/python/import/games.log'.

