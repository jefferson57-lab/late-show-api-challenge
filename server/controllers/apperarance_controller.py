from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.extensions import db


class AppearancesResource(Resource):

    @jwt_required()
    def post(self):
        json_data = request.get_json()

        
        missing_fields = self._validate_required_fields(json_data)
        if missing_fields:
            return make_response(
                {"error": f"Missing fields: {', '.join(missing_fields)}"}, 400
            )

        try:
            
            appearance = Appearance(
                rating=json_data["rating"],
                guest_id=json_data["guest_id"],
                episode_id=json_data["episode_id"]
            )
            db.session.add(appearance)
            db.session.commit()

            return make_response(jsonify({
                "id": appearance.id,
                "rating": appearance.rating,
                "guest_id": appearance.guest_id,
                "episode_id": appearance.episode_id
            }), 201)

        except Exception as error:
            return make_response({"error": str(error)}, 500)

    def _validate_required_fields(self, data):
        """Helper method to find missing required fields."""
        required = ["rating", "guest_id", "episode_id"]
        return [field for field in required if not data.get(field)]
