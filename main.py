from twilio.rest import Client

# Substitua as informações abaixo com suas próprias credenciais Twilio e número de telefone
account_sid = 'SuaContaSid'
auth_token = 'SeuTokenDeAutenticação'
client = Client(account_sid, auth_token)

message = client.messages.create(
    to='Destinatário',
    from_='SeuNúmeroTwilio',
    body='Mensagem de texto de exemplo enviada com o Twilio e Python!')

print(message.sid)
