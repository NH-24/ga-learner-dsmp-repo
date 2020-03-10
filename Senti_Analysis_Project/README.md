### Project Overview

 Amazon Company want  to focus on customer reviews on there alexa product. So my aim is to classify the unhappy customer based on the features 'rating', 'date', 'variation', 'verified_reviews', 'feedback'. So let's work on the customer reviews.




### Learnings from the project

 After completing this project, I have the better understanding of how to solve sentiment analysis . In this project, I have apply the following concepts.

Train-test split
posterstemmer
Text cleaning
Random forest classifier
Metrics for classification


### Approach taken to solve the problem

 The first step - you know the drill by now - load the dataset and see how it looks like.

Load data and convert timestamp
Rating vs feedback and Product rating vs feedback
Data cleaning
Spliting the dataset
Predictor check - checking the negative feedback so check the accuracy matrix as precision
Predictor check after using SMOTE-As the dataset in imbalanced data where 91% is positive feedback and 9% is negative feedbak. So if are focusing on negative feedback, if we are applying the model it will always gives us positive feedback. So we apply the oversampling technic SMOTE and check the accuracy of the model.



### Challenges faced

 We first did some initial data analysis to understand about various variables present in the dataset.It was seen that the average score for the reviews was 4.46. The number of reviews by weekday and average rating was plotted to understand if there was any significant difference in the reviews by the day .

Models were created to predict the sentiment of the review given the review statement . Text cleaning steps like removing punctuation , stemming and creating the counter matrix. The dataset was split into train and test by 80-20 ratio . Given the highly imbalanced dataset , the AUC was around 0.9 for both Naive Bayes and Logit models.

SMOTE techniques were applied and the model was rebuilt which improved the AUC scores to 0.9 for both the models.


### Additional pointers

 we could further perform more sentiment analysis


