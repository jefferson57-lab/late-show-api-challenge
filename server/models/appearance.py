from server.extensions import db
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin


class Appearance(db.Model, SerializerMixin):
    __tablename__ = "appearances"
    serialize_rules = ('-episode.appearances', '-guest.appearances')

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey(
        "guests.id"), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey(
        "episodes.id"), nullable=False)

    def __repr__(self):
        return f"<Appearance Guest {self.guest_id} on Episode {self.episode_id} Rating: {self.rating}>"

    @validates('rating')
    def validate_rating(self, key, value):
        if not (1 <= value <= 5):
            raise ValueError("Rating must be between 1 and 5")
        return value