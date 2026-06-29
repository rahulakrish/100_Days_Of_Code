from flask import Flask

app = Flask(__name__)
# print(__name__)
#refer to __name__.txt for more on this

@app.route("/")
def home():
    return "Hello, Flask is running in VS Code!"

"""
you need to run this in the terminal
make sure thatthe path points to where the file is
however, when you run this, nothing will happen

you need to tell the flask framework the name of the file that contains the server
here, the hello.py file contains the server.
so, you need to tell Flask to look at this file for you to see your website
in the flask framework, that info is stored in the environment variable called FLASK_APP
in the tutorial, she talks about the different methods for setting the environment variable in mac and windows
but that is outdated. per the latest docs, it does not look like you nede to set that

instead, per the docs you ned to use the following command in the terminal: flask --app hello run
this will run on the development server and you can see the website.

"""

if __name__ == '__main__':
    app.run()

"""
you can run the file in two ways:
1. you can use the command flask -app hello run in the terminal
or
2. you can run the code using the if statement. if you use that, then you can tap into the run() method of the app class
to run the flask server.

"""




