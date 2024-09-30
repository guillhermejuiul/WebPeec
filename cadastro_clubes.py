import json
import os

# Nome do arquivo JSON usado para armazenar os clubes
CLUBES_FILE = 'clubes.json'

def load_clubes():
    """Carrega os dados dos clubes do arquivo JSON."""
    if not os.path.exists(CLUBES_FILE):
        return []
    with open(CLUBES_FILE, 'r') as file:
        return json.load(file)

def save_clubes(clubes):
    """Salva a lista de clubes no arquivo JSON."""
    with open(CLUBES_FILE, 'w') as file:
        json.dump(clubes, file, indent=4)

def add_clube(nome_clube, lider, vice_lider, contato, descricao):
    clubes = load_clubes()

    # Verifica se já existe um clube com o mesmo nome
    for clube in clubes:
        if clube['nome_clube'] == nome_clube:
            return False

    # Adiciona o novo clube com todas as informações, incluindo a descrição
    clubes.append({
        'nome_clube': nome_clube,
        'lider': lider,
        'vice_lider': vice_lider,
        'contato': contato,
        'descricao': descricao  # Novo campo de descrição do clube
    })

    # Salva a lista atualizada de clubes no arquivo JSON
    save_clubes(clubes)
    return True

def get_clubes():
    """Retorna a lista de clubes carregada do arquivo JSON."""
    return load_clubes()
