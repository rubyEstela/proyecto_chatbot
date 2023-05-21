import re
import random
from app import buscarLibros

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

print("********** BIENVENID@ A TU BIBLIOTECA VIRTUAL UCC ************")

def check_all_messages(message):
        highest_prob = {}

        # message = str(message).lower()

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)
        
        # response('Aqui tenemos algunas recomendaciones para IA \n \n' + buscarLibros('IA'), ['IA', 'ia' 'inteligencia', 'artificial',], required_words=['libros'])
        # response('Aqui tenemos algunas recomendaciones', ['inteligencia', 'artificial', ], single_response = True)
        # response('de libros relacionados con el tema buscado', ['inteligencia', 'artificial', ], single_response = True)
        response('Hola', ['hola', 'hi', 'que tal','buenos dias', ], single_response = True)
        response('Aqui tenemos algunas recomendaciones para IA \n \n' + buscarLibros('IA'), ['inteligencia', 'artificial', 'ia',], single_response=True)
        response('Aqui tenemos algunas recomendaciones para PROGRAMACION \n \n' + buscarLibros('PROGRAMACION'), ['java', 'programacion', 'clases',], single_response=True)
        response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes','que', 'tal',], required_words=['como'])
        response('fue un placer atenderl@', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)
        response('en que te puedo ayudar?', ['bien', 'mal', 'va', 'vas', 'sientes','que', 'tal',], required_words=['bien'])

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
    return response

while True:
    print("HOORI: " + get_response(input('You: ')))