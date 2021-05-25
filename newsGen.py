import random
import problems
import discovered
import solutions
import someone
import datetime

today = datetime.date.today()

def newsGen():
    # for i in range(5):
        print(today)
        print("There were discovered " + random.choice(problems.problems) +
              " " +random.choice(discovered.when) +
              " and " + random.choice(someone.clever) +
              " decide to " + random.choice(solutions.solutions))

