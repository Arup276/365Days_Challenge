import pymongo

# 27017 is the port number where the server is connect
uri = "mongodb://127.0.0.1:27017"
# mongo db client
client = pymongo.MongoClient(uri)
database = client["fullstack1"]
collection = database['students']

# students = collection.find({})
'''# print(students) ## we just can't use print because its return a "pymongo.cursor.Cursor object"

for student in students:
    print(student)'''

# list comprehension
students = [student for student in collection.find({}) if student['roll'] == 56.0]
print(students)  # output is in one line




