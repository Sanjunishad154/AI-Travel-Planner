def calculate_budget(budget, days, travel_style, distance_km):
    budget = int(budget)
    distance_km = int(distance_km)

    # Base percentages
    travel_pct = 0.25
    stay_pct = 0.40
    food_pct = 0.30

    # 🔹 Adjust based on distance
    if distance_km > 500:
        travel_pct += 0.10
        stay_pct -= 0.05
        food_pct -= 0.05

    # 🔹 Adjust based on travel style
    if travel_style == "group":
        stay_pct -= 0.10
        food_pct += 0.05
        travel_pct += 0.05

    travel = int(budget * travel_pct)
    stay = int(budget * stay_pct)
    food = int(budget * food_pct)
    misc = budget - (travel + stay + food)

    return {
        "travel": travel,
        "stay": stay,
        "food": food,
        "misc": misc,
        "total": travel + stay + food + misc,
        "status": "Within Budget"
    }
