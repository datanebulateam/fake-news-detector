# Detector de Fake News

Este projeto realiza a detecção de notícias que podem ser ou não Fake News. Nos últimos anos a forma como as pessoas estão tendo acesso à informação tem mudado bastante, hoje não temos apenas a TV, o Rádio e o Jornal Impresso para recebermos qualquer notícia, a internet possibilitou ir muito além, podemos acessar qualquer informação em qualquer lugar e a qualquer hora. A internet ao mesmo tempo que nos possibilita sermos pessoas mais informadas e conectadas com todo o Globo, também se tornou um meio eficiente para difundir notícias falsas em massa. Atualmente podemos dizer que é até difícil ter certeza que uma notícia sobre um determinado assunto é verdadeira ou não. Baseado nisso esse projeto busca realizar de forma automatizada a detecção de notícias falsas, ou seja, Fake News.

## Objetivos e resultados chave

O objetivo principal do projeto é fazer a detecção de notícias Fake.

- Organizar o projeto
  - Selecionar a melhor ferramenta para gerenciamento de tarefas
  - Registrar as tarefas em etapas, A fazer, Executando, Concluído e Impedimento

- Selecionar a base de dados
  - Selecionar a base de dados, primeiramente dentro da plataforma Kaggle
  - Criar uma nova base de dados com notícias do Brasil em português
 
- Realizar a analise exploratória dos dados
  - Identificar as variáveis disponíveis, descreve-las e definir os tipos de dados
  - Realizar transformação de variáveis (codificação)
  - Tratar de valores faltantes e valores discrepantes
  - Realizar algumas visualizações gráficas
  - Compreender o DataFrame

- Criar modelo de detecção de Fake News
  - Realizar transformação de dados textuais utilizando o tf-idf
  

## Conteúdo

Atualmente o projeto possui três arquivos de notebook

00-AnaliseExploratoriaFakeNews: Neste notebook foi realizado a analise exploratória dos dados. Para tanto foi feito um pré tratamento dos dados, como alterações de tipos de variáveis, cálculos para quantificar os valores das variáveis e a visualização dos dados, encerrando com as conclusões que foram feitas a partir da análise dos dados.

01-Preparandoosdados: Esse notebook foi o de preparação dos dados frente a analise realizada anteriormente.

02-Treinamentodomodelo: Esse notebook é onde está sendo executado o modelo de Classificação que irá classificar as notícias em verdadeiras ou falsas.


## Utilização

Para executar o projeto, foi utilizado o Jupyter Notebook para execução de código em Python, as principais bibliotecas necessárias para a execução dos notebook foram Numpy e  Pandas para a manipulação dos dados, Seaborn e Matplotlib para visualização de gráficos estatísticos e o WordCloud para visualizar nuvens de palavras.

## Desenvolvedores
 - [Alexsandro Lopes](http://github.com/contribuidor_1)
 - [Crislane Maria](http://github.com/contribuidor_2)
 - [Claudiane Gomes](https://github.com/ClaudianeGomes0409)
 - [Walmylson Castro]()

## Organização de diretórios

