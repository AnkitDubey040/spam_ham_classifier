# sms-spam-ham-detector 📱

A simple web app to detect SMS as spam or ham(not spam) using Python Flask and Naïve Bayes classifiers.SpamHam is a text-classification app which detects whether the message/email is spam or not. I've used Naive-Bayes along with NLP (TF-IDF, Bag of Words and more).
In order to perform an experiment I've combined two datasets (Enron email spam/ham and SMS spam classification) into one to gather more data.

<h4 align="center">In this project I build a model for classifying the SMS/Email into spam or ham through the text of the SMS/Email using standard classifiers.</h4>



![sms-spam-ham-detector](https://user-images.githubusercontent.com/25213850/88257771-3f98b580-ccde-11ea-9e03-c1b5323ab387.gif)



**Live at:** [Spam or Ham | SMS Detector](https://sms-spam-ham-detector.herokuapp.com)


## How It Does:
Extract the text and the target class from the dataset. Extract the features of the test using TF-IDF vectorizer for the Input features.Split the skewed data into shuffled sets using stratified shuffle split in sklearn library. Use standard classifiers to classify the data into spam or ham.
<p align="center">
  <br>
  <img src="https://github.com/ShubhamPy/Spam-Classifier/blob/master/Screenshots/modelLearning.png">
</p>

### Built With

1. `Flask`
2.`Python 3.7`
3. `Scikit-Learn`
4. `Numpy`
5. `Pandas
6. `Matplotlib`
7. `Seaborn`
4. `HTML5`
5.`CSS`
6.` Bootstrap-v4`
7. `Love`

### Installing/ Things you need to install the Web App and how to set up the project locally?

1. `Python3`
2. `Pip`
3. `Flask`
4. `Conda`

#### Steps
- Make a virtual environment using "conda create -n envname python=3.7 pip"
- source activate envname (for mac/linux) | activate envname (for windows)
- Download or clone this repo 
- pip install -r requirements.txt
- Run the app using python manage.py runserver

The files contain one message per line. Each line is composed by two columns:
- `Class`- contains the label (ham or spam) 
- `Message` - contains the raw text.

### Milestones for version 2
- Implement login and tailor experience for each user
- Collect the result reported by user for false classification of messages/email
- Model will self-learn from the reported data

Made by
**Ankit Dubey**  - [linkedin.com/AnkitDubey](https://www.linkedin.com/in/ankit-dubey-a6b522212/)
