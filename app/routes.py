from flask import Blueprint, render_template, request, jsonify
from datetime import datetime
from app.models import User
from app import db

bp = Blueprint('main', __name__)

@bp.route("/")
def home_page():
    return render_template("index.html")

@bp.route("/reg")
def reg_page():
    users = User.query.all()
    return render_template("reg.html", users=users)

@bp.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    full_name = data.get("full_name")
    matric_no = data.get("matric_number")
    dept = data.get("department")
    level = data.get("level")
    role = data.get("role")

    user = User.query.filter_by(matric_number=matric_no).first()

    if not full_name or not matric_no or not dept or not level:
        return jsonify({"message": "Full Name, Matric Number, Department and Level are required"}), 400
    if user:
        if datetime.now().strftime("%Y-%m-%d") in user.dates:
            return jsonify({"message": "User attendance already marked"}), 400
        user.dates.append(datetime.now().strftime("%Y-%m-%d"))
        db.session.commit()
        return jsonify({"message": "User attendance marked"}), 200

    new_user = User(full_name=full_name, matric_number=matric_no, department=dept, level=level)
    if role:
        User.role = role
    db.session.add(new_user)
    db.session.commit()
    db.session.refresh(new_user)
    return jsonify({"message": "User Created and attendance marked"}), 201
