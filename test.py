from flask import Flask, g, request, render_template
from calhacks import *

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html', lat_lon = lat_lon, center = center)

if __name__ == "__main__":
    app.run()