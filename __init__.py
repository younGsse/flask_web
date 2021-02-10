from flask import Flask

def create_app():
    app = Flask(__name__)

    # @app.route('/')
    # def hello_pybo():
    #     return 'Hello, Pybo!'

    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app