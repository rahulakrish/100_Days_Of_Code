
#rendering HTML, static images with FLASK

#import relevant library and class
from flask import Flask, render_template

#initialize
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("angela.html")

#rather than write HTML code fully here in Python, you use the render_template method from the Flask library to run HTML files.
#the HTML file is written seperately and passed as an argument to the render_template method.
#writing HTML seperately is a lot easier than writing it in Python. You can use VS Code's tools for HTML to write the files easily.
#the HTML(angela.html) file should be stored in a folder called templates. Flask will specifically look for the file in the folder
#if the folder does not exist, then nothing will run. This is how it is. No way around.

#like with HTML files, images have to be stored in a folder called static.
#Flask will look for images in that folder specifically.

#within the HTML file, you will point to the static folders for the images



if __name__ == "__main__":
    app.run(debug=True)

