import requests
import json
import sys
import urllib.parse
from flask import Flask, request, send_file, send_from_directory, safe_join, abort, jsonify
import subprocess, os

app = Flask(__name__)
app.config["output"] = "output/"

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        fp = open('output/doc.tex', 'w')
        fp.write("""\\documentclass{article}
\\usepackage{amsmath}
\\usepackage{pbox}
\\thispagestyle{empty}
\\begin{document}
""")
        fp.write(request.json['tex'])
        fp.write("""
\\end{document}
""")
        fp.close()

        CMD = 'echo $(source compile.sh; echo $STR)'
        p = subprocess.Popen(CMD, stdout=subprocess.PIPE, shell=True, executable='/bin/bash')
        out = p.stdout.readlines()[0].strip()
        success = int(out.decode('utf-8'))
        dt = request.json['dt']
        os.rename('output/output.png', 'output/output' + str(dt) + ".png")
        if success == 1:
            return '', 204
        else:
            return '', 400

    if request.method == 'GET':
        return """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>TeXBot</title>
    </head>

    <body>
        <img style="-webkit-user-select: none; display: block; margin: auto; padding: env(safe-area-inset-top) env(safe-area-inset-right) env(safe-area-inset-bottom) env(safe-area-inset-left); cursor: zoom-in;" src="output/output.png">
    </body>

</html>"""

@app.route('/output/<filename>')
def send_output(filename):
    return send_from_directory("output/", filename)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000)
