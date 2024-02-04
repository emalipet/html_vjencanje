from flask import Flask, render_template, request
from database import add_guest

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/confirm', methods=['POST'])
def confirm():
    guest_name = request.form['guestName']
    add_guest(guest_name)
    return 'Potvrđeno!'


if __name__ == '__main__':
    app.run(debug=True)
