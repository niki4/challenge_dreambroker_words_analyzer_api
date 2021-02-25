import unittest

from words_analyzer import app


class TestWordAnalyzer(unittest.TestCase):
    def test_analyze_valid_json(self):
        input_data = {"text": "hello 2 times  "}
        expected = {
            "textLength": {"withSpaces": 15, "withoutSpaces": 11},
            "wordCount": 3,
            "characterCount": [{"e": 2}, {"h": 1}, {"i": 1}, {"l": 2}, {"m": 1}, {"o": 1}, {"s": 1}, {"t": 1}]
        }
        with app.test_client() as c:
            # Passing the json argument in the test client methods sets the request data to the
            # JSON-serialized object and sets the content type to application/json.
            resp = c.post("/analyze", json=input_data)
            json_resp = resp.get_json()
            for field in expected:
                assert json_resp[field] == expected[field], f"Data mismatch for '{field}':\n" \
                                                            f"expected:\t{expected[field]}\n" \
                                                            f"got:\t\t{json_resp[field]}"
