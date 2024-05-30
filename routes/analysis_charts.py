# routes/analysis_charts.py
from flask import Blueprint, request, jsonify
from models import db, Chart
from datetime import datetime

bp = Blueprint('analysis_charts', __name__, url_prefix='/api/analysis_charts')

@bp.route('/', methods=['POST'])
def generate_chart():
    params = request.json
    # Process parameters and generate chart (omitted for brevity)
    chart = Chart(name=params.get('name'), parameters=params, generated_at=datetime.utcnow())
    db.session.add(chart)
    db.session.commit()
    return jsonify({'message': 'Chart generated successfully'}), 201

@bp.route('/', methods=['GET'])
def get_charts():
    charts = Chart.query.all()
    return jsonify([c.parameters for c in charts]), 200

