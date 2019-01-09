#!/usr/bin/python3

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


# Map of userId to number of complete TODOs for that user
todos_by_user = {}

# Increment complete TODOs count for each user.
for todo in todos:
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1

# Create a sorted list of (userId, num_complete) pairs.
top_users = sorted(todos_by_user.items(), 
                   key=lambda x: x[1], reverse=True)

# Because the list has been sorted, the first 
# entry allows you to get the maximum number 
# of completed TODOs.
max_complete = top_users[0][1]

# Create a list of all users who have completed
# the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

print("The users with the most completed tasks are: " + max_users)