from flask import Flask, request, render_template
from ai_generator import generate_itinerary
from maps_api import estimate_route
from budget_engine import calculate_budget
from database import init_db
import os

app = Flask(__name__)

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    origin = request.form.get("from")
    destination = request.form.get("to")
    budget = int(request.form.get("budget"))
    days = int(request.form.get("days"))
    interest = request.form.get("interest")
    travel_style = request.form.get("style")

    route, distance_km = estimate_route(origin, destination)
    plan = generate_itinerary(days, interest, destination)

    budget_info = calculate_budget(
        budget=budget,
        days=days,
        travel_style=travel_style,
        distance_km=distance_km
    )

    return render_template(
        "result.html",
        origin=origin,
        destination=destination,
        route=route,
        plan=plan,
        budget_info=budget_info,
        budget=budget
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
