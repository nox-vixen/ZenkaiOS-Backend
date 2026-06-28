from flask import Blueprint, jsonify, render_template

from backend.home_engine import home_engine

home_bp = Blueprint(
    "home",
    __name__
)

@home_bp.route("/")
def homepage():
    return render_template("home.html")


@home_bp.route("/api/home")
def home():
    return jsonify(home_engine.build())
