import re

def clean_books(raw_books):
    clean = []
    ratings_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}

    for title, price, availability, rating in raw_books:
        price = float(re.sub(r"[^0-9.]", "", price))
        availability = "In stock" in availability
        rating = ratings_map.get(rating, 0)

        clean.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating
        })

    return clean