from datetime import datetime
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from PH import PH

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/ph', methods=['GET', 'POST'])
def ph():
    if request.method == 'POST':
        value = request.json['ph']
        ph_to_add = PH(value=value)
        db.session.add(ph_to_add)
        db.session.commit()
        return jsonify({'message': 'PH value added successfully'})
    else:
        ph_values = PH.query.all()
        return jsonify(
            [{'id': ph_value.id, 'value': ph_value.value, 'datetime': ph_value.datetime} for ph_value in ph_values])


if __name__ == '__main__':
    app.run()
