"""Initialize app."""
from flask import Flask
from flask_apscheduler import APScheduler


def create_app():
    """Construct the core application."""
    app = Flask(__name__,
                instance_relative_config=False)
    app.config.from_object('config.Config')

    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
   
    with app.app_context():

        # Import main Blueprint
        from application import routes
        app.register_blueprint(routes.main_bp)

        # Import Dash application
        from application.dash_application.dash_coronavirus import Add_Dash
        app = Add_Dash(app)

        # Compile assets
        from application.assets import compile_assets
        compile_assets(app)

        return app
