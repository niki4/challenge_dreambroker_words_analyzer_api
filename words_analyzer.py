from flask import Flask, request

app = Flask(__name__)


@app.route("/analyze", methods=["GET", "POST"])
def analyze():
    if request.method == "POST":
        json_data = request.get_json()  # raise and return "bad request" if non-valid json
        return json_data
    else:
        return """
        <p>Send POST request with JSON string to parse, e.g.</p>
        <code>curl --header "Content-Type: application/json" \
              --request POST --data '{"text":"hello 2 times  "}' \
              https://mysuperawesomeapi.com/analyze</code>
        """
