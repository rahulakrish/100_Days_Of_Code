
#adding CSS styling to HTML

#import libraries
from flask import Flask, render_template

#initialize
app = Flask(__name__)

#define home page
@app.route("/")
def home():
    return render_template("index1.html")

if __name__ =='__main__':
    app.run(debug=True)


#you can add CSS styling to the static folder and within the HTML file, point to the static folder for styling.
#here, in index1.html, CSS style for purple background was added.
#like with HTML images, the CSS stylesheet has to placed in the static folder.



