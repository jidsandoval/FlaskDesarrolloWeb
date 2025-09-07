from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta_flask_2024'

# Datos de ejemplo con imágenes
servicios = [
    {
        'id': 1,
        'nombre': 'Desarrollo Web',
        'descripcion': 'Creación de sitios y aplicaciones web modernas',
        'precio': 1200,
        'imagen': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80'
    },
    {
        'id': 2,
        'nombre': 'Diseño UX/UI',
        'descripcion': 'Diseño de interfaces atractivas y funcionales',
        'precio': 800,
        'imagen': 'https://images.unsplash.com/photo-1545235617-9465d2a55698?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80'
    },
    {
        'id': 3,
        'nombre': 'Consultoría SEO',
        'descripcion': 'Optimización para motores de búsqueda',
        'precio': 600,
        'imagen': 'https://images.unsplash.com/photo-1589652717521-10c0d092dea9?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80'
    },
    {
        'id': 4,
        'nombre': 'E-commerce',
        'descripcion': 'Tiendas online con pasarelas de pago integradas',
        'precio': 1500,
        'imagen': 'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80'
    },
    {
        'id': 5,
        'nombre': 'Apps Móviles',
        'descripcion': 'Desarrollo de aplicaciones nativas e híbridas',
        'precio': 2000,
        'imagen': 'https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80'
    },
    {
        'id': 6,
        'nombre': 'Branding Digital',
        'descripcion': 'Desarrollo de identidad visual para tu marca',
        'precio': 900,
        'imagen': 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80'
    }
]


@app.route('/')
def index():
    return render_template('index.html', servicios=servicios[:3])


@app.route('/servicios')
def listar_servicios():
    return render_template('servicios.html', servicios=servicios, titulo="Todos Nuestros Servicios")


@app.route('/servicio/<int:servicio_id>')
def detalle_servicio(servicio_id):
    servicio = next((s for s in servicios if s['id'] == servicio_id), None)
    if servicio:
        return render_template('servicios.html', servicios=[servicio], titulo=f"Servicio: {servicio['nombre']}")
    else:
        flash('Servicio no encontrado', 'danger')
        return redirect(url_for('index'))


@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        servicio = request.form['servicio']

        # Aquí normalmente procesarías el formulario (guardar en BD, enviar email, etc.)
        flash(f'¡Gracias {nombre} por contactarnos! Te responderemos pronto sobre {servicio}.', 'success')
        return redirect(url_for('contacto'))

    return render_template('contacto.html', servicios=servicios)


@app.context_processor
def inject_ano_actual():
    return {'ano_actual': datetime.now().year}


if __name__ == '__main__':
    app.run(debug=True)