import json
import os

USERS_FILE = 'usuarios.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, 'r') as file:
        return json.load(file)

def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)

def add_user(usuario, email, senha):
    users = load_users()
    for user in users:
        if user['usuario'] == usuario or user['email'] == email:
            return False
    users.append({'usuario': usuario, 'email': email, 'senha': senha})
    save_users(users)
    return True

def authenticate_user(usuario, senha):
    users = load_users()
    for user in users:
        if user['usuario'] == usuario and user['senha'] == senha:
            return True
    return False
