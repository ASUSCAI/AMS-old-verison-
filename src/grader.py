from calendar import weekday
import peoplesoft


def grade():
    # start, end = peoplesoft.getTimes(57271)
    # print(start, end)

    nums = peoplesoft.getCanvasNums()
    for num in nums:
        if weekday() in peoplesoft.getDays(num):
            start, end = peoplesoft.getTimes(num)
grade()