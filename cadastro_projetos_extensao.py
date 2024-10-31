import json
import os

PROJETOS_FILE = 'projetos_extensao.json'

def load_projetos():
    """Carrega os dados dos projetos de extensão do arquivo JSON."""
    if not os.path.exists(PROJETOS_FILE):
        return []
    with open(PROJETOS_FILE, 'r') as file:
        return json.load(file)

def save_projetos(projetos):
    """Salva a lista de projetos de extensão no arquivo JSON."""
    with open(PROJETOS_FILE, 'w') as file:
        json.dump(projetos, file, indent=4)

def add_projeto(nome_projeto, lider, coordenador, contato, descricao, foto_filename):
    """Adiciona um novo projeto de extensão à lista e salva no arquivo."""
    projetos = load_projetos()

    # Verifica se já existe um projeto com o mesmo nome
    for projeto in projetos:
        if projeto['nome_projeto'] == nome_projeto:
            return False

    projetos.append({
        'nome_projeto': nome_projeto,
        'lider': lider,  # Adicionado o campo "líder"
        'coordenador': coordenador,
        'contato': contato,
        'descricao': descricao,
        'foto': foto_filename  
    })

    save_projetos(projetos)
    return True

def get_projetos():
    """Retorna a lista de projetos de extensão carregada do arquivo JSON."""
    return load_projetos()
