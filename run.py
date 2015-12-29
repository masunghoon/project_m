#!.venv/bin/python3

from blog import app

app.run(host='0.0.0.0', port=80, debug=True)
