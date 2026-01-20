def estimate_route(origin, destination):
    """
    Estimates route and distance between two cities (API-free).
    """

    origin = origin.strip().lower()
    destination = destination.strip().lower()

    routes = {
        ("delhi", "haridwar"): (220, "5–6 hours", "Bus / Train"),
        ("haridwar", "ujjain"): (950, "18–20 hours", "Train"),
        ("delhi", "jaipur"): (280, "5 hours", "Bus / Train"),
        ("delhi", "agra"): (230, "4 hours", "Bus / Train"),
        ("mumbai", "pune"): (150, "3 hours", "Bus / Train"),
        ("bangalore", "mysore"): (145, "3 hours", "Bus"),
        ("chennai", "pondicherry"): (160, "4 hours", "Bus"),
        ("kolkata", "digha"): (185, "4 hours", "Bus / Train"),
        ("indore", "ujjain"): (55, "1.5 hours", "Bus / Taxi"),
        ("jaipur", "udaipur"): (400, "7 hours", "Bus / Train"),
        ("delhi", "manali"): (540, "12–14 hours", "Bus"),
        ("delhi", "rishikesh"): (240, "6 hours", "Bus / Train"),
    }

    key = (origin, destination)
    reverse_key = (destination, origin)

    if key in routes:
        distance_km, time, transport = routes[key]
    elif reverse_key in routes:
        distance_km, time, transport = routes[reverse_key]
    else:
        distance_km, time, transport = 300, "Approx. time", "Public Transport"

    route = f"{origin.title()} to {destination.title()} – {distance_km} km ({time}, {transport})"

    return route, distance_km
