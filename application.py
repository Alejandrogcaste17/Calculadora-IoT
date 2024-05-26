from flask import Flask, render_template, request, jsonify

application = Flask(__name__)

@application.route("/")
def index():
    return render_template("index.html")

@application.route("/calculate", methods=["POST"])
def calculate():
    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    operation = request.form["operation"]

    result = 0

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            return jsonify({"error": "No se puede dividir por cero."})

    return jsonify({"result": result})

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=80, debug=True)
