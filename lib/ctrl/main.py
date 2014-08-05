from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/map')
def map():
    return render_template('map.html')

@main.route('/list')
def list():
    return render_template('list.html')

@main.route('/register')
def register():
    return render_template('parking/register.html')

@main.route('/control/<placeid>')
def control(placeid):
    return render_template('parking/control.html', placeid=placeid)
