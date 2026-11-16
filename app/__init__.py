import os
from datetime import date
from urllib.parse import quote

from flask import Flask, render_template, url_for

from . import content


def whatsapp_link(message=None):
    """Build a wa.me link to the business number, with an optional pre-filled message."""
    url = f"https://wa.me/{content.COMPANY['whatsapp']}"
    if message:
        url += "?text=" + quote(message)
    return url


def order_link(product):
    label = content.product_label(product)
    message = (
        f"Hello Harvests Gateway, I would like to order *{label}*. "
        "Please let me know the availability and delivery details. Thank you."
    )
    return whatsapp_link(message)


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    def asset(filename):
        """Static file URL with a version number, so browsers fetch the new file after every edit."""
        try:
            version = int(os.path.getmtime(os.path.join(app.static_folder, filename)))
        except OSError:
            version = 0
        return url_for("static", filename=filename, v=version)

    app.jinja_env.globals.update(whatsapp_link=whatsapp_link, order_link=order_link, asset=asset)

    @app.context_processor
    def inject_globals():
        return {
            "company": content.COMPANY,
            "categories": content.CATEGORIES,
            "year": date.today().year,
        }

    from .routes import bp
    app.register_blueprint(bp)

    @app.errorhandler(404)
    def not_found(_e):
        return render_template("404.html", title="Page not found"), 404

    return app
