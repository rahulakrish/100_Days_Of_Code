#import libraries
from flask import Flask, render_template

#instantiate
app = Flask(__name__)

#define home page
@app.route("/")
def home():
    return render_template("index2.html")

if __name__ == "__main__":
    app.run(debug=True)



