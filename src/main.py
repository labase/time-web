from bottle import route, run, get, static_file, template
import bottle
import os

@route('/<request:re:\w\w\w\w\w>')
def record_from_code(request):
    return template("Neurolog - Processo: {{ name }}", name = request)


if __name__ == "__main__":
    run(server='gunicorn', host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=True, workers=1)

app = bottle.default_app()
