from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/orbita-creativa')
def orbita_creativa():
    return render_template('orbita_creativa.html')

@app.route('/nova-tienda')
def nova_tienda():
    return render_template('nova_tienda.html')

@app.route('/psicoestacion')
def psicoestacion():
    return render_template('psicoestacion.html')

@app.route('/constelacion-astra')
def constelacion_astra():
    return render_template('constelacion_astra.html')

@app.route('/tecnonucleo')
def tecnonucleo():
    return render_template('tecnonucleo.html')

@app.route('/almaceleste')
def almaceleste():
    return render_template('almaceleste.html')

@app.route('/juegos')
def juegos():
    return render_template('juegos.html')

@app.route('/retos')
def retos():
    return render_template('retos.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

if __name__ == '__main__':
    app.run(debug=True)
