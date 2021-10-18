import json
import os

from global_constants import *


def register(username, password, first_name, last_name):
    with open(os.path.join(DB_FOLDER_NAME, USERS_FILE_NAME), 'r+') as file:
        # validation
        for user_line in file:
            user = json.loads(user_line.strip())
            if user['username'] == username:
                return False

        user_obj = {
            'username': username,
            'password': password,
            'firstName': first_name,
            'lastName': last_name
        }

        file.write(json.dumps(user_obj))
        file.write('\n')
        return True


def login(username, password):
    with open(os.path.join(DB_FOLDER_NAME, USERS_FILE_NAME), 'r') as users, \
            open(os.path.join(DB_FOLDER_NAME, SESSION_FILE_NAME), 'w') as session:
        for user_line in users:
            user = json.loads(user_line.strip())
            if user['username'] == username and user['password'] == password:
                session.write(user_line)
                return True
        return False
