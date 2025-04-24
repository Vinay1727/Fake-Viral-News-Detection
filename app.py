from flask import Flask, request, render_template
from markupsafe import escape
import pickle
import joblib
# from sklearn.feature_extraction.text import TfidfVectorizer
  
vector = joblib.load(open("tfidf_vectorizer.pkl", 'rb'))
model = joblib.load(open("fake_news_model.pkl", 'rb'))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        news = request.form.get('news', '').strip()
        if not news:
            return render_template("prediction.html", prediction_text="Please enter a news headline for prediction.")
        try:
            predict = model.predict(vector.transform([news]))
            prediction_label = predict[0]
            return render_template("prediction.html", prediction_text=f"News headline is predicted as -> {prediction_label}")
        except Exception as e:
            return render_template("prediction.html", prediction_text=f"Error during prediction: {str(e)}")
    else:
        return render_template("prediction.html")

if __name__ == "__main__":
    app.run()
