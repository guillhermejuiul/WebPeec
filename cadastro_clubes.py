import json
import os

CLUBES_FILE = 'clubes.json'

def load_clubes():
    if not os.path.exists(CLUBES_FILE):
        return []
    with open(CLUBES_FILE, 'r') as file:
        return json.load(file)

def save_clubes(clubes):
    with open(CLUBES_FILE, 'w') as file:
        json.dump(clubes, file, indent=4)

def add_clube(nome_clube, lider, vice_lider, contato):
    clubes = load_clubes()
    for clube in clubes:
        if clube['nome_clube'] == nome_clube:
            return False
    clubes.append({
        'nome_clube': nome_clube,
        'lider': lider,
        'vice_lider': vice_lider,
        'contato': contato
    })
    save_clubes(clubes)
    return True

def get_clubes():
    return load_clubes()
