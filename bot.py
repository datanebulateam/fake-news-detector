import telebot
from telebot import types
from pickle import load

import psycopg2
import requests
import validators
from nltk.corpus import stopwords
from nltk.stem.snowball import PortugueseStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

chave_api = "5051039864:AAFoaDyRNGrZMMZiIVSTPLMKSTHeYGN28OY"
bot = telebot.TeleBot(chave_api)



#connection = sqlite3.connect('tests_history.db', check_same_thread=False)
connection = psycopg2.connect(host = 'ec2-54-157-113-118.compute-1.amazonaws.com',dbname = 'd22mcpr5tvgopu', user = 'pvhmxhskrwovep', password = '6bfea686194dada7754c63dd287ce3af48e7720e0c4f8af2536d223eaf8d5085')
cursor = connection.cursor()

msg_feedback = 'Nos ajude deixando o seu feedback: Essa predição foi útil?'
msg_note = ('Lembre-se, isso é apenas uma predição realizada por um modelo de aprendizado de máquina. Confira no link abaixo um guia prático de como analisar a veracidade de notícias.'
'\n\n https://bit.ly/guia-fake-news-jus')


def insert(text,feedback):
    prob_perc = model.predict_proba([text])[0]
    prob = model.predict([text])[0]

    command1 = """CREATE TABLE IF NOT EXISTS
    tests(title TEXT, prob_true REAL, prob_false REAL, label INTEGER, feedback TEXT)"""
    cursor.execute(command1)
    command2 = f"""INSERT INTO tests 
    VALUES('{str(text)}', {float(prob_perc[0])}, {float(prob_perc[1])}, {int(prob)}, {str(feedback)})"""
    cursor.execute(command2)
    connection.commit()

words = stopwords.words('portuguese')
stemmer = PortugueseStemmer()
analyzer = TfidfVectorizer().build_analyzer()

def stemmed_words(doc):
    return (stemmer.stem(w) for w in analyzer(doc))

stem_vectorizer = TfidfVectorizer(analyzer=stemmed_words, stop_words= words)

def get_title(url):
    params = {'source_url': url}
    r = requests.get('https://api.outline.com/v3/parse_article', params=params)
    if r.status_code == 200:
        if r.json()['data']['date']:
            return r.json()['data']['title']
    return False



def predict(text):
    header = f'*Notícia detectada:* _{text}_'
    prob = model.predict_proba([text])[0][1]
    #insert(text)
    
    
    if prob> 0.65:
        return (
            f'{header}\n\n*Resposta*: Tome cuidado, esta notícia tem *{prob*100:.1f}% * de chance de ser falsa!'
            )
    elif prob>= 0.5 and prob<=0.65:
        return (
            f'{header}\n\n*Resposta*: Não temos certeza em relacao a sua notícia, ' 
            f'pois ela tem *{prob*100:.1f}%* de chance de ser falsa!'
            )
    elif prob>= 0.35 and prob<0.5:
        return (
            f'{header}\n\n*Resposta*: Não temos certeza em relação a sua notícia, ' 
            f'pois ela tem *{(1-prob)*100:.1f}%* de chance de ser verdadeira!'
            )
    return (
        f'{header}\n\n*Resposta*: Fique tranquilo, essa notícia tem *{(1-prob)*100:.1f}%* de probabilidade de ser verdadeira.'
        )


model = load(open('models/modelofinal.joblib', 'rb'))

markup_confirm = types.ReplyKeyboardMarkup(row_width=2)
markup_confirm.add(types.KeyboardButton("Sim"), types.KeyboardButton("Não"))


@bot.message_handler(commands=['start', 'help'])
def responder(mensagem):
    texto = (
        'Olá, eu sou um bot que realiza análises de notícias. Você pode verificar '
        'a notícia utilizando o link ou apenas copiando o título da reportagem'
    )
    global id
    id = mensagem.chat.id
    msg = bot.reply_to(mensagem, texto,  reply_markup=False)
    #bot.register_next_step_handler(msg, process_message_step, reply_markup=False)


@bot.message_handler(func=lambda message: True)
def process_message_step(message):
    global title
    noticia = message.text
    title = message.text
    if validators.url(noticia):
        title = get_title(noticia)
        texto = (
            f'A notícia que você enviou tem o seguinte título: '
            f'**{title}**?' 
        )
        msg = bot.reply_to(message, texto, parse_mode='Markdown', reply_markup=markup_confirm)
        bot.register_next_step_handler(msg, verify_message)
    else:
        outcome = predict(title)
        bot.reply_to(message, outcome, parse_mode= 'Markdown')     
        bot.send_message(message.chat.id, msg_note, parse_mode= 'Markdown')
        callback = bot.send_message(message.chat.id, msg_feedback) 
        bot.register_next_step_handler(callback, get_feedback)
        
def verify_message(message):
    if message.text == 'Sim':
        outcome = predict(title) 
        bot.reply_to(message, outcome, parse_mode= 'Markdown')     
        bot.send_message(message.chat.id, msg_note)
        callback = bot.send_message(message.chat.id, msg_feedback)
        bot.register_next_step_handler(callback, get_feedback)
        
    else:
        response = 'Desculpe, não conseguimos processar sua URL, por favor tente enviar o título notícia.'  
        bot.reply_to(message, response)


def get_feedback(message):
    if message.text == 'Sim':
        avaliacao = 1
    else:
        avaliacao = 0
    insert(title, avaliacao)
    bot.reply_to(message, 'Obrigado pelo feedback! :)', reply_markup = False) 
   
bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.infinity_polling()

