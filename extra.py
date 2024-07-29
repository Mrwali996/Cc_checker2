import requests

def hit_sender(card,message,chat_id):
    bot_token = '7362675940:AAEtWNxVCvB4-r8e2SIOzStKLQCAbvyDCaU'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=data)
