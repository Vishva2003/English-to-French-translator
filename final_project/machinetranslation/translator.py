import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['c5BPQ305-wDB-A8sXUHlS8socJOUM2n9y9qhMvvbcyh4']
url = os.environ['https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/83fa0e0f-0fa7-431b-95b9-5e3648a1eca3']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    ''' Translate English to French '''
    french_text = language_translator.translate(
    text = english_text,
    model_id = 'en-fr').get_result()
    french_text = french_text['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    ''' Translate French to Enflish '''
    english_text = language_translator.translate(
    text = french_text,
    model_id = 'fr-en').get_result()
    english_text = english_text['translations'][0]['translation']
    return english_text