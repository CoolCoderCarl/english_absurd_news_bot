import random
import problems
import discovered
import solutions
import someone
import datetime
import reporters

# DEPRECATED

today = datetime.date.today()

def newsGen():
    # for i in range(5):
    #     print(today)
    news = ("INNOVATION !!!" + "\n" +
                "=====================================================" + "\n" +
                "There were discovered " + random.choice(problems.problems) +
                " " +random.choice(discovered.when) +
                " and " + random.choice(someone.clever) +
                " decide to " + random.choice(solutions.solutions) + "\n" +
                "=====================================================" + "\n" +
                "The reporter is: " + random.choice(reporters.reporter))

        # print("The reporter is: " + random.choice(reporters.reporter))
    return news
