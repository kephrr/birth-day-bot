import scripts as bot
import random

contacts = bot.read_json(DATES_FILE)
formulas = bot.read_json(FORMULAS)

for contact in contacts :
    message = bot.generate_message(formulas[random.randint(1, len(formulas))]["content"], contact)
    print(message + "\n")