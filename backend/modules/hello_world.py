from flask import Blueprint

test_bp = Blueprint('test_blueprint', __name__)


@test_bp.route('/')
def test_blueprint():
    return {
        "name": "name",
        "message": "message"
    }
