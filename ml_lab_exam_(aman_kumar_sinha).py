# -*- coding: utf-8 -*-
"""ML Lab Exam (Aman Kumar Sinha).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xFzpcTp55-biZh2i_5WPmt6PlNp_dPKN
"""

import kagglehub

# Downloading the latest version
path = kagglehub.dataset_download("milobele/sentiment140-dataset-1600000-tweets")

print("Path to dataset files:", path)

path

#Importing libraries

import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.cluster import KMeans
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

#Importing Dataset
data = pd.read_csv('/root/.cache/kagglehub/datasets/milobele/sentiment140-dataset-1600000-tweets/versions/1/testdata.manual.2009.06.14.csv')

data

data.head()

data.info()

data.columns = ['polarity', 'id', 'date', 'query', 'user', 'tweet']

# Selecting relevant columns
data = data[['polarity', 'tweet']]

# Mapping polarity to categories
data['polarity'] = data['polarity'].map({0: 'negative', 2: 'neutral', 4: 'positive'})

# Data cleaning
def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # Removing URLs
    text = re.sub(r'@\w+', '', text)    # Removing mentions
    text = re.sub(r'#', '', text)        # Removing hashtags symbol
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Removing special characters
    text = text.lower().strip()         # Converting to lowercase
    return text

data['cleaned_tweet'] = data['tweet'].apply(clean_text)

# Text preprocessing
import nltk

# Downloading the 'stopwords' dataset
nltk.download('stopwords')

# Text preprocessing
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Downloading the 'wordnet' dataset
nltk.download('wordnet') # Download the wordnet dataset

# Text preprocessing
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Downloading the 'punkt_tab' data package
nltk.download('punkt_tab')

def preprocess_text(text):
    words = word_tokenize(text)
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)

data['processed_tweet'] = data['cleaned_tweet'].apply(preprocess_text)

# Visualize=ing sentiment distribution
sns.countplot(x='polarity', data=data, palette='viridis')
plt.title('Sentiment Distribution')
plt.show()

# Generating WordCloud for each sentiment
for sentiment in ['negative', 'neutral', 'positive']:
    text = ' '.join(data[data['polarity'] == sentiment]['processed_tweet'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'WordCloud for {sentiment} Sentiment')
    plt.show()

# Train test split
X = data['processed_tweet']
y = data['polarity']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

# Feature extraction using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Defining models and parameters
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'SVM': SVC(),
    'Random Forest': RandomForestClassifier()
}

params = {
    'Logistic Regression': {'C': [0.1, 1, 10]},
    'SVM': {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']},
    'Random Forest': {'n_estimators': [50, 100, 200], 'max_depth': [None, 10, 20]}
}

# Performing GridSearchCV for each model
best_models = {}
for model_name in models:
    print(f"Tuning {model_name}...")
    grid = GridSearchCV(models[model_name], params[model_name], cv=3, scoring='f1_weighted', n_jobs=-1)
    grid.fit(X_train_tfidf, y_train)
    best_models[model_name] = grid.best_estimator_
    print(f"Best parameters for {model_name}: {grid.best_params_}")

# Evaluating each best model
for model_name, model in best_models.items():
    print(f"\nEvaluating {model_name}...")

    accuracy = accuracy_score(y_test, y_pred) # Calculating accuracy as well
    print(f"Accuracy: {accuracy:.4f}")
    y_pred = model.predict(X_test_tfidf)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

# Confusion Matrix for the best model
best_model = best_models['Logistic Regression']  # As Logistic Regression as the best
conf_matrix = confusion_matrix(y_test, best_model.predict(X_test_tfidf))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=best_model.classes_, yticklabels=best_model.classes_)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Topic Modeling with LDA
vectorizer_lda = CountVectorizer(max_features=1000, stop_words='english')
X_lda = vectorizer_lda.fit_transform(data['processed_tweet'])
lda = LatentDirichletAllocation(n_components=5, random_state=42)
lda.fit(X_lda)

# Displaying topics
for idx, topic in enumerate(lda.components_):
    print(f"Topic {idx+1}: ", [vectorizer_lda.get_feature_names_out()[i] for i in topic.argsort()[-10:]])

# Clustering with K Means
kmeans = KMeans(n_clusters= 5, random_state=100)
kmeans_labels = kmeans.fit_predict(X_train_tfidf)

# Visualizing clustering results
sns.scatterplot(x=X_train_tfidf.toarray()[:, 0], y=X_train_tfidf.toarray()[:, 1], hue=kmeans_labels, palette='viridis')
plt.title('KMeans Clustering')
plt.show()

from sklearn.cluster import KMeans

# Assuming X_train_tfidf is our TF-IDF matrix
num_clusters = 5
kmeans = KMeans(n_clusters=num_clusters, random_state=100)
cluster_labels = kmeans.fit_predict(X_train_tfidf)

# Creating a new DataFrame for the training data with cluster labels
clustered_data = pd.DataFrame({'processed_tweet': X_train, 'cluster_kmeans': cluster_labels})

data = pd.merge(data, clustered_data[['processed_tweet', 'cluster_kmeans']], on='processed_tweet', how='left', suffixes=('', '_y'))

# Exploring the clusters
for i in range(num_clusters):
    print(f"Cluster {i}:")
    # Accessing cluster column
    cluster_tweets = data[data['cluster_kmeans'] == i]['processed_tweet']
    print(cluster_tweets.sample(5))  # Print 5 sample tweets from the cluster

"""###Our analysis revealed that Logistic Regression performed slightly better than SVM and Random Forest with a balanced F1-score across sentiment classes. Clustering and topic modeling provided additional insights into sentiment distribution and dominant themes. Overall, the approach effectively demonstrated sentiment analysis techniques, though fine-tuning and dimensionality reduction could improve clustering visualization."""

