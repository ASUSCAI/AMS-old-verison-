from calendar import weekday
from xml.sax.handler import EntityResolver
import peoplesoft
from canvasapi import Canvas
import datetime as date
import sqlite3
import time

conn = sqlite3.connect("sample.db")
cursor = conn.cursor()


# Canvas API URL
API_URL = "https://canvas.instructure.com/"

# Canvas API Key
API_KEY = "7~WzcUAwH59JqOHTgALQ7nrrUrlQVwcvXKcrhhyyUWPyYdB1l04l7TiBK0cGkH8JpT"

# Initializing canvas object
canvas = Canvas(API_URL, API_KEY)

todayDate = date.datetime.now().date()

currentMonth = date.datetime.now().month
currentDay = date.datetime.now().day
current = ['Attendance for ', currentMonth,"/",currentDay]

def grade():
    # start, end = peoplesoft.getTimes(57271)
    # print(start, end)

    courseNums  = peoplesoft.getCanvasNums()
    for courseNum in courseNums:
        if weekday() in peoplesoft.getDays(courseNum):
            start, end = peoplesoft.getTimes(courseNum)

            x = [todayDate, start]
            y = [todayDate, end]

            startTime = date.datetime.fromisoformat(x)
            endTime = date.datetime.fromisoformat(y)

            unixStartTime = time.mktime(startTime.timetuple())
            unixEndTime = time.mktime(endTime.timetuple())

            course = canvas.get_course(courseNum)

            assignment = course.create_assignment({
                'name' : current,
                'submission_types' : 'none',
                'notify_of_update' : False,
                'points_possible' : 1,
                'assignment_group_id' : 10,
                'published' : True
            })

            studentList = courseNum.get_users(enrollment_type = ['student'])
            for student in studentList:
                command = '''SELECT * FROM KeycardScans WHERE room = ? AND sid = ? '''
                cursor.execute(command, (peoplesoft.getRoom(courseNum), int(student.name)))
                entries= cursor.fetchall()
                
                passed = False

                i = 0

                while(i < len(entries)):
                    if entries[i][3] == 1 :
                        if entries[i][0] > unixStartTime - 900 and entries[i][0] < unixStartTime + 900 :
                            i += 1
                            if entries[i][0] > unixEndTime - 900 and entries[i][0] < unixEndTime + 900 :
                                passed = True
                
                    
                sub1 = assignment.get_submission(student.id)

                if passed :
                    sub1.edit(submission = {'posted_grade' : 1})
                else:
                    sub1.edit(submission = {'posted_grade' : 0})



grade()
conn.commit()
conn.close()