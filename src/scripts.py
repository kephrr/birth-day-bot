import json
from const import CRITERIA

def generate_message(formula, contact)->str:
    gender=""
    match contact["gender"]:
        case 0 :
            gender = "mon reuf"
        case 1 :
            gender = "ma reuss"
        case 2 :
            gender = "mon amour"
    return modelize(formula, contact["nom"], gender)

# TAKE A FORMULA AND ADAPT TO THE CONTACT
def modelize(formula, name, gender)->str:
    if is_inside_text(CRITERIA['GENDER'], formula) :
        formula = formula.replace(CRITERIA['GENDER'], gender)

    if is_inside_text(CRITERIA['NAME'], formula):
        formula = formula.replace(CRITERIA['NAME'], name)

    if is_inside_text(CRITERIA['EMOJI'], formula):
        formula = formula.replace(CRITERIA['EMOJI'], ":)")

    return  formula

def is_inside_text(mot, txt):
    if mot in txt :
        return True
    return False

# READ FILE
def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# SENDING MESSAGE REQUEST
#def send_message():
# Variables pour l'API
    #url = 'https://graph.facebook.com/v21.0/FROM_PHONE_NUMBER_ID/messages'
    #access_token = 'ACCESS_TOKEN'  # Remplacez par votre token d'accès

    # Données pour le message
    #data = {
    #    "messaging_product": "whatsapp",
    #    "recipient_type": "individual",
    #    "to": "PHONE_NUMBER",  # Remplacez par le numéro de téléphone du destinataire
    #    "type": "text",
    #    "text": {
    #        "preview_url": False,
    #        "body": "MESSAGE_CONTENT"  # Remplacez par le contenu du message
    #    }
    #}

    # En-têtes de la requête
    #headers = {
    #    "Authorization": f"Bearer {access_token}",
    #    "Content-Type": "application/json"
    #}

    # Envoyer la requête
    #response = requests.post(url, headers=headers, data=json.dumps(data))

    # Afficher la réponse
    #if response.status_code == 200:
    #    print("Message envoyé avec succès!")
    #else:
    #    print(f"Erreur: {response.status_code}")
#    print(response.json())
