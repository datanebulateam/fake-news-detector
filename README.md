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



## Utilização

Descreva aqui quais os passos necessários (dependências externas, comandos, etc.) para replicar o seu projeto. Instalação de dependências necessárias, criação de ambientes virtuais, etc. Este modelo é baseado em um projeto utilizando o [Poetry](https://python-poetry.org/) como gerenciador de dependências e ambientes virtuais. Você pode utilizar o `conda`, ambientes virtuais genéricos do Python ou até mesmo containers do docker. Mas tente fazer algo que seja facilmente reprodutível.

## Desenvolvedores
 - [Contribuidor 1](http://github.com/contribuidor_1)
 - [Contribuidor 2](http://github.com/contribuidor_2)

## Organização de diretórios

> **Nota**: essa seção é somente para entendimento do usuário do template. Por favor removê-la quando for atualizar este `README.md`

```
.
├── data/                   # Diretório contendo todos os arquivos de dados (Geralmente está no git ignore ou git LFS)
│   ├── external/           # Arquivos de dados de fontes externas
│   ├── processed/          # Arquivos de dados processados
│   └── raw/                # Arquivos de dados originais, imutáveis
├── docs/                   # Documentação gerada através de bibliotecas como Sphinx
├── models/                 # Modelos treinados e serializados, predições ou resumos de modelos
├── notebooks/              # Diretório contendo todos os notebooks utilizados nos passos
├── references/             # Dicionários de dados, manuais e todo o material exploratório
├── reports/                # Análioses geradas como html, latex, etc
│   └── figures/            # Imagens utilizadas nas análises
├── src/                    # Código fonte utilizado nesse projeto
│   ├── data/               # Classes e funções utilizadas para download e processamento de dados
│   ├── deployment/         # Classes e funções utilizadas para implantação do modelo
│   └── model/              # Classes e funções utilizadas para modelagem
├── pyproject.toml          # Arquivo de dependências para reprodução do projeto
├── poetry.lock             # Arquivo com subdependências do projeto principal
├── README.md               # Informações gerais do projeto
└── tasks.py                # Arquivo com funções para criação de tarefas utilizadas pelo invoke

```
