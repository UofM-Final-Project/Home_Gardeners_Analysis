from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
#init my Database manager
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):

    # Init the app
    app = Flask(__name__)
    #Link in the Config
    app.config.from_object(config_class)

    # Add static
    app.static_folder = 'static'
    #Register Plug-in

    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register Bootstrap
    bootstrap = Bootstrap(app)

    # Register views to blueprint
    from .views import bp as views_bp
    from .models import county_lookup_model,county_metrics_model,county_yearly_metrics_model,observation_model,station_model,station_yearly_model
    app.register_blueprint(views_bp)

    return app