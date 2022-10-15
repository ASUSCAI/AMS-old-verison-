# Import the Canvas class
from canvasapi import Canvas

# Canvas API URL
API_URL = "https://canvas.instructure.com/"
# Canvas API key
API_KEY = "7~as8LyLp4Z3I2Gksb1d9Ehpx4KphVnDzL8yiPKgQqE5qgqZfTifUoPMg4XjHx4slA"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

course = canvas.get_course(5493217)

print(course.name)