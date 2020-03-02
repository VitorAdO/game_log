# game_log
Projeto que irá realizar um parser do arquivo que gera todas as informações de cada partida do game Quake 3 Arena.

# Linguagem

	Linguagem: Python
	Versão: 3.7.3

# Bibliotecas utilizadas
	re
	os.path
	json

	Caso não possua essas bibliotecas instaladas em sua maquina, por favor, realizar a instalação para que o script execute corretamente.

# Overview código
#  parser.py
		Importação do arquivo games.log;
		Encontrar os indices de cada inicio de game;
			O que marca o inicio de cada jogo é a palavra 'InitGame'.
		Encontrar os indices de cada final de game;
			O que marca o fim de cada jogo é a palavra 'ShutdownGame'
		Agrupar as partidas de acordo com os indices passados;
			Obs: Caso exista algum InitGame que não tenha um ShutdownGame, será retornado todos os dados até o próximo ShutdownGame. 
		Para cada partida é realizada o Agrupamento de Player, Informações das Kills e é montado uma variavel com a estrutura dos dados para o json;
		Transformar a variavel em arquivo Json.

# relatorio_game.py
		Importação do arquivo games_log.json;
		Para cada partida é separado os valores que serão mostrados no relatório em uma variavel;
		Montado a string com todos os dados do relatório;
		Realização do print dessa string.

# Instruções
#  parser.py
		Abrir o código em um editor de texto;
		Informar o CAMINHO do arquivo "games.log" na variavel "self.path_games_log";
			A importação do arquivo é necessária para se realizar o parse;
			Ex: 'C:/desenvolvimento/teste_enext/python/import/games.log'.
		Informar o CAMINHO do arquivo "game_log.json" na variavel "self.path_json";
			Esse caminho é importante para que o arquivo JSON seja exportado para uma pasta desejada;
			Ex: 'C:/desenvolvimento/teste_enext/python/export/game_log.json'.

# relatorio_game.py
		Abrir o código em um editor de texto;
		Informar o CAMINHO do arquivo "game_log.json" na variavel "path_json";
			A importação do arquivo é necessária para a exibição de um relatório;
			Ex: 'C:/desenvolvimento/teste_enext/python/import/games.log'.
