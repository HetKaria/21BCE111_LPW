from flask import redirect, render_template, Response, Flask

app = Flask(__name__)

# Hello from Git
# Hello from Mac``
# very good stuff
#Hi
#Hello

# Hello1
#hi2

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/hospital', methods=['POST', 'GET'])
def add_hospital():
    return render_template("Hospital.html")

@app.route('/patients', methods= ["POST", "GET"])
def add_Patients():
    return render_template("Patients.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

#Hi

# Hello
# modification by HetKaria
