# --------------
# import packages
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

# Load the dataset
df=pd.read_csv(path,sep="\t")

# Converting date attribute from string to datetime.date datatype 
from datetime import datetime, timedelta, date
type(df['date'][0]) , df['date'][0]
df['date'] = pd.to_datetime(df['date'])
df['date'][0]
#verified_reviews =
reviews = df['verified_reviews']
len_review = []
for review in reviews:
    len_review.append(len(review))

df['len_of_reviews'] = len_review
df['len_of_reviews'][0], df['verified_reviews'][0]

# calculate the total length of word




# --------------
## Rating vs feedback

# set figure size


# generate countplot
plt.figure(figsize=(15,7))
sns.countplot(x="rating", hue="feedback", data=df)
plt.show()


# display plot


## Product rating vs feedback

# set figure size


# generate barplot
plt.figure(figsize=(15,7))
sns.barplot(x="rating", y="variation", hue="feedback", data=df, estimator= sum, ci = None)
plt.show()

# display plot




# --------------
# import packages
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# declare empty list 'corpus'
corpus =[]
for i in range(0, 3150):
    review = re.sub('[^a-zA-Z]', ' ', df['verified_reviews'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
 

# for loop to fill in corpus

    # retain alphabets
    
    # convert to lower case
    
    # tokenize
    
    # initialize stemmer object
    
    # perform stemming
    
    # join elements of list
    
    # add to 'corpus'
    
    
# display 'corpus'



# --------------
# import libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# Instantiate count vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

cv = CountVectorizer(max_features = 1500)

X = cv.fit_transform(corpus).toarray()
y = df['feedback']
count = df['feedback'].value_counts() 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Independent variable


# dependent variable


# Counts


# Split the dataset



# --------------
# import packages
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, f1_score

# Instantiate calssifier
rf= RandomForestClassifier(random_state=2)

# fit model on training data
rf.fit(X_train,y_train)

# predict on test data
y_pred =rf.predict(X_test)
score =accuracy_score(y_test, y_pred)
precision=precision_score(y_test,y_pred)

# calculate the accuracy score


# calculate the precision


# display 'score' and 'precision'



# --------------
# import packages
from imblearn.over_sampling import SMOTE

# Instantiate smote
smote = SMOTE(random_state = 9)

# fit_sample onm training data
X_train,y_train =smote.fit_sample(X_train,y_train)

# fit modelk on training data
rf = RandomForestClassifier(random_state=2)
rf.fit(X_train,y_train)
# predict on test data
y_pred = rf.predict(X_test)

# calculate the accuracy score
score =accuracy_score(y_test, y_pred)
precision=precision_score(y_test,y_pred)


# calculate the precision


# display precision and score



