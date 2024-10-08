# Importa o Flask para o aplicativo
from flask import Flask, render_template

app = Flask(__name__)

SITE = {
    'name': 'FlaskVT', # Nome do site
    'logo': '',        # Font awesome do logotipo
}

@app.route('/')  # Rota para a página inicial → raiz
def home():
    # Passa parâmetros para o template
    # 'css' e 'js' são opcionais
    toPage = {
        # Título da página → <title></title>
        'site': SITE,
        'title': ''
    }


    return render_template('home.html', page=toPage)


@app.route('/contacts')  # Rota para a página de contatos → /contacts
def contacts():

    toPage = {
        'site': SITE,
        'title': 'Faça contato',
        'css': 'contacts.css'
    }

    return render_template('contacts.html', page=toPage)


@app.route('/about')
def about():
    toPage = {
        'site': SITE,
        'title': 'Sobre',
        'css': 'about.css'
    }

    return render_template('about.html', page=toPage)

@app.route('/policies')
def policies():
    toPage = {
        'site': SITE,
        'title': 'Sobre'
    }

    return render_template('policies.html', page=toPage)

if __name__ == '__main__':
    app.run(debug=True, port=80)