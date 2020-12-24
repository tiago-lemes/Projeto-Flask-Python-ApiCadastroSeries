```diff
+  Repositório criado para armazenar o projeto criado no módulo 3 do Bootcamp de Python do IGTI,
+ para demonstrar a criação de uma API REST para gerenciar os dados de um cadastro de "Séries"
+ e "Episódios" dessas "Séries", utilizando como ferramenta o FLASK e a linguagem Python.

! Vamos conversar a respeito? Me adicione no linkedin (👊)
- https://www.linkedin.com/in/tiagolemesferreira
```

----------------------------

Prints do Projeto:

* Configuração do APP, da Porta e Execução do Servidor Local
![LocalServer](https://raw.githubusercontent.com/tiago-lemes/Projeto-Flask-Python-ApiCadastroSeries/master/doc/img%20api%201.png)
----------------------------


* Exemplificando a chamada e o retorno do método de cadastro de séries[/show] (POST)
>Chamada
![CallInputShow](https://raw.githubusercontent.com/tiago-lemes/Projeto-Flask-Python-ApiCadastroSeries/master/doc/img%20api%202.png)

>Retorno
![ReturnCallInputShow](https://raw.githubusercontent.com/tiago-lemes/Projeto-Flask-Python-ApiCadastroSeries/master/doc/img%20api%203.png)
----------------------------


* Exemplificando a chamada e o retorno do método de cadastro de episódios de uma série [/show/<ID_da_serie>/episode] (POST)
>Chamada
![CallInputEpisodeInShow](https://raw.githubusercontent.com/tiago-lemes/Projeto-Flask-Python-ApiCadastroSeries/master/doc/img%20api%204.png)

>Retorno
![ReturnCallInputEpisodeInShow](https://raw.githubusercontent.com/tiago-lemes/Projeto-Flask-Python-ApiCadastroSeries/master/doc/img%20api%205.png)
----------------------------


* Exemplificando a chamada e o retorno do método de listagem de todas as séries e episódios cadastrados [/showall] (GET)
![ReturnAllEpisodesAndShows](https://raw.githubusercontent.com/tiago-lemes/Projeto-Flask-Python-ApiCadastroSeries/master/doc/img%20api%206.png)
----------------------------


* Exemplificando a chamada e o retorno do método de listagem de uma série e seus episódios cadastrados
>Utilizando "Nome da Série" na busca [/show/<nome_da_serie>] (GET)
![ReturnEpisodesAndShowByName](https://raw.githubusercontent.com/tiago-lemes/Projeto-Flask-Python-ApiCadastroSeries/master/doc/img%20api%207.png)

>Utilizando "ID da Série" na busca [/show/<ID_da_serie>] (GET)
![ReturnEpisodesAndShowByID](https://raw.githubusercontent.com/tiago-lemes/Projeto-Flask-Python-ApiCadastroSeries/master/doc/img%20api%208.png)
----------------------------


* Exemplificando a chamada e o retorno do método de exclusão/delete de uma determinada série e de seus episódios [/show/<ID_da_serie>] (DELETE)
![DeleteShowAndEpisodes](https://raw.githubusercontent.com/tiago-lemes/Projeto-Flask-Python-ApiCadastroSeries/master/doc/img%20api%209.png)
----------------------------

