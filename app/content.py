"""
Site content for Harvests Gateway Ltd.

Everything the website displays lives here, so text and products can be
edited in one place. When the admin panel is added later, this data will
move into PostgreSQL.

Text marked DRAFT was written for the website and still needs the
business owner's approval. Everything else is taken from the company's
own flyers, posters and pack labels.
"""

COMPANY = {
    "name": "Harvests Gateway Ltd.",
    "short_name": "Harvests",
    "descriptor": "A Snacks Products Company",
    "tagline": "Quality Ghana Snacks, Better Lives",
    "slogan": "Where Quality Meets Passion",
    "safety_tagline": "Safe Today, Healthy Lives Tomorrow",
    "phone": "059 288 5501",
    "phone_link": "+233592885501",
    "email": "harvestsgateway@gmail.com",
    # WhatsApp number for orders, digits only in international format
    "whatsapp": "+233592885501",
    "whatsapp_display": "+233 59 479 1756",
}

# Source: "Welcome to Harvests Gateway Ltd" poster
WELCOME = (
    "We believe every great product begins with great people, great values, "
    "and a commitment to excellence."
)

# DRAFT: About Us introduction
ABOUT_INTRO = [
    "Harvests Gateway Ltd. is a Ghanaian snacks products company. We take "
    "produce from local farms, such as plantain, sweet potato, maize and "
    "peanuts, and turn it into crunchy, freshly made snacks for homes, "
    "offices, schools and celebrations.",
    "Every pack is made with care, from the very first ingredient to the "
    "final package, under strict food safety and hygiene standards. Our "
    "goal is simple: snacks you can trust, at prices that make sense, made "
    "by people who take pride in their work.",
]

# Source: Vision / Mission / Purpose poster
VISION = (
    "To become a leading and trusted African snack brand known for quality, "
    "innovation, and delicious products that enrich everyday lives."
)
MISSION = (
    "To produce safe, high-quality, and affordable snacks using locally "
    "sourced ingredients, modern production methods, and a dedicated team "
    "while creating value for our customers, employees, and communities."
)
PURPOSE = (
    "To transform local agricultural produce into delicious, trusted, and "
    "accessible snacks while creating jobs, empowering communities, and "
    "delivering lasting value."
)

# Source: "Welcome" poster
PILLARS = [
    {"icon": "badge", "title": "Creating Quality Snacks",
     "text": "Carefully selected local ingredients, prepared fresh and packed to keep their crunch."},  # DRAFT text
    {"icon": "handshake", "title": "Service With Integrity",
     "text": "Honest products, honest dealings and a team that keeps its word to every customer."},  # DRAFT text
    {"icon": "people", "title": "Growing Together",
     "text": "We grow with our farmers, our staff and the communities that support us."},  # DRAFT text
]

# Source: "Every Hand Matters" poster
CULTURE = [
    {"icon": "target", "title": "Work With Purpose", "text": "Your efforts build our success."},
    {"icon": "team", "title": "Work As A Team", "text": "Together, we go further."},
    {"icon": "handshake", "title": "Work With Integrity", "text": "Do what is right, always."},
    {"icon": "star", "title": "Take Pride In What You Produce", "text": "Because quality matters."},
]

# Source: "Food Safety & Hygiene" poster
SAFETY = [
    {"icon": "shield", "title": "Food Security",
     "text": "We follow strict safety standards to keep our products safe for you."},
    {"icon": "wash", "title": "Hygiene",
     "text": "Clean hands, clean spaces, clean products."},
    {"icon": "team", "title": "Teamwork",
     "text": "A safer workplace creates a better product."},
    {"icon": "check", "title": "Quality Control",
     "text": "We check, we test, and we ensure the best."},
    {"icon": "care", "title": "Responsibility",
     "text": "We care for our people, our product, and our community."},
]

# Source: Organisational Structure poster
ORG = {
    "top": "Chief Executive Officer (C.E.O)",
    "second": "General Manager (G.M)",
    "units": [
        "H.R. & Admin. Manager",
        "Sales & Marketing Manager",
        "Accountant",
        "Chief Production Chef",
    ],
}


HERO_SLIDES = [
    "ripe-plantain-snacks",
    "popcorn-milky-chocolate",
    "coated-peanuts",
    "sweet-potato-snacks",
]

CATEGORIES = [
    {"slug": "plantain", "name": "Plantain"},
    {"slug": "potato", "name": "Sweet Potato"},
    {"slug": "popcorn", "name": "Popcorn"},
    {"slug": "peanuts", "name": "Peanuts"},
]

# Names, flavours and weights come from the pack labels.
# Descriptions are DRAFT.
PRODUCTS = [
    {
        "slug": "ripe-plantain-snacks",
        "name": "Ripe Plantain Snacks",
        "flavour": "Naturally sweet",
        "category": "plantain",
        "weight": "150g",
        "image": "ripe-plantain.jpg",
        "description": "Golden slices of ripe plantain, fried to a light crisp "
                       "with a natural sweetness in every bite.",
        "featured": True,
    },
    {
        "slug": "plantain-snacks",
        "name": "Plantain Snacks",
        "flavour": "Savoury crunch",
        "category": "plantain",
        "weight": "150g",
        "image": "plantain-green.jpg",
        "description": "Crunchy chips made from green plantain. Savoury, "
                       "satisfying and right for any time of day.",
        "featured": False,
    },
    {
        "slug": "sweet-potato-snacks",
        "name": "Sweet Potato Snacks",
        "flavour": "Lightly seasoned",
        "category": "potato",
        "weight": "150g",
        "image": "sweet-potato.jpg",
        "description": "Thin, crispy sweet potato chips, lightly seasoned for "
                       "a gentle sweet and savoury crunch.",
        "featured": True,
    },
    {
        "slug": "popcorn-white-cheddar",
        "name": "Crunchy Popcorn",
        "flavour": "Salted Classic White Cheddar",
        "category": "popcorn",
        "weight": "150g",
        "image": "popcorn-cheddar.jpg",
        "description": "Fluffy popcorn with a salted classic white cheddar "
                       "taste. A favourite for film nights and sharing.",
        "featured": True,
    },
    {
        "slug": "popcorn-creamy-milkway",
        "name": "Crunchy Popcorn",
        "flavour": "Creamy Milkway",
        "category": "popcorn",
        "weight": "150g",
        "image": "popcorn-milkway.jpg",
        "description": "Light, crunchy popcorn finished with a creamy Milkway "
                       "flavour for a sweet, milky treat.",
        "featured": False,
    },
    {
        "slug": "popcorn-milky-chocolate",
        "name": "Crunchy Popcorn",
        "flavour": "Milky Chocolate",
        "category": "popcorn",
        "weight": "150g",
        "image": "popcorn-chocolate.jpg",
        "description": "Crunchy popcorn coated in a rich milky chocolate "
                       "flavour. Sweet, indulgent and hard to put down.",
        "featured": False,
    },
    {
        "slug": "coated-peanuts",
        "name": "Crunchy Coated Peanuts",
        "flavour": "Spicy & NutKhat",
        "category": "peanuts",
        "weight": "150g",
        "image": "coated-peanuts.jpg",
        "description": "Crunchy coated peanuts with a spicy kick, made for "
                       "snacking, sharing and gatherings.",
        "featured": True,
    },
]


def product_label(product):
    """Full product name used in the WhatsApp order message."""
    if product["category"] in ("plantain", "potato"):
        return f'{product["name"]} ({product["weight"]})'
    return f'{product["name"]}, {product["flavour"]} ({product["weight"]})'
