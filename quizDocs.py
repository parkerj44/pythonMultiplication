#Parker Johnson
import time

class Question:
  def __init__(self, questionText, answer):
    self.questionText = questionText
    self.answer = answer

class AttemptLimitException(Exception):
  pass

class TimeLimitException(Exception):
  pass

def checkTimeLimit(startTime, finish):
  if time.time() > startTime + finish:
    return TimeLimitException()
  
def checkAttemptLimit(attempts, limit):
  if attempts == limit:
    return AttemptLimitException()
