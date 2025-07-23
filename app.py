from flask import Flask
from neomodel import config
from dotenv import load_dotenv
import os

load_dotenv()  # 🔄 Load from .env file

app = Flask(__name__)

# Set Neo4j connection from env
config.DATABASE_URL = os.getenv("DATABASE_URL")

# Import blueprints after config
from routes import queries_bp
app.register_blueprint(queries_bp)

@app.route("/")
def home():
    return "Flask + Neo4j app is running!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
