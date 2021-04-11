from flask import Flask, render_template
from app.routes import bp as static_content_bp


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(
        __name__,
        template_folder='templates',
        instance_relative_config=True
    )
    app.debug = True
    app.register_blueprint(static_content_bp, url_prefix='/')

    @app.route('/hello', methods=['GET'])
    def hello():
        return 'Hello World!', 200

    @app.route('/')
    def home():
        return render_template('base_layout.html', message="Hello World!")

    return app
