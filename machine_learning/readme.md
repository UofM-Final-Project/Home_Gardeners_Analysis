# Machine Learning Notes

### Description of preliminary data preprocessing 
We used the observed weather conditions from different weather stations around the twin cities.

### Description of preliminary feature engineering and preliminary feature selection, including their decision-making process
From those observations we cleaned the data to be able to plug into our models. For example, to determine the day of the year specific temperatures will occur, the date of an observation was in month/day/year format and we changed it to a numerical representation of the day of the year. In doing so allowed us to visualize how weather conditions change for specific days of the year and create a linear model to track those trends.

### Description of how data was split into training and testing sets 
To be able to classify a day with frost the observation data was used as a training dataset find patterns and develop understanding of a day with freezing condition to create frost. The test set dropped the column that categorize which day was freezing or not to see if the model was accurate.

###  Explanation of model choice
We decided to use a logistical regression model to first see if the model could classify a day with freezing conditions based on the weather features.
Next, we wanted to show how using one feature can change predicting a day of the year that will be below freezing. By using linear regression, two models were created to show two different trends based off different features. The last model puts those two features together and uses linear regression to create a best fit line and predict the day of the year in which an average temp and minimum temp (around freezing) will occur.


### Each Program Specifics

- Linear_min_vs_avg.ipynb -> Creates two models using linear regression to show the difference between average temp and minimum temp with their corresponding day of the year.

- Linear_Predict_day.ipynb -> Creates model to try and predict the day of the year in which specific average and minimum temp take place.

- Logistic_classify_day.ipynb -> Creates model to classify a day with frost based on past weather conditions.
