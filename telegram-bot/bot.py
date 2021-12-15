import telebot
from pickle import load

import requests
import validators
from nltk.stem.snowball import PortugueseStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
chave_api = "5051039864:AAFoaDyRNGrZMMZiIVSTPLMKSTHeYGN28OY"


stemmer = PortugueseStemmer()
analyzer = TfidfVectorizer().build_analyzer()
def stemmed_words(doc):
    return (stemmer.stem(w) for w in analyzer(doc))

def get_title(url):
    params = {'source_url': url}
    r = requests.get('https://api.outline.com/v3/parse_article', params=params)
    if r.status_code == 200:
        if r.json()['data']['date']:
            return r.json()['data']['title']
    return False

def predict(text):
    header = f'Notícia detectada: *{text}*'
    prob = model.predict_proba([text])[0][1]
    if prob> 0.3:
        return (
            f'{header}\n\nResposta: Tome cuidado, esta notícia tem *{prob*100:.1f}% * de chance de ser falsa!'
            'Mas lembre-se, isso é apenas uma predição. Aqui segue um guia prático de como analisar a veracidade de notícias.'
            '\n\n https://www.cnj.jus.br/programas-e-acoes/painel-de-checagem-de-fake-news/guia-pratico/'
            )
    return (
        f'{header}\n\nResposta: Fique tranquilo, essa notícia tem *{(1-prob)*100:.1f}%* de probabilidade de ser verdadeira.'
        'Mas lembre-se, isso é apenas uma predição. Aqui segue um guia prático de como analisar a veracidade de notícias.'
        '\n\n https://www.cnj.jus.br/programas-e-acoes/painel-de-checagem-de-fake-news/guia-pratico/'
        )

bot = telebot.TeleBot(chave_api)

model = load(open('models/modelofinal.joblib', 'rb'))

@bot.message_handler(commands=['start', 'help'])
def responder(mensagem):
    texto = (
        'Olá, eu sou um bot que realiza análises de notícias. Você pode verificar '
        'a notícia utilizando o link ou apenas copiando o título da reportagem'
    )
    bot.reply_to(mensagem,texto)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if validators.url(message.text):
        response = get_title(message.text)
        if response:
            response = predict(response)
        else:
            response = 'Desculpe, não consegui processar essa URL. Tente copiar o título da reportagem!'
    else:
        response = predict(message.text)
    bot.reply_to(message, response, parse_mode= 'Markdown')  

bot.polling()