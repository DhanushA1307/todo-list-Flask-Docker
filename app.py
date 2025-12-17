from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ---------- Model ----------
class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# ---------- Routes ----------
@app.route("/items", methods=["POST"])
def create_todo():
    data = request.get_json(silent=True)

    # ✅ Validation
    if not data or "name" not in data:
        return jsonify({"error": "name field is required"}), 400

    # ✅ Correct object creation
    todo = Item(name=data["name"])

    db.session.add(todo)
    db.session.commit()

    return jsonify({
        "id": todo.id,
        "name": todo.name
    }), 201


@app.route("/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    return jsonify([
        {"id": t.id, "name": t.name}
        for t in items
    ])

# ---------- App Start ----------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()   # ✅ creates table if not exists

    app.run(host="0.0.0.0", port=5000, debug=True)