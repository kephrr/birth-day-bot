import tweepy

# Remplace par tes propres clés et tokens
api_key = 'TON_API_KEY'
api_secret_key = 'TON_API_SECRET_KEY'
access_token = 'TON_ACCESS_TOKEN'
access_token_secret = 'TON_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def send_direct_message(user_id, text):
    try:
        event = {
            "event": {
                "type": "message_create",
                "message_create": {
                    "target": {"recipient_id": user_id},
                    "message_data": {"text": text}
                }
            }
        }
        api.send_direct_message_new(event)
        print("Message envoyé avec succès !")
    except Exception as e:
        print(f"Erreur lors de l'envoi du message : {e}")