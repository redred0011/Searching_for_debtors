import requests

def send_whatsapp_message(access_token, phone_number, message_template):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "template",
        "template": {
            "name": message_template,
            "language": {
                "code": "en_US"
            }
        }
    }

    url = 'https://graph.facebook.com/v17.0/104404726062000/messages'

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Wiadomość została pomyślnie wysłana!")
    else:
        print("Wystąpił błąd podczas wysyłania wiadomości.")

if __name__ == "__main__":
    # Tymczasowy token dostępu WhatsApp Cloud API
    access_token = 'EAAOdJ9jBJ2oBAO9Fm4y2HZCRdeuZC6YQCyzqZAn13rb4LZCeZAmZCVpmee2Hn3Ovd6qKEXZBC1eYZBnZCZBZAHVhSwZAygEJJ7QsZAPwMTIVdcjulOy6PbPd1nKfXYvflHumYcUv0JR7ZAIZALdT0bRmA7aknySn43CKsTRz6dx42mpn3EUwhucksc6Bb8d5fkJ5d47lgpkH1Lqt0dxkwZDZD'

    # Numer telefonu odbiorcy w międzynarodowym formacie (np. "+48" dla Polski) bez "+"
    recipient_phone_number = 'XXXXXXXXXXX'

    # Nazwa szablonu wiadomości.
    message_template = 'hello_world'   

    # Wysłanie wiadomości
    send_whatsapp_message(access_token, recipient_phone_number, message_template)
