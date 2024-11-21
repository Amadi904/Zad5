from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form["user_input"]
        return f"Received: {data}"
    return '''
    <form method="POST">
        <input type="text" name="user_input" placeholder="Enter data" required>
        <button type="submit">Submit</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
