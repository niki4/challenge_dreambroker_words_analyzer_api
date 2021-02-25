# py_words_analyzer
The Programming Assignment solution for https://challenge.dreambroker.jobs/

Curl command to call the API might look like this:

            curl --header "Content-Type: application/json" \
            --request POST \
            --data '{"text":"hello 2 times  "}' \
            https://mysuperawesomeapi.com/analyze
            
And the response will be:

        {
            "textLength":{"withSpaces":15,"withoutSpaces":11},
            "wordCount":3,
            "characterCount":[{"e":2},{"h":1},{"i":1},{"l":2},{"m":1},{"o":1},{"s":1},{"t":1}]
        }
            
Please pay attention that the characters array contain only English letters and they are alphabetically ordered.
