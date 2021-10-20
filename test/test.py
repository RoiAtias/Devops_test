
# import urllib library
from urllib.request import urlopen
  
import json
import random

score = 0


import string

NUMBER_OF_ATTEMPTS = 2
ENTER_ANSWER = 'Hit %s for your answer\n'
TRY_AGAIN = 'Incorrect!!! Try again.'
CORRECT = 'Correct'
NO_MORE_ATTEMPTS = 'Incorrect!!! You ran out of your attempts'

def question(message, options, correct, attempts=NUMBER_OF_ATTEMPTS):
    print (message)
    while attempts > 0:
        response = input(ENTER_ANSWER % ', '.join(options))
        if response == correct:
            print (CORRECT)
            return True
        
        else:
            attempts -= 1
            print (TRY_AGAIN)

    print (NO_MORE_ATTEMPTS)
    return False

    

urlQuestion = "https://d-wwts.ext.hp.com/qna/questions.json"
urlAnswers = "https://d-wwts.ext.hp.com/qna/answers.json"

responseQuestionsAndAnswers = urlopen(urlQuestion)
responseQandA_json = json.loads(responseQuestionsAndAnswers.read())
  
responseCurrectAnswers = urlopen(urlAnswers)
responseUrlCurrectAnswers_json = json.loads(responseCurrectAnswers.read())
  
random_item = random.choice(responseQandA_json)

questionId = random_item['id'];
filterAnswer = [f for f in responseUrlCurrectAnswers_json if f["id"] == questionId]
ans = filterAnswer[0]['a'];
question2 = question(random_item['q'], random_item['a'], ans)






