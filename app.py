listings = [
    {"price": 80000, "sqm": 70, "bedrooms": 2},
    {"price": 120000, "sqm": 90, "bedrooms": 3},
    {"price": 95000, "sqm": 75, "bedrooms": 2},
    {"price": 150000, "sqm": 110, "bedrooms": 4},
    {"price": 68000, "sqm": 60, "bedrooms": 1},
]

def print_listings():
    for listing in listings:
        print(
            f"Price: €{listing['price']}, "
            f"Size: {listing['sqm']} sqm, "
            f"Bedrooms: {listing['bedrooms']}"
        )

print_listings()