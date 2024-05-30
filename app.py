# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from routes import excel_data, reports, analysis_charts

app.register_blueprint(excel_data.bp)
app.register_blueprint(reports.bp)
app.register_blueprint(analysis_charts.bp)

if __name__ == '__main__':
    app.run(debug=True)
