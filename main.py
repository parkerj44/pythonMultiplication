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
    try: 
      attempts = 0
      correct = False
      while attempts < 3 and not correct:
        start = time.time()
        answer = input(f'{question.questionText}')
        end = time.time()
        if end - start >= 10:
          raise TimeLimitException
        if not answerCheck(answer, question):
          print('Incorrect.')
          attempts += 1
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
