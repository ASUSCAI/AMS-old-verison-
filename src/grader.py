from calendar import weekday
import peoplesoft
import canvasapi


def grade():
    for courseID in peoplesoft.getCanvasNums():
        if weekday() in peoplesoft.getDays(courseID):
            start, end = peoplesoft.getTimes(courseID)
grade()