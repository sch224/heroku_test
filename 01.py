from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Привет от Ивана Николаевича"

@app.route('/about')
def about():
    return 'Тест странички о себе'


if __name__ == '__main__':
    app.run()