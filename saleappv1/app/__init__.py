from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = '@(fhfbgf4h5g8hgfbj*jfhbv(rug45g4hgb)SGSFB^HGJHG57)'
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
