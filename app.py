# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

app.config['postgres://guxdnmjbofwoac:d33409f0568bac78d191dbd2511c27a1f888d857258d97a9deaf8211db08339f@ec2-3-227-15-75.compute-1.amazonaws.com:5432/da7ntdovasosdk'] = (
    os.environ.get('ec2-3-227-15-75.compute-1.amazonaws.com')
    .replace('postgres://', 'postgresql://', 1)
    )
# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app = Flask(__name__)

@app.route("/")
def index():
   
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)