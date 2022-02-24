# Student Success Analysis

## Topic
We have decided to investigate what factors contribute the greatest student success in K-12 education.  With more education choices than ever before with remote learning, home schooling, hybrid solutions, public schools, private schools, etc., will different combinations of factors yield greater academic success than others and how might those factors change with different educational paths.  Are we able to predict the success of a student based on different factors?

## Data Source
Our data source comes from the National Center for Education Statistics, which bears the responsibility of the collection, analysis and reporting of data pertaining to education within the United States.  We are using a csv that compiles the results of the 2019 National Household Education Surveys Program.  We have elected to focus on the Parent and Family Involvement in Education (PFI) survey.  The survey contains data completed with parents or guardians of 16,446 children age 20 or younger who were enrolled in grades K through 12.

## Questions 
We hope to answer the following questions:
  - What combination of factors yield the greatest student success?
  - How do those factors differ for success with different education paths, such as remote learning?
  - Are there paths that better prepare future success in post-secondary education?

## Dream Team Protocols
We have named our project group the Dream Team.  We hae settled on a quick daily checkin at 6:00 via Slack.  Future meetings may be scheduled as needed depending on challenges presented throughout the project.  

## Data Management
The cleaned and processed data will be housed in an Postgres database hosted by Heroku. This includes the train and test data, survey responses and feature importance. Below is a link to the ERD:

[Database_ERD](./Resources/Database_ERD.sql)

The data will then be pulled in for use in the dashboard.

## Front End
The front end is a Flask site using Bootstrap hosted by Heroku. People can submit answers to a selection of questions picked from the National Household Education Surveys Program. These answers can then be used to train and/or test the model moving forward. The immediate use of the answers will be to provide recommendations on what parents can do to improve their childs success. The results will be displayed on the dashboard. The front end can be accessed here:

https://student-success-analysis.herokuapp.com/

## Machine Learning Model

 - We began our preliminary data preprocessing by eliminating columns from the original csv that did not pertain to our questions.  This left us with 16,446 rows of data.  From there, we removed rows with a -1 or -9 as a value, which represented variables that were not applicable or were missing.  This left us with 8,353 rows across 56 columns.  We then ran a value count for each column and decided to eliminate school types to help minimize noise since 8,314 rows were public schools.  We then binned the following columns:
   - Grades:  We combined grades into passing and failing categories.  
   - Parent Ages:  Due to the vast range in ages, we binned them into 5 ranges.
   - Homework Hours:  Due to the vast range, we binned them into 4 ranges
   - Number of Family Dinners Weekly:  These were binned into 4 ranges
   - Total Household Income:  These were consolidated from 12 categories to 4 categories.
 
 Then we wrote the resulting dataframe to our Postgres database hosted by Heroku.

 - To determine feature selection, we first connected to the database and pulled the table into a dataframe for review.  A correlation matrix was generated for review.  We selected SEGRADES as our target and left the other 49 columns as our features. 

 - The data was split into training and testing datasets using the default split of .75 for training and .25 for testing.  While we did experiment with different splits, the results weren't significantly different so we decided that utilizing the defaults was sufficient.  The datasets were stratified.  

 - Since all of our data was classification data, we began by using the Random Forest Classifier and the Extremely Random Forest Classifier.  However, we discovered that these models were overfitting the training data unless we limited nearly all of our categories.  So, we then turned to AdaBoost Classifier since it known for working well with binary classification.  AdaBoost would continue to correct errors of the preceding model to help improve our accuracy.  We then reviewed the feature importance and were able to eliminate some of the less important features.  We then run the remaining features through the AdaBoost classifier again and improved our accuracy. We benefited from the continual learning to help improve the model.  A limitation is that the dataset has to really have minimal noise.  We originally used pd.dummies to encode the data but then switched to OneHotEncoder so that we could employ the parameter of dropping the 1st category if it were binary (Yes or No) but retain all the columns if it was just a classification.

 - The current accuracy score is 70%.

## Dashboard
The dashboard is displayed upon completion of the student survey.  It is a Flask site using Bootstrap hosted by Heroku.  Using D3 a radar chart will be generated with the respondent's results overlaying the optimal results from the ML model.  In addition, resources will be dynamically presented in the categories that may enhance the respondent's results in the future.