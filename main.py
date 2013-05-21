from bottle import route, run, get, static_file, template
import bottle
import os

@route('/<request>')
def hello(request):
    return template("Processo: {{ name }}", name = request)


if __name__ == "__main__":
    #run(host='i-quarto.herokuapp.com', port=80, debug=True)
    run(server='gunicorn', host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=True, workers=1)
    #run(host='localhost', port=8080, debug=True)

app = bottle.default_app()
