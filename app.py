import requests
import sys
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=['POST'])
def home():
    if request.method == 'POST':
        fp = open('output/doc.tex', 'w')
        fp.write("""\\documentclass{article}
\\usepackage{amsmath}
\\thispagestyle{empty}
\\begin{document}
\\begin{gather*}
    x^2 + 4x + 4
\\end{gather*}
\\end{document}
""")
        fp.close()
        subprocess.call(['./compile.sh'])
        print(request.form['tex'])
        return request.form['tex']



if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)
