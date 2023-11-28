from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_sin_descuento = cantidad_tarros * 9000
        descuento_total = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - descuento_total

        return render_template('resultado_ejercicio1.html',
                               nombre=nombre,
                               edad=edad,
                               cantidad_tarros=cantidad_tarros,
                               total_sin_descuento=total_sin_descuento,
                               descuento_total=descuento_total,
                               total_con_descuento=total_con_descuento)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje_bienvenida = None

    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']

        usuarios = {'juan': 'admin', 'pepe': 'user'}

        if nombre in usuarios and usuarios[nombre] == password:
            mensaje_bienvenida = f"Bienvenido {'Administrador' if nombre == 'juan' else 'Usuario'} {nombre}"
        else:
            mensaje_bienvenida = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje_bienvenida=mensaje_bienvenida)

if __name__ == '__main__':
    app.run(debug=True)