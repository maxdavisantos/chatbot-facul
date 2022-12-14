from flask import Flask, render_template, request
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot import ChatBot

input = [
  'Olá',  'Olá, bem vindo ao central de agendamento de instalação de fibra ótica da claro.        Gostaria de agendar a instalação?',
  'Sim', 'Me informe o ceu CPF ou número de instalação' ,
  '32320032',  'Olá Max, para qual data gostaria de agendar sua instalação?',
  '20/11/2022',    'Me confirma o endereço de instalação?',
  'Rua 123, são paulo', 'Para qual horário gostaria de agendar a instalação?',
  '14:00',  'Ok. Agendamento concluído com sucesso para o dia 20/11/2022 às 14 horas.',
  '10:00',  'Ok. Agendamento concluído com sucesso para o dia 20/11/2022 às 10 horas.',
  '11:00',  'Ok. Agendamento concluído com sucesso para o dia 20/11/2022 às 11 horas.',
  'Obrigado', 'Eu quem de agradeço!',
]

bot = ChatBot('Bot Instalação Internet')
bot.set_trainer(ListTrainer)
bot.train(input)

app = Flask(__name__)


@app.route("/")
def home():
  return render_template("index.html")


@app.route("/get")
def get_bot_response():
  userText = request.args.get('msg')
  response = str(bot.get_response(userText))

  return response


app.run(host='0.0.0.0', port=81)
