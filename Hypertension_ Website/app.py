from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import InputRequired
import numpy as np

app = Flask(__name__,template_folder='template')
app.config['SECRET_KEY'] = 'secret_key'

class HypertensionForm(FlaskForm):
    age = FloatField('Age', validators=[InputRequired()])
    systolic_bp = FloatField('Systolic Blood Pressure', validators=[InputRequired()])
    diastolic_bp = FloatField('Diastolic Blood Pressure', validators=[InputRequired()])
    submit = SubmitField('Detect Hypertension')

def simulate_hypertension_detection(age, systolic_bp, diastolic_bp):
    
    if systolic_bp > 140 or diastolic_bp > 90:
        return "High"
    else:
        return "Normal"

@app.route('/', methods=['GET', 'POST'])
def index():
    form = HypertensionForm()
    result = None

    if form.validate_on_submit():
        age = form.age.data
        systolic_bp = form.systolic_bp.data
        diastolic_bp = form.diastolic_bp.data
        result = simulate_hypertension_detection(age, systolic_bp, diastolic_bp)

    return render_template('index.html', form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)