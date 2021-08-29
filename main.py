from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import requests
import json
from pymongo import MongoClient

DB = MongoClient("").tencui.tencui
SID = "YOUR_SID"
AUTH_TOKEN = "YOUR_AUTH_TOKEN"
PHONE_NUMBER = "TWILIO_PHONE_NUMBER"
# Twilio SID y Auth Token
client = Client(SID, AUTH_TOKEN)
app = Flask(__name__)

# Ruta POST para mandar mensaje de notificacion
@app.route('/message/add')
def add_notification():
    number_list = []
    for number in number_list:
        client.messages.create(
            body = 'TEXTO DE PRUEBA',
            from_ = PHONE_NUMBER,
            to = number
        )

@app.route('/get', methods = ['GET'])
def send_hw():
    raw_data = list(db.find({}))
    return json.dumps(raw_data)

@app.route('/sms', methods = ['GET', 'POST'])
def get_response():
    tareas_response = requests.get("http://localhost:5000/homework")
    tareas_txt = tareas_response.text
    datos = json.loads(tareas_txt)
    tareas = ' '.join(datos['tareas'])
    message_body = request.values.get('Body', None)
    # crear variable con el mensaje del usuario
    response = MessagingResponse()
    # determinar la respuesta correcta al mensaje
    if message_body.lower() == 'tareas':
        response.message('Tus tareas son:' + tareas)
    return str(response)

@app.route('/add', methods = ['POST'])
def add_data():
    request_data = request.get_json()
    db.insert_one(request_data)

if __name__ == '__main__':
    app.run(debug = True)
