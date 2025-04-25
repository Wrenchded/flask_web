from flask import Flask
import os
os.system("pip install flask")


app = Flask(__name__)

@app.route('/')
def fibonacci():
    a, b = 0, 1
    result = "Fibonacci sequence up to 8 numbers: <br>"
    for _ in range(8):
        result += f"{a} <br>"
        a, b = b, a + b
    return result

if __name__ == '__main__':
    app.run(debug=True)