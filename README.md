# Student Success Analysis

## Topic
We have decided to investigage what factors contribute the greatest student success in K-12 education.  With more education choices than ever before with remote learning, home schooling, hybrid solutions, public schools, private schools, etc., will different combinations of factors yield greater academic success than others and how might those factors change with different educational paths.  Are we able to predict the success of a student based on different factors?

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

![Resources/Database_ERD.rtf]

The data will then be pulled in for use in the dashboard.

## Front End
The front end is a Flask site using Bootstrap hosted by Heroku. People can submit answers to a selection of questions picked from the National Household Education Surveys Program. These answers can then be used to train and/or test the model moving forward. The immediate use of the answers will be to provide recommendations on what parents can do to improve their childs success. The results will be displayed on the dashboard. The front end can be accessed here:

![https://student-success-analysis.herokuapp.com/]

## Dashboard
To do