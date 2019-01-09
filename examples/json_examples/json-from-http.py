import json
import requests


# Get placeholder dummy data from jsonplaceholder.

# Example of one of the json entries returned
# {
#     "userId": 1,
#     "id": 1,
#     "title": "delectus aut autem",
#     "completed": false
# }

response = requests.get("https://jsonplaceholder.typicode.com/todos")

# Parse the json into a list, containing 1 json entry per array value.
todos = json.loads(response.text)

# Display the userId of the first todos json value. 
print(todos[0]['userId'])