# """Server for Takehome Challenge."""

# from flask import (Flask, render_template, request, flash, session,
#                    redirect, url_for, jsonify)
# from jinja2 import StrictUndefined
# import os

# app = Flask(__name__)
# if "SECRET_KEY" in os.environ:
#     app.secret_key = os.environ["SECRET_KEY"]
# else:
#     app.secret_key = "dev"
# app.jinja_env.undefined = StrictUndefined


# @app.route("/")
# def homepage():
#     """Render homepage."""

#     return render_template("homepage.html")


# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0")