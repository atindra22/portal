from flask import Flask


def create_app():
    app = Flask(__name__,
                template_folder=
                'Employee management  portal\website\templates\home.html')
    app.config['SECRET KEY'] = '1234'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
