import requests
import json
import sys
import urllib.parse
from flask import Flask, request, send_file, send_from_directory, safe_join, abort, jsonify
import subprocess

app = Flask(__name__)
app.config["output"] = "output/"

@app.route("/", methods=['POST'])
def home():
    if request.method == 'POST':
        fp = open('output/doc.tex', 'w')
        fp.write("""\\documentclass{article}
\\usepackage{amsmath}
\\thispagestyle{empty}
\\begin{document}
\\begin{gather*}
""")
        fp.write(request.json['tex'])
        fp.write("""\\end{gather*}
\\end{document}
""")
        fp.close()
        subprocess.call(['./compile.sh'])
        try:
            return send_from_directory(app.config["output"], filename="output.png", as_attachment=True)
        except FileNotFoundError:
            abort(404)



if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)
