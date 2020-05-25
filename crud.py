

from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import json

from src.main.model.brand import Brand
from src.main.model.colour import Colour
from src.main.model.ruler import Ruler

with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class OfficeRuler(Ruler, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producer = db.Column(db.String(45), unique=False)
    price_in_uah = db.Column(db.Float, unique=False)
    brand = db.Column(db.String(45), unique=False)
    colour = db.Column(db.String(45), unique=False)
    warranty_in_days = db.Column(db.Integer, unique=False)
    weight_in_grams = db.Column(db.Integer, unique=False)
    length_in_cm = db.Column(db.Integer, unique=False)

    def __init__(self, producer='def_producer', price_in_uah=0, brand=Brand(4),
                 colour=Colour(1), warranty_in_days=0, weight_in_grams=0, length_in_cm=0):
        super().__init__(producer, price_in_uah, brand, colour, warranty_in_days, weight_in_grams)
        self.length_in_cm = length_in_cm


class OfficeRulerSchema(ma.Schema):
    class Meta:
        fields = ('producer', 'price_in_uah', 'brand', 'colour', 'warranty_in_days', 'weight_in_grams', 'length_in_cm')


office_ruler_schema = OfficeRulerSchema()
office_ruler_schemas = OfficeRulerSchema(many=True)


@app.route("/ruler", methods=["POST"])
def create_tool():
    producer = request.json['producer']
    price_in_uah = request.json['price_in_uah']
    brand = request.json['brand']
    colour = request.json['colour']
    warranty_in_days = request.json['warranty_in_days']
    weight_in_grams = request.json['weight_in_grams']
    length_in_cm = request.json['length_in_cm']
    office_ruler_constructor = OfficeRuler(producer, price_in_uah, brand, colour, warranty_in_days, weight_in_grams,
                                           length_in_cm)
    db.session.add(office_ruler_constructor)
    db.session.commit()
    return office_ruler_schema.jsonify(office_ruler_constructor)


@app.route("/ruler", methods=["GET"])
def get_tool():
    all_office_ruler_tool = OfficeRuler.query.all()
    result = office_ruler_schemas.dump(all_office_ruler_tool)
    return jsonify({'office_ruler_constructor': result})


@app.route("/ruler/<id>", methods=["GET"])
def get_tool_id(id):
    office_ruler_tool = OfficeRuler.query.get(id)
    if not office_ruler_tool:
        abort(404)
    return office_ruler_schema.jsonify(office_ruler_tool)


@app.route("/ruler/<id>", methods=["PUT"])
def tool_update(id):
    office_ruler_tool = OfficeRuler.query.get(id)
    if not office_ruler_tool:
        abort(404)
    office_ruler_tool.producer = request.json['producer']
    office_ruler_tool.price_in_uah = request.json['price_in_uah']
    office_ruler_tool.brand = request.json['brand']
    office_ruler_tool.colour = request.json['colour']
    office_ruler_tool.warranty_in_days = request.json['warranty_in_days']
    office_ruler_tool.weight_in_grams = request.json['weight_in_grams']
    office_ruler_tool.length_in_cm = request.json['length_in_cm']
    db.session.commit()
    return office_ruler_schema.jsonify(office_ruler_tool)


@app.route("/ruler/<id>", methods=["DELETE"])
def tool_delete(id):
    office_ruler_tool = db.session.query(OfficeRuler).get(id)
    if not office_ruler_tool:
        abort(404)
    db.session.delete(office_ruler_tool)
    db.session.commit()
    return office_ruler_schema.jsonify(office_ruler_tool)


if __name__ == '__main__':
    db = SQLAlchemy(app)
    db.create_all()
    app.run(debug=True, host='127.0.0.1')
