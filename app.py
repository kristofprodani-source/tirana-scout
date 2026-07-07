listings = [
    {"price": 80000, "sqm": 70, "bedrooms": 2},
    {"price": 120000, "sqm": 90, "bedrooms": 3},
    {"price": 95000, "sqm": 75, "bedrooms": 2},
    {"price": 150000, "sqm": 110, "bedrooms": 4},
    {"price": 68000, "sqm": 60, "bedrooms": 1},
]

def print_listings(properties):
    for listing in properties:
        print(
            f"Price: €{listing['price']}, "
            f"Size: {listing['sqm']} sqm, "
            f"Bedrooms: {listing['bedrooms']}"
        )

def filter_by_price(max_price):
    return [listing for listing in listings if listing["price"] <= max_price]

def deal_score():
    prices_per_sqm = [listing["price"] / listing["sqm"] for listing in listings]
    average = sum(prices_per_sqm) / len(prices_per_sqm)

    print(f"\nAverage price per sqm: €{average:.2f}\n")

    for listing in listings:
        price_per_sqm = listing["price"] / listing["sqm"]
        label = "Good Deal" if price_per_sqm <= average else "Bad Deal"

        print(
            f"Price: €{listing['price']}, "
            f"Size: {listing['sqm']} sqm, "
            f"Price/sqm: €{price_per_sqm:.2f} -> {label}"
        )

print("All listings:")
print_listings(listings)

print("\nListings under €100000:")
print_listings(filter_by_price(100000))

print("\nListings under €70000:")
print_listings(filter_by_price(70000))

deal_score()