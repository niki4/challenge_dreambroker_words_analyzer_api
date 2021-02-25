import collections
import string
from typing import List

from flask import Flask, request, abort

app = Flask(__name__)


def sum_chars_count(words_counter) -> int:
    return sum(words_counter.values())


def split_to_words(s: str) -> List[str]:
    return s.split()


def count_ascii_letters(word_list: List[str]):
    counter = collections.Counter()
    result = list()
    for word in word_list:
        counter.update(word.lower())
    chars_length = sum_chars_count(counter)  # len of non-space chars, incl. nums

    for ch in string.ascii_lowercase:  # filter non-letters, e.g. nums
        if counter[ch]:
            result.append({ch: counter[ch]})
    return result, chars_length


@app.route("/analyze", methods=["GET", "POST"])
def analyze():
    if request.method == "POST":
        json_data = request.get_json()  # raise and return "bad request" if non-valid json
        if "text" not in json_data:
            abort(400)
        text = json_data["text"]
        words = split_to_words(text)
        ch_count, ch_len_without_spaces = count_ascii_letters(words)
        return {
            "textLength": {
                "withSpaces": len(text),
                "withoutSpaces": ch_len_without_spaces,
            },
            "wordCount": len(words),
            "characterCount": ch_count,
        }
    else:
        return """
        <p>Send POST request with JSON string to parse, e.g.</p>
        <pre>curl --header "Content-Type: application/json" \
--request POST --data '{"text":"hello 2 times  "}' \
https://mysuperawesomeapi.com/analyze</pre>
        """
