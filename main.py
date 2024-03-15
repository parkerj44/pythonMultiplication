#Parker Johnson
#Ten question multiplication quiz that allows 3 attempts per question and 8 seconds per attempt

import random, time
from questionClass import Question, TimeLimitException, AttemptLimitException

def questionList(numberOfQuestions):
  li = []

  for question in range(numberOfQuestions):
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)

    li.append(Question('#%s: %s x %s = ' % (question, num1, num2)), num1 * num2)

  return li


def answerCheck(answer, question):
  if answer.isdigit():
    if answer == question.answer:
      return True
  return False

def answerLoop(li):
  for question in li:
    attempts = 0
    start = time.time()
    answer = input(f'{question.questionText}')
    end = time.time()
    ## Trying to figure out where to put if statement if time runs out
    ##Maybe look at try case methods!!!
    try: 
      answer = input(f'{question.questionText}')
      if not answerCheck(answer, question):
        print('Incorrect.')
    except TimeLimitException:
      print('Out of time!')
    except AttemptLimitException:
      print('Out of attempts!')
    else:
      print('Correct!')
      correct += 1

def main():
  numberOfQuestions = 10
  correct = 0
  li = questionList(numberOfQuestions)

  
  answerLoop(li)
      

main()
