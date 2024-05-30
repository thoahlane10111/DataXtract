# routes/excel_data.py
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os
import pandas as pd
from models import db, ExcelData

bp = Blueprint('excel_data', __name__, url_prefix='/api/excel_data')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@bp.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        df = pd.read_excel(file_path)
        data = df.to_dict(orient='records')
        
        excel_data = ExcelData(data=data)
        db.session.add(excel_data)
        db.session.commit()
        
        return jsonify({'message': 'File successfully uploaded and data extracted'}), 201

@bp.route('/', methods=['GET'])
def get_data():
    data = ExcelData.query.all()
    return jsonify([d.data for d in data]), 200
