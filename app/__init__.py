from flask import Flask

def creation_app():
    app = Flask(__name__)
    from .views import views


    app.register_blueprint(views, url_prefix='/')


    return app