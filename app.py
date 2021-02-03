from flask import Flask, request, render_template
from repository.memory import Storage
from service.service import Service

app = Flask(__name__)
app.config.from_object(__name__)

repo = Storage()
service = Service(repo)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def root():
    return app.send_static_file('favicon.ico')

@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    key = service.create(data['url'])
    return key

@app.route('/<key>', methods=['GET'])
def get(key):
    val = service.get(key)
    return "not found" if val == None else val

if __name__ == '__main__': # pragma: no cover
    app.run(port=80)
