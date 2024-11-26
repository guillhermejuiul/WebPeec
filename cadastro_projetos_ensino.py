import json
import os

ENSINO_FILE = 'ensino.json'

def load_ensino():
    """Carrega os dados do ensino do arquivo JSON."""
    if not os.path.exists(ENSINO_FILE):
        return []
    with open(ENSINO_FILE, 'r') as file:
        return json.load(file)

def save_ensino(ensinos):
    """Salva a lista de ensinos no arquivo JSON."""
    with open(ENSINO_FILE, 'w') as file:
        json.dump(ensinos, file, indent=4)

def add_ensino(nome_ensino, lider, vice_lider, contato, descricao, foto_filename):
    ensinos = load_ensino()

    # Verifica se já existe um ensino com o mesmo nome
    for ensino in ensinos:
        if ensino['nome_ensino'] == nome_ensino:
            return False

    ensinos.append({
        'nome_ensino': nome_ensino,
        'lider': lider,
        'vice_lider': vice_lider,
        'contato': contato,
        'descricao': descricao,
        'foto': foto_filename  
    })

    save_ensino(ensinos)
    return True

def get_ensino():
    """Retorna a lista de ensino carregada do arquivo JSON."""
    return load_ensino()
