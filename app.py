from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    elif request.method == "POST":
        return render_template("login.html")

    return jsonify({"message": "Unrecognized request type"}), 405
                       
if __name__ == '__main__':
    app.run(debug=True)
