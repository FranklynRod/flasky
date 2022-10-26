from flask import Blueprint, jsonify

class Dog:
    def __init__(self,id, name, color, personality):
        self.id = id
        self.name = name
        self.color = color
        self.personality = personality

dogs = [
    Dog(1, "Luna", "grey", "naughty"),
    Dog(2, "Orange Dog", "orange", "antagonistic"),
    Dog(3, "Big Ears", "grey and white", "sleepy"),
]

bp = Blueprint("dogs", __name__, url_prefix="/dogs")

@bp.route("", methods=["GET"])
def handle_dogs():
    results_list = []
    for dog in dogs:
        results_list.append(dict(
            id = dog.id,
            name = dog.name,
            color = dog.color,
            personality = dog.personality))
    return jsonify(results_list)