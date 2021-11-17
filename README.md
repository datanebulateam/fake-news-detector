# Detector de Fake News

Este projeto realiza a detecção de notícias que podem ser ou não Fake News. Nos últimos anos a forma como as pessoas estão tendo acesso à informação tem mudado bastante, hoje não temos apenas a TV, o Rádio e o Jornal Impresso para recebermos qualquer notícia, a internet possibilitou ir muito além, podemos acessar qualquer informação em qualquer lugar e a qualquer hora. A internet ao mesmo tempo que nos possibilita sermos pessoas mais informadas e conectadas com todo o Globo, também se tornou um meio eficiente para difundir notícias falsas em massa. Atualmente podemos dizer que é até difícil ter certeza que uma notícia sobre um determinado assunto é verdadeiro ou não. Baseado nisso esse projeto busca realizar de forma automatizada a detecção de notícias falsas, ou seja, Fake News.

## Objetivos e resultados chave

O objetivo principal do projeto é fazer a detecção de noticias Fake.

- Organizar o projeto
  - Selecionar a melhor ferramenta para gerenciamento de tarefas
  - Registrar as tarefas em etapas, A fazer, Executando, Concluido e Impedimento

- Selecionar a base de dados
  - Selecionar a base de dados, primeiramente dentro da plataforma Kaggle
  - Criar uma nova base de dados com noticias do Brasil em português
 
- Realizar a analise exploratória dos dados
  - Identificar as váriaveis disponiveis, descreve-las e definir os tipos de dados
  - Realizar transformação de variáveis (codificação)
  - Tratar de valores faltantes e valores discrepantes
  - Realizar algumas visualizações gráficas
  - Compreender o DataFrame

- Criar modelo de detecção de Fake News
  - Realizar transformação de dados textuais utilixando o tf-idf
  

## Conteúdo

Atualmente o projeto possui três arquivos de notebook

00-AnaliseExploratoriaFakeNews: Neste notebook foi realizado a analise exploratória dos dados. Para tanto foi feito um pré tratamento dos dados, como alterações de tipos de variaveis, calculos para quantificar os valores das variaveis e a visualização dos dados, encerrando com as conclusões que foram feitas a partir da analise dos dados.

01-Preparandoosdados: Esse notebook foi o de preparação dos dados frente a analise realizada anteriormente.

02-Treinamentodomodelo: Esse notebook é onde está sendo executado o modelo de Classificação que irá classificar as noticias em verdadeiras ou falsas.


## Utilização

Descreva aqui quais os passos necessários (dependências externas, comandos, etc.) para replicar o seu projeto. Instalação de dependências necessárias, criação de ambientes virtuais, etc. Este modelo é baseado em um projeto utilizando o [Poetry](https://python-poetry.org/) como gerenciador de dependências e ambientes virtuais. Você pode utilizar o `conda`, ambientes virtuais genéricos do Python ou até mesmo containers do docker. Mas tente fazer algo que seja facilmente reprodutível.

## Desenvolvedores
 - [Alexsandro Lopes](http://github.com/contribuidor_1)
 - [Crislane Maria](http://github.com/contribuidor_2)
 - [Claudiane Gomes](https://github.com/ClaudianeGomes0409)
 - [Walmylson Castro]()

## Organização de diretórios

