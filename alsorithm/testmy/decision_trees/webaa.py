import json
from bottle.bottle import route, run, Bottle

app = Bottle()


@app.route('/')
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name='world'):
    return 'hello %s!' % (name,)


@app.route('/jobs/<offset:int>/<size:int>')
def get_jobs(offset, size):
    d = {"offset": offset, "size": size}
    return json.dumps(d)


run(app,host='localhost', port=8080, debug=True)

