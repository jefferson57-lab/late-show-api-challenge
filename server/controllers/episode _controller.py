from flask_restful import Resource
from flask import request
from server.models.episode import Episode
from server.extensions import db


class Episodes(Resource):
    def get(self):
        episodes = Episode.query.all()
        return [eps.to_dict() for eps in episodes], 200


class EpisodeByID(Resource):
    def get(self, id):
        ep = Episode.query.get(id)
        if not ep:
            return {"error": "Episode not found"}, 404
        return ep.to_dict_with_appearances(), 200

    def delete(self, id):
        ep = Episode.query.get(id)
        if not ep:
            return {"error": "Episode not found"}, 404
        db.session.delete(ep)
        db.session.commit()
        return {}, 204