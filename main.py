from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import urllib

SID = "YOUR_SID"
AUTH_TOKEN = "YOUR_AUTH_TOKEN"
PHONE_NUMBER = "TWILIO_PHONE_NUMBER"
# Twilio SID y Auth Token
client = Client(SID, AUTH_TOKEN)
app = Flask(__name__)

# Ruta POST para mandar mensaje de notificacion
@app.route('/message/add')
def add_notification():
    number_list = "PHONE_NUMBER_LIST"
    for number in number_list:
        client.messages.create(
            body = 'TEXTO DE PRUEBA',
            from_ = PHONE_NUMBER,
            to = number
        )
@app.route('/sms', methods = ['GET', 'POST'])
def get_response():
    message_body = request.values.get('Body', None)
    # crear variable con el mensaje del usuario
    response = MessagingResponse()
    # determinar la respuesta correcta al mensaje
    if message_body.lower() == 'tareas':
        response.message('Tus tareas pendientes son:')
    # TODO: CONSEGUIR TAREAS PENDIENTES DE API
    return str(response)

if __name__ == '__main__':
    app.run(debug = True)
