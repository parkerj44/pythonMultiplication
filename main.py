#Parker Johnson
#Ten question multiplication quiz that allows 3 attempts per question and 8 seconds per attempt

import random, time
from quizDocs import Question, TimeLimitException, AttemptLimitException

def questionList(numberOfQuestions):
  li = []

  #adds amount of numberOfQuestions, Question object to list
  for question in range(numberOfQuestions):
    #multiplication questions from 1-15
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)

    li.append(Question('#%s: %s x %s = ' % (question, num1, num2), num1 * num2))

  return li

#Checks if answer is a number and is correct
def answerCheck(answer, question):
  if answer.isdigit():
    if int(answer) == question.answer:
      return True
  return False

#try except for time limit of 10 and 3 attempts
def answerLoop(li):
  correctAttempts = 0
  for question in li:
    try: 
      attempts = 0
      correct = False
      #Loop continues for three tries
      while attempts < 3 and not correct:
        start = time.time()
        answer = input(f'{question.questionText}')
        end = time.time()
        #checks if time to answer was above 10 seconds
        if end - start > 10:
          #exits try if true
          raise TimeLimitException
        #if answer is incorrect, increase attempt count
        if answerCheck(answer, question) == False:
          print('Incorrect.')
          attempts += 1
          #exception if over 3 attempts
          if attempts == 3:
            raise AttemptLimitException
        else:
          correct = True
    except TimeLimitException:
      print('Out of time!')
    except AttemptLimitException:
      print('Out of attempts!')
    except Exception as e:
      print(e)
    else:
      print('Correct!')
      correctAttempts += 1

  return correctAttempts

def main():
  numberOfQuestions = 10
  correct = 0
  li = questionList(numberOfQuestions)

  
  correct += answerLoop(li)
  print('You got %s/10 correct!' % (correct))
      

main()
