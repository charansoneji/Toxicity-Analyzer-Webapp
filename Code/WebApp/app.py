from flask import Flask, request
from flask import render_template
from flask import current_app as app
from predict import prediction

app = Flask(__name__)


# @app.route('/')
# def print_my_pred():
#    return prediction("Hey you!")

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def predictmytoxicity():
    giveninput = request.form["querytext"]
    output = prediction(giveninput)
    toxic=round(output['Toxic'])
    severetoxic=round(output['Severely Toxic'])
    obscene=round(output['Obscene'])
    threat=round(output['Threat'])
    insult=round(output['Insult'])
    identityhate=round(output['Identity Hate'])
    return render_template('result.html', toxic=toxic,severe=severetoxic, obscene=obscene, threat=threat, insult=insult,
                           identity=identityhate)


if __name__ == '__main__':
    app.run(debug=True)
