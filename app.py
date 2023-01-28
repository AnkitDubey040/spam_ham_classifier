from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import os,sys
app = Flask(__name__)
from spam_ham.logger import logging

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	logging.info(f"Reading Data from the Csv file")
	df = pd.read_csv("spam.csv", encoding="latin-1")
	logging.info(f"Cleaning the data")
	df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
	logging.info(f"Fetching Collection as Dataframe")

	# df = get_collection_as_dataframe(database_name=DATABASE_NAME, collection_name=COLLECTION_NAME)
	# Features and Labels
	logging.info(f"Labeling spam as 1 and ham as 0")
	df['label'] = df['type'].map({'ham': 0, 'spam': 1})
	logging.info(f"Specifiying Target and Feature columns")
	X = df['text']
	y = df['label']

	# Extract Feature With CountVectorizer
	# Extract Feature With CountVectorizer :cleaning involved converting all of our data to lower case and removing all punctuation marks.
	logging.info(f"Initializing CountVectorizer")
	cv = CountVectorizer()
	X = cv.fit_transform(X)  # Fit the Data
	from sklearn.model_selection import train_test_split
	logging.info(f"Train Test Split on data")
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
	# Naive Bayes Classifier
	logging.info(f"Training the Multinomial Naive Bayes model")
	from sklearn.naive_bayes import MultinomialNB
	# particular classifier is suitable for classification with discrete features ( word counts for text classification). It takes in integer word counts as its input.
	clf = MultinomialNB()  # NAIVE BAYES
	clf.fit(X_train, y_train)
	clf.score(X_test, y_test)
	logging.info(f"The score of the model is : 'clf.score(X_test,y_test)' ")
	logging.info(f"Predicting the result")

	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		vect = cv.transform(data).toarray()
		my_prediction = clf.predict(vect)
	return render_template('result.html', prediction=my_prediction)
	
if __name__ == '__main__':
	app.run(debug=True)
