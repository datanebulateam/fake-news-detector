# Detector de Fake News

Este projeto realiza a detecção de notícias que podem ser ou não Fake News. Nos últimos anos a forma como as pessoas estão tendo acesso à informação tem mudado bastante, hoje não temos apenas a TV, o Rádio e o Jornal Impresso para recebermos qualquer notícia, a internet possibilitou ir muito além, podemos acessar qualquer informação em qualquer lugar e a qualquer hora. A internet ao mesmo tempo que nos possibilita sermos pessoas mais informadas e conectadas com todo o Globo, também se tornou um meio eficiente para difundir notícias falsas em massa. Atualmente podemos dizer que é até difícil ter certeza que uma notícia sobre um determinado assunto é verdadeira ou não. Baseado nisso esse projeto busca realizar de forma automatizada a detecção de notícias falsas, ou seja, Fake News.

Um guia de uso do nosso projeto está disponível em: https://crislanem.github.io/fakedetectorbot/

## Objetivos e resultados chave

O objetivo principal do projeto é fazer a detecção de notícias Fake.

- Para a execução do projeto, primeiro foi necessário criar um conjunto de dados. Assim, fizemos alguns scrapys para pegar notícias de sites checkeadores e de jornais famosos.
 
- Com os dados em mãos, fizemos a analise exploratória dos dados
  - Identificando as variáveis disponíveis, descreve-las e definir os tipos de dados
  - Realizando transformação de variáveis (codificação)
  - Tratando de valores faltantes e valores discrepantes

- Criar modelo de detecção de Fake News
  - Realizar transformação de dados textuais utilizando o tf-idf
  - Treinamento do modelo usando Decision Tree, Logistic Regression, MLP and SVC - ainda foi usado um stacked classifier de todos os anteriores, com o SVC sendo o final estimator.
  

## Conteúdo

Atualmente o projeto está quase finalizado. Nele é possível encontrar todo desenvolvimento do projeto, desde os scrapys até a implementação do bot.



## Utilização

Para executar o projeto, foi utilizado o Jupyter Notebook para execução de código em Python, as principais bibliotecas necessárias para a execução dos notebook foram Numpy e  Pandas para a manipulação dos dados, Seaborn e Matplotlib para visualização de gráficos estatísticos e o WordCloud para visualizar nuvens de palavras.

## Desenvolvedores
 - [Alexsandro Lopes](https://github.com/AlexsandroLBS)
 - [Crislane Maria](https://github.com/crislaneM)
 - [Claudiane Gomes](https://github.com/ClaudianeGomes0409)
 - [Walmylson Castro]()


