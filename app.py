from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

#Load the ML model
model = pickle.load(open('./models/phishing.pkl', 'rb'))

@app.route('/')
def hello_world():
    return render_template('index.html')

    
@app.route('/predict', methods=['POST'])
def predict():
    url = request.form.get('urlInput')
    
    prediction = model.predict([url])
    return render_template('index.html', prediction_text='This is {}'.format(prediction))


if __name__ == '__main__':
    app.run(debug=True)