from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/<name>")
def index(name):
    if name.startswith("..") or name.startswith("~"):
        return error_403(403)
    if os.path.isfile("./templates/" + name) and name.endswith("html"):
        return render_template(name, name="test")
    return error_404(404)
    
@app.errorhandler(403)
def error_403(error):
    return render_template("403.html"), 403   
    
@app.errorhandler(404)
def error_404(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
