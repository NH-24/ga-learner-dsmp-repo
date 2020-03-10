### Project Overview

 You are given references to news pages collected from an web aggregator in the period from 10-March-2014 to 10-August-2014. The resources are grouped into categories that represent pages discussing the same story. News categories included in this dataset include business(b); science and technology(t); entertainment(e); and health(h).


### Learnings from the project

 Solving it will reinforce the following concepts of text analytics:

Preprocess text data with tokenization, stopword removal etc
Vectorize data using Bag-of-words and TF-IDF approaches
Apply classifiers (Logistic and Multinomial Naive Bayes) to perform multi-class classification


### Approach taken to solve the problem

 1.Preprocess text data by doing the following steps on the NewsML column
  - retain only alphabets
  - Convert the data to lowercase and tokezize
  - Remove stop words by using list comprehension
  - join list elements
Finally split into train and test using train_test_split function where feature is X, target is y,test size is 20% and random state is 3. Save the resultant variables as X_train, X_test, y_train and y_test
2.Vectorize with Bag-of-words and TF-IDF approach:
After cleaning data its time to vectorize data so that it can be fed into an ML algorithm. You will be doing it with two approaches: Bag-of-words and TF-IDF.
3.Predicting with Multinomial Naive Bayes: Multinomial Naive Bayes is an algorithm that can be used for the purpose of multi-class classification. You will be using it to train and test it on both the versions i.e. Bag-of-words and TF-IDF ones and then checking the accuracy on both of them.
4.Predicting with Logistic Regression Logistic Regression can be used for binary classification but when combined with OneVsRest classifer, it can perform multiclass classification as well. You will be using one such algorithm to train and test it on both the versions i.e. Bag-of-words and TF-IDF ones and then checking the accuracy on both of them







### Challenges faced

 We achieved 95% accuracy with tfidf vectorizer and 92% with count vectorizer by using MultinomialNB algorithm. Lets see if we can increase the accuracy by using Logistic Regression on both vectorizer.After applying Logistic Regression we can see that for Count Vectorizer the accuracy is increased i.e 96% and for tfidf vectorizer the accuracy is same.


### Additional pointers

 We learn NLP functionality through New Articles.The goal is to predict which class a particular resource belongs to given the title of the resource.



