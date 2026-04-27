import json

# # Convert the following dictionary into JSON format.

import json
Student_data = {"name": "David", "age":13, "marks":87}
print (type(Student_data))
json_data = json.dumps(Student_data)
print (json_data)
print (type(json_data))



# # # Access the value of age from the given data.

import json


Student_data = {"name": "David", "age":13, "marks":87}
print(Student_data["age"])



# # # Pretty Print following JSON data.
import json

Student_data = {"name": "David", "age":13, "marks":87}
data= json.dumps(Student_data, indent=4, separators=(". ", " = "))
print(data)

Sort the following JSON keys and write them into a file.
Student_data = {"name": "David", "age":13, "marks":87}
f = open("Student_data.json", "w")
json.dump(Student_data, f, indent=4, separators=(". ", " = "), sort_keys=True)
f.close()

# Access the nested key "marks" from the following nested data
student_data = """{ "student":{
                      "grade":{
                        "name" : "David",
                           "marks":{
                              "math":87, }
                         }           
                     }"""
data = json.loads(student_data)
print(data["student"]["grade"]["marks"]["math"])    



