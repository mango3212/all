from flask import Flask
import subprocess
app = Flask(__name__)
@app.route("/")
def index():
    return '''
    <p>menu     :</p>
    <a href="/shut">restart your pc.</a>
    <a href="/shutdown">shutdown your pc.</a>
    '''
@app.route("/shutdown")
def shutd():
    subprocess.run(['shutdown','-s','-t','0'])
    return "bye :)"
@app.route("/shut")
def shuljtd():
    subprocess.run(['shutdown','-r','-t','0'])
    return "bye :)"

if __name__ == "__main__":
    app.run()
