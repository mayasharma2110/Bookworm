import os
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world again 456"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # dont forget to change this to debug False prior to project
            # submission!
            debug=True)
