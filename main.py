import gtts.lang
from gtts import gTTS
import PyPDF2
from flask import Flask, render_template, send_file
from flask_wtf import FlaskForm
from wtforms import FileField, SelectField, SubmitField
from wtforms.validators import DataRequired, regexp
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "skhfie39u5%ksakfj()375khdf"


def pdf_to_text(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
        return text


class RequestForm(FlaskForm):
    lang_dict = gtts.lang.tts_langs()
    choices = [(key, value) for (key, value) in lang_dict.items()]
    pdf = FileField(label="Choose your PDF:", validators=[DataRequired()])
    lang = SelectField(label="Language: ", choices=choices,
                       validators=[DataRequired()])
    submit = SubmitField(label="Submit")


@app.route("/", methods=["GET", "POST"])
def home():
    form = RequestForm()
    if form.validate_on_submit():
        pdf_name = form.data.get("pdf").filename
        # save uploaded pdf to current working folder
        form.data.get("pdf").save(pdf_name)
        text = pdf_to_text(pdf_name)
        tts = gTTS(text=text, lang=form.data.get("lang"))
        filename = f"{pdf_name.split('.')[0]}.mp3"
        tts.save(f"{filename}")
        return send_file(filename, as_attachment=True)
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
