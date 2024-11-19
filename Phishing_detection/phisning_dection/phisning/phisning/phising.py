from flask import Flask, render_template, request
import pickle

app = Flask(__name__)


with open("C:/Users/Asus/Downloads/Phishing_detection/phisning_dection/phisning/phisning/phishing.pkl", 'rb') as model_file:
    phishing_model = pickle.load(model_file)

def is_phishing(url):

    prediction = phishing_model.predict([url]) 
    return prediction[0]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        url = request.form['url']
        result = is_phishing(url)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
