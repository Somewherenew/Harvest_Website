from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Visitor(db.Model):
    """Contact details a visitor enters on the welcome page."""

    __tablename__ = "visitors"

    id = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key=True)
    full_name = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text)
    organisation = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())