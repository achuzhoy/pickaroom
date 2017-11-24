from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import random1
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        name=request.form['name']
 
        if form.validate():
            # Save the comment here.
            output=random1.main(name)
            flash(output)
        else:
            flash('Error: All the form fields are required.')
 
    return render_template('roomlottery.html', form=form)
 
@app.route("/flush", methods=['GET', 'POST'])
def helloa():
    form = ReusableForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        passwd=request.form['name']
 
        if form.validate():
            # Save the comment here.
            output=random1.flushdb(passwd)
            flash(output)
        else:
            flash('Error: All the form fields are required.')
 
    return render_template('flush.html', form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)
