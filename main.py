from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import requests
import json
from replit import db
import ast

SID = ""
AUTH_TOKEN = ""
PHONE_NUMBER = ""
# Twilio SID y Auth Token
client = Client(SID, AUTH_TOKEN)
app = Flask(__name__)

db["events"] = []

@app.route('/')
def main():
    return 'funciona ;)'

# Ruta POST para mandar mensaje de notificacion
@app.route('/message/add')
def add_notification():
  db["number_list"] = ""
  for number in db["number_list"]:
    client.messages.create(
            body = 'TEXTO DE PRUEBA',
            from_ = PHONE_NUMBER,
            to = number
        )

@app.route('/get', methods = ['GET'])
def send_hw():
  res=[]
  for i in db["events"]:
    res.append(i)
    print(i)
  return str(res) # no se puede hacer return de listas xd

@app.route('/sms', methods = ['GET', 'POST'])
def get_response():
    tareas_response = requests.get("https://moccasinyouthfulcells.scidroid.repl.co/get")
    datos = tareas_response.text
    datos = datos.replace('ObservedDict(value=', "")
    datos = datos.replace(')', '')
    datos = ast.literal_eval(datos)
    #tareas = ' '.join(datos)
    message_body = request.values.get('Body', None)
    # crear variable con el mensaje del usuario
    response = MessagingResponse()
    # determinar la respuesta correcta al mensaje
    if message_body.lower() == 'actividad':
      response.message('Tu actividad más reciente es: ' + str(datos[-1]['title']))
    elif message_body.lower() == 'info':
      response.message('La información de tu tarea más reciente es: ' + str(datos[-1]['description']))
    elif message_body.lower() == 'ayuda':
      response.message('Comandos disponibles: \ninfo (información de tarea), \ntareas (nombre de tarea más reciente)')
    return str(response)

@app.route('/add', methods = ['POST', 'GET'])
def add_data():
    request_data = json.loads(request.data)
    db["events"].append(request_data)
    print(request_data)
    return "agregado"

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=8080)
