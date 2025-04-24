# Fake-News-Detection

Project Title: Fake News Detection

Description:
The Fake News Classification system is a smart web-based solution designed to differentiate between genuine and misleading news articles. By leveraging machine learning, the system empowers users to verify the credibility of online news, helping to counteract the rising spread of digital misinformation and support trustworthy journalism.

Technologies Used:
1.Flask: A lightweight web framework in Python used to build the backend of the application and manage server-side logic and HTTP routing.

2.Jupyter Notebook: A tool for interactive development, utilized during the stages of data analysis, preprocessing, and model creation.

3.Passive Aggressive Classifier: An efficient online learning algorithm tailored for binary classification, ideal for distinguishing between real and fake news.

4.TfidfVectorizer: Converts raw text into numerical format using Term Frequency-Inverse Document Frequency, enabling the model to process textual inputs.

5.HTML/CSS: Used for constructing and styling the front-end interface, ensuring a clean and responsive user experience.

Functionality:
Landing Page: The home screen offers a sleek interface where users can paste or input headlines or news content for verification.

News Classification: Upon submission, the system analyzes the content using a trained Passive Aggressive model to determine if it’s authentic or fabricated.

Output Display: The result page delivers clear feedback to the user, specifying whether the news is identified as “REAL” or “FAKE”.

Model Refresh (Optional): An optional feature that allows for periodic retraining or updating of the model to reflect newly emerging patterns in fake news.

Process Flow:
Dataset Sourcing: The training data comprises a collection of news entries labeled as real or fake, sourced from reliable repositories.

Text Preprocessing: The raw news content undergoes cleaning, which includes tokenization, removal of irrelevant words, and transformation into numerical vectors via TfidfVectorizer.

Model Training: The Passive Aggressive Classifier is trained in Jupyter Notebook using the preprocessed data to develop its ability to detect misinformation.

Integration & Deployment: Once trained, the model is serialized and incorporated into a Flask web app to handle real-time predictions.

User Interface: The Flask app is connected to an interactive front-end where users can input and receive feedback on news credibility.

Challenges Addressed:
Data Imbalance: One of the primary concerns was managing unequal class distribution (e.g., more real news than fake), which could bias the model's learning.

Text Data Handling: Efficiently converting textual data into a structured numerical format that is suitable for machine learning algorithms.

Model Efficiency: Maintaining high accuracy and generalizability to ensure reliable classification of both familiar and unseen news inputs.

Algorithm Utilized:
Passive Aggressive Classifier (Machine Learning)

Estimated Accuracy:
Approximately 95%