import os
import subprocess

from flask import Flask, send_from_directory
from werkzeug.routing import BaseConverter

app = Flask(__name__, static_url_path='', static_folder='build')

class WildcardConverter(BaseConverter):
    regex = r'(|/.*)'
    weight = 200

app.url_map.converters['wildcard'] = WildcardConverter

def launch_build():
    """ start toHTML.py script """
    # build with toHTML.py
    build_cmd = "python src/toHTML.py -f" 
    subprocess.check_output(build_cmd.split())


@app.route('/site<wildcard:path>')
@app.route('/site/<path:path>')
def serve_static_site(path):
    print ("site path : =%s=" % path)
    if path == '/':
        path = 'index.html'
    else if path = "":
        pass # fixme: redirect browser to site/
    print ("site path AFTER: =%s=" % path)
    return send_from_directory('build/last', path)


@app.route('/build')
def build():
    launch_build()
    return 'Build done !'


if __name__ == '__main__':
    app.debug = True
    app.run()