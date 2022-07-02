from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

# Globally accessible libraries
db = SQLAlchemy()

def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    # app.config.from_object('config.Config')

    db.init_app(app)
    CORS(app)

    with app.app_context():
        # Import parts of our application
        from .budgets import routes
        from .categories import routes
        from .envelopes import routes
        from .transactions import routes
        db.create_all()
        
        # Register Blueprints
        app.register_blueprint(budgets.budgets_bp)
        app.register_blueprint(categories.categories_bp)
        app.register_blueprint(envelopes.envelopes_bp)
        app.register_blueprint(transactions.transactions_bp)

        return app