from flask import Blueprint, render_template

from . import content

bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    featured = [p for p in content.PRODUCTS if p["featured"]]
    by_slug = {p["slug"]: p for p in content.PRODUCTS}
    hero_slides = [by_slug[s] for s in content.HERO_SLIDES if s in by_slug]
    return render_template(
        "index.html",
        title="Home",
        featured=featured,
        hero_slides=hero_slides,
        pillars=content.PILLARS,
        welcome=content.WELCOME,
        mission=content.MISSION,
        product_count=len(content.PRODUCTS),
    )


@bp.route("/products")
def products():
    return render_template("products.html", title="Our Snacks", products=content.PRODUCTS)


@bp.route("/about")
def about():
    return render_template(
        "about.html",
        title="About Us",
        intro=content.ABOUT_INTRO,
        welcome=content.WELCOME,
        vision=content.VISION,
        mission=content.MISSION,
        purpose=content.PURPOSE,
        pillars=content.PILLARS,
        culture=content.CULTURE,
        org=content.ORG,
    )


@bp.route("/quality")
def quality():
    return render_template("quality.html", title="Food Safety & Quality", safety=content.SAFETY)


@bp.route("/contact")
def contact():
    return render_template(
        "contact.html",
        title="Contact & Order",
        products=content.PRODUCTS,
        label=content.product_label,
        5
    )
