import collections
from flask import Flask, request

app = Flask(__name__)


def count_spaces(s: str) -> int:
    return s.count(" ")

def count_words(s: str) -> int:
    return len(s.split())

def count_chars(s: str):
    return collections.Counter(s)

@app.route("/analyze", methods=["GET", "POST"])
def analyze():
    if request.method == "POST":
        json_data = request.get_json()  # raise and return "bad request" if non-valid json
        if "text" not in json_data:
            abort(400)
        return {
            "textLength": {
                "withSpaces": len(json_data["text"]),
                "withoutSpaces": len(json_data["text"]) - count_spaces(json_data["text"]),
            },
            "wordCount": count_words(json_data["text"]),
            "characterCount": count_chars(json_data["text"]),
        }
    else:
        return """
        <p>Send POST request with JSON string to parse, e.g.</p>
        <code>curl --header "Content-Type: application/json" \
              --request POST --data '{"text":"hello 2 times  "}' \
              https://mysuperawesomeapi.com/analyze</code>
        """
