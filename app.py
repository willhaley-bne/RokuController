from flask import Flask, Response
from flask_cors import CORS
from RokuKeypress import RokuKeypress

app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/primecode/<tv>/<code>')
def primecode(tv, code):

    ip = None

    if str(tv).lower() == 'office':
        ip = '192.168.1.250'

    if str(tv).lower() == 'living':
        ip = '192.168.1.105'

    if str(tv).lower() == 'master':
        ip = '192.168.1.181'

    roku = RokuKeypress.RokuKeypress(ip)
    roku.command_list(code)
    roku.end()
    return 'True'


if __name__ == '__main__':
    app.run()
