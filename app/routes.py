import re

from flask import Blueprint, current_app, redirect, render_template, request, url_for

from . import content
from .models import Visitor, db

bp = Blueprint("main", __name__)

PHONE_PATTERN = re.compile(r"^\+?[0-9\s\-()]+$")
EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
VISITOR_FIELDS = ("full_name", "phone", "email", "organisation")


def _check_visitor_form(form):
    errors = {}
    if not form["full_name"]:
        errors["full_name"] = "Please enter your name."
    elif len(form["full_name"]) > 120:
        errors["full_name"] = "Please keep your name under 120 characters."

    digits = re.sub(r"\D", "", form["phone"])
    if not form["phone"]:
        errors["phone"] = "Please enter your phone number."
    elif not PHONE_PATTERN.match(form["phone"]) or not 9 <= len(digits) <= 15:
        errors["phone"] = "Please enter a valid phone number, for example 024 123 4567."

    if form["email"] and (len(form["email"]) > 254 or not EMAIL_PATTERN.match(form["email"])):
        errors["email"] = "Please enter a valid email address, or leave it blank."

    if len(form["organisation"]) > 150:
        errors["organisation"] = "Please keep the organisation name under 150 characters."
    return errors


@bp.route("/welcome", methods=["GET", "POST"])
def welcome():
    cookie_name = current_app.config["VISITOR_COOKIE"]
    if request.method == "GET" and request.cookies.get(cookie_name):
        return redirect(url_for("main.home"))

    form = {field: request.form.get(field, "").strip() for field in VISITOR_FIELDS}
    errors = {}

    if request.method == "POST":
        errors = _check_visitor_form(form)
        if not errors:
            try:
                db.session.add(Visitor(
                    full_name=form["full_name"],
                    phone=form["phone"],
                    email=form["email"] or None,
                    organisation=form["organisation"] or None,
                ))
                db.session.commit()
            except Exception:
                # Do not lock customers out if the database is briefly unavailable
                db.session.rollback()
                current_app.logger.exception("Could not save visitor details")

            response = redirect(url_for("main.home"))
            response.set_cookie(
                cookie_name, "1",
                max_age=current_app.config["VISITOR_COOKIE_DAYS"] * 24 * 60 * 60,
                httponly=True, samesite="Lax", secure=request.is_secure,
            )
            return response

    return render_template("welcome.html", title="Welcome", form=form, errors=errors)


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
    )
