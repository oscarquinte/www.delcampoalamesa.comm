from flask import Flask, request, render_template, redirect, url_for
from utils.graficos import crear_grafico_barras, crear_grafico_pastel
import nexmo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/principal')
def principal():
    return render_template('principal.html')

@app.route('/nosotros')
def nosotros():
    grafico_barras = crear_grafico_barras()  
    grafico_pastel = crear_grafico_pastel()  
    return render_template('sobrenosotros.html', grafico_barras=grafico_barras, grafico_pastel=grafico_pastel)

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/productos/mandarina')
def mandarinas():
    return render_template('mandarina.html')

@app.route('/productos/yuca')
def yuca():
    return render_template('yuca.html')

@app.route('/productos/aguacate')
def aguacate():
    return render_template('aguacate.html')

@app.route('/productos/caña')
def caña():
    return render_template('caña.html')

@app.route('/productos/cafe')
def cafe():
    return render_template('cafe.html')

@app.route('/productos/Naranja')
def Naranja():
    return render_template('Naranja.html')

@app.route('/productos/platano')
def platano():
    return render_template('platano.html')

@app.route('/productos/papaya')
def papaya():
    return render_template('papaya.html')

@app.route('/productos/maiz')
def maiz():
    return render_template('maiz.html')

@app.route('/productos/cacao')
def cacao():
    return render_template('cacao.html')

@app.route('/productos/tomate')
def tomate():
    return render_template('tomate.html')

@app.route('/productos/mora')
def mora():
    return render_template('mora.html')

client = nexmo.Client(key="c6303e7e", secret="o9eMfCFKWpgXqn7F")

@app.route('/enviar_sms', methods=['POST'])
def enviar_sms():
    nombre = request.form['nombre']
    producto = request.form['producto']
    cantidad = request.form['cantidad']
    telefono = '+573103759166'  

    mensaje = f"El cliente/a {nombre}, solicita {cantidad} de {producto}. ¡Gracias por tu pedido!  ahora se enviar mensajes gracias a python y al profe Alex jeje"

    response = client.send_message({
        'from': 'Nexmo',
        'to': telefono,
        'text': mensaje,
    })

    if response['messages'][0]['status'] == '0':
        return redirect(url_for('servicios', mensaje='Mensaje enviado con éxito!'))
    else:
        return redirect(url_for('servicios', mensaje=f"Error: {response['messages'][0]['error-text']}"))

if __name__ == '__main__':
    app.run(debug=True)
