from modules.hello_world import test_bp


def route(app):
    app.register_blueprint(test_bp)