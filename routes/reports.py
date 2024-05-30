# routes/reports.py
from flask import Blueprint, request, jsonify
from models import db, Report
from datetime import datetime

bp = Blueprint('reports', __name__, url_prefix='/api/reports')

@bp.route('/', methods=['POST'])
def generate_report():
    params = request.json
    # Process parameters and generate report (omitted for brevity)
    report = Report(name=params.get('name'), parameters=params, generated_at=datetime.utcnow())
    db.session.add(report)
    db.session.commit()
    return jsonify({'message': 'Report generated successfully'}), 201

@bp.route('/', methods=['GET'])
def get_reports():
    reports = Report.query.all()
    return jsonify([r.parameters for r in reports]), 200
