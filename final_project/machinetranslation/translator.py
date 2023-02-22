


import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


from dotenv import load_dotenv

load_dotenv()

apikey="W9SoQ-j0mxlwINgc0bX2N6SIaqKJc7kFPGNvISVcyOul"
url="https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/0a09016b-45d6-4c7e-b542-168a8fecc0af"

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
version='2018-05-01',
authenticator=authenticator
)
language_translator.set_service_url(url)


def english_to_french(english_text: str):
    """Function takes the string in englsh and return translated string in french"""
    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        #Getting the pure translation string
        french_text = translation['translations'][0]['translation']
        return french_text
    except Exception as error:
        print(error)
        return None


def french_to_english(french_text: str):
    """Function takes the string in french and return translated string in english"""
    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        #Getting the pure translation string
        english_text = translation['translations'][0]['translation']
        return english_text
    except Exception as error:
        print(error)
        return None
