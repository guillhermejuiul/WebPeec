from flask import Flask, render_template, request, redirect, url_for, session
from usuarios import add_user, authenticate_user
from cadastro_clubes import add_clube, get_clubes
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads/clubes'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config["SECRET_KEY"] = "chave secreta"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def projetoEscola():
    return render_template("projetoEscola.html")

@app.route('/login', methods=['POST'])  
def login():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    
    if authenticate_user(usuario, senha):
        session["usuario"] = usuario
        return redirect(url_for("telaInicial"))

    return render_template("projetoEscola.html", mensagem_erro="Nome do usuário ou senha errada")

@app.route('/cadastro', methods=['POST'])
def cadastro():
    usuario = request.form.get('usuario')
    email = request.form.get('email')
    senha = request.form.get('password1')
    confirmarsenha = request.form.get('password2')
    
    if senha != confirmarsenha:
        return render_template('projetoEscola.html', mensagem_erro_senhas="Senhas não se assemelham")

    if add_user(usuario, email, senha):
        return redirect(url_for("telaInicial"))
    else:
        return render_template('projetoEscola.html', mensagem_erro_email="Usuário ou e-mail já cadastrados")

@app.route("/logout")
def logout():
    if "usuario" in session:
        del session["usuario"]
    return redirect(url_for("projetoEscola"))

@app.route("/telaInicial")
def telaInicial():
    return render_template("tela.html")

@app.route('/esqueceuAsenha')
def esqueceuAsenha():
    return render_template("esqueceuAsenha.html")

@app.route("/telaclubes")
def telaClubes():
    clubes = get_clubes()
    return render_template("clubes/tela_clubes.html", clubes=clubes)

@app.route("/telacadastroclubes")
def telacadastroclubes():
    return render_template("clubes/cadastrar_clubes.html")

@app.route("/teladeinformações")
def teladeinformacoes():
    return render_template("clubes/clubes_informações.html")

@app.route("/teladeinformações/<nome_clube>")
def informacoesdoclube(nome_clube):
    clubes = get_clubes()
    clube = next((c for c in clubes if c['nome_clube'] == nome_clube), None)
    if clube:
        return render_template("clubes/clubes_informacoes.html", clube=clube)
    return "Clube não encontrado", 404

def allowed_file(filename):
    """Verifica se o arquivo é de um tipo permitido."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/cadastro_clube", methods=['POST'])
def cadastro_clube():
    nome_clube = request.form.get('usuario')
    lider = request.form.get('lider')
    vice_lider = request.form.get('vice_lider')
    contato = request.form.get('contato')
    descricao = request.form.get('descricao')

    if 'foto_clube' not in request.files:
        return render_template("clubes/cadastrar_clubes.html", mensagem_erro_clube="Nenhuma foto foi enviada")

    foto_clube = request.files['foto_clube']


    if foto_clube.filename == '' or not allowed_file(foto_clube.filename):
        return render_template("clubes/cadastrar_clubes.html", mensagem_erro_clube="Arquivo inválido ou não enviado")

    filename = secure_filename(foto_clube.filename)
    foto_clube.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    if add_clube(nome_clube, lider, vice_lider, contato, descricao, filename):
        return redirect(url_for("telaClubes"))
    else:
        return render_template("clubes/cadastrar_clubes.html", mensagem_erro_clube="Clube já cadastrado")

if __name__ == "__main__":
    app.run(debug=True)
