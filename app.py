
from flask import Flask, request, render_template
import pickle

# Charger le pipeline enregistré
with open('model/pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        text = request.form['text']  # Récupérer le texte du formulaire
        prediction = pipeline.predict([text])[0]  # Utiliser le pipeline pour prédire
    return render_template('predict.html', prediction=prediction)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
