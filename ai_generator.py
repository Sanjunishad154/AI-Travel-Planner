def generate_itinerary(days, interest, destination):
    days = int(days)
    interest = interest or "nature"

    activities = {
        "history": [
            "Visit historical monuments",
            "Explore museums and heritage sites",
            "Guided city heritage walk",
            "Visit ancient temples or forts",
            "Local cultural exploration"
        ],
        "nature": [
            "Nature walk and sightseeing",
            "Visit nearby hills or parks",
            "Sunrise viewpoint exploration",
            "Riverbank or waterfall visit",
            "Relax in scenic locations"
        ],
        "beach": [
            "Relax at the beach",
            "Sunset walk along the shore",
            "Local seafood experience",
            "Water activities and sightseeing",
            "Beachside café hopping"
        ],
        "food": [
            "Street food exploration",
            "Local market food tour",
            "Traditional cuisine tasting",
            "Budget cafés and eateries",
            "Famous local food spots"
        ]
    }

    selected = activities.get(interest, activities["nature"])

    itinerary = []

    for d in range(days):
        itinerary.append(
            f"Day {d+1}: {selected[d % len(selected)]} in {destination} using public transport."
        )

    return itinerary
