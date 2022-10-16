from calendar import weekday
from xml.sax.handler import EntityResolver
import peoplesoft
from canvasapi import Canvas
import datetime as date
import sqlite3
import time
import zoom

conn = sqlite3.connect("sample.db")
cursor = conn.cursor()


# Canvas API URL
API_URL = "https://canvas.instructure.com/"

# Canvas API Key
API_KEY = "7~WzcUAwH59JqOHTgALQ7nrrUrlQVwcvXKcrhhyyUWPyYdB1l04l7TiBK0cGkH8JpT"

# Initializing canvas object
canvas = Canvas(API_URL, API_KEY)
TOLERANCE = 300

todayDate = date.datetime.now().date()

currentMonth = date.datetime.now().month
currentDay = date.datetime.now().day
current = 'Attendance for ' + str(currentMonth) + "/" + str(currentDay)

def grade():
    # start, end = peoplesoft.getTimes(57271)
    # print(start, end)

    courseNums  = peoplesoft.getCanvasNums()
    for courseNum in courseNums:
        # if weekday() in peoplesoft.getDays(courseNum):
            start, end = peoplesoft.getTimes(courseNum)

            # x = [todayDate, 'T', start]
            # y = [todayDate, 'T', end]
            x = str(todayDate) + 'T' + str(start)
            y = str(todayDate) + 'T' + str(end)

            startTime = date.datetime.fromisoformat(x)
            endTime = date.datetime.fromisoformat(y)

            unixStartTime = int(time.mktime(startTime.timetuple()))
            unixEndTime = int(time.mktime(endTime.timetuple()))

            course = canvas.get_course(courseNum)

            assignment = course.create_assignment({
                'name' : current,
                'submission_types' : 'none',
                'notify_of_update' : False,
                'points_possible' : 1,
                'assignment_group_id' : 1,
                'published' : True
            })

            studentList = course.get_users(enrollment_type = ['student'])
            for student in studentList:
                command = '''SELECT * FROM KeycardScans WHERE room = ? AND sid = ? '''
                cursor.execute(command, (peoplesoft.getRoom(courseNum), int(student.name)))
                
                entries = cursor.fetchall()
                # print(entries)

                
                passed = False

                if (len(entries) != 0):
                    i = 0

                    while(i < len(entries)):
                        print(entries[i][3])
                        if entries[i][3] == 1:
                            print('Start: ', unixStartTime, entries[i][0])
                            if entries[i][0] > unixStartTime - TOLERANCE and entries[i][0] < unixStartTime + TOLERANCE:
                                i += 1
                                if i == len(entries): continue
                                if entries[i][0] > unixEndTime - TOLERANCE and entries[i][0] < unixEndTime + TOLERANCE:
                                    print('End: ', unixEndTime, entries[i][0])
                                    passed = True
                        i += 1
                    
                sub1 = assignment.get_submission(student.id)

                if passed:
                    sub1.edit(submission = {'posted_grade' : 1})
                else:
                    sub1.edit(submission = {'posted_grade' : 0})
                # studentList.remove(student)
            
            print(studentList)
            zoomGrade(course, assignment, start, end)
    
def zoomGrade(course, assignment, start, end):
    studentList = course.get_users(enrollment_type = ['student'])
    for student in studentList:
        sub = assignment.get_submission(student.id)
        if sub.score == 0:
            if zoom.startTime(student.name) > start - TOLERANCE and zoom.startTime < start + TOLERANCE:
                if zoom.endTime(student.name) > end - TOLERANCE and zoom.endTime < end + TOLERANCE:
                    sub.edit(submission = {'posted_grade' : 1})
            pass


grade()
conn.commit()
conn.close()
