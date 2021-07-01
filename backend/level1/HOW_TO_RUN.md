# Level 1 Solution

## Explanation

This API receives a payload like `data.json` and returns a response like `output.json`, per the specs in the README.
Input validation was also added to ensure that the necessary data is included and that at least one cart is sent.

Flask was chosen as the web framework as it is extremely lightweight. Pytest was chosen as the testing library for its ease of use and readability.

## Running

Please install Flask using the following command:

    python3 -m pip install --upgrade flask

To run the web server:

    export FLASK_APP=main.py
    python3 -m flask run

The server will be running on http://localhost:5000

## Testing

Please install pytest using the following command:

    python3 -m pip install --upgrade pytest

You can then run the tests for this solution with this command:

    python3 -m pytest
