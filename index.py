from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/nc')
def about():
    return render_template('Galeria.html')
@app.route('/pc')
def pc():
    return render_template('pc.html')
#@app.route('/')
#def about():
#Siempre poner "render_template('')" con un "return".


if __name__ == '__main__':
    app.run(debug=True) #"debug=True" para activar el "debug mode"

#Luego ves que hacer con el "WARNING". Me da pereza modificar esta parte :v
