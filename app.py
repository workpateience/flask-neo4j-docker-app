from flask import Flask
from neomodel import config
from flask import render_template
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
    print("Home route accessed")
    return render_template("index.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
