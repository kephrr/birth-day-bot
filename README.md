# Required config to get starred with the bot

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Create Date File

In the project directory, you NEED to create a src/data/dates.json file:
with the structure ->

## 
    [
        {
            "id": int,
            "nom": string,
            "number": string,
            "date": "dd-yy",
            "gender": int
        }
    ]

for the gender, different values are :

## 
    gender_values = {
        0: 'girl'
        1: 'boy'
        2: 'other/lover'
    }

## Configure

Then (if wanted) configure your formulas and Data File (.json). Initial config perfectly works

## Development run

Run the bot in development with the following command ->

### `python3 ./src/app.py` 

## Deployment

Deployment advices will be updated very soon !!