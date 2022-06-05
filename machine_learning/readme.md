# Machine Learning Notes

### Description of preliminary data preprocessing 
We used the observed weather conditions from different weather stations around the twin cities.

### Description of preliminary feature engineering and preliminary feature selection, including their decision-making process
From those observations we cleaned the data to be able to plug into our models. For example, to determine the day of the year specific temperatures will occur, the date of an observation was in month/day/year format and we changed it to a numerical representation of the day of the year. In doing so allowed us to visualize how weather conditions change for specific days of the year and create a linear model to track those trends.

### Description of how data was split into training and testing sets 
To be able to classify a day with frost the observation data was used as a training dataset find patterns and develop understanding of a day with freezing condition to create frost. The test set dropped the column that categorize which day was freezing or not to see if the model was accurate.

###  Explanation of model choice

![Frost_obs_doy](https://user-images.githubusercontent.com/56700719/171307931-f8ad3cc2-a384-46a4-8f35-f71f13d5822e.JPG)

- We decided to use a logistical regression model to first see if the model could classify a day with freezing conditions based on the weather features.

![avg_fit_line](https://user-images.githubusercontent.com/56700719/171308288-fde4ea21-319b-4c7f-bdfc-b6df9fe2294a.JPG)
![Min_fit_line](https://user-images.githubusercontent.com/56700719/171308325-21706a2f-b886-4908-9c74-1987c00d4800.JPG)

- Next, we wanted to show how using one feature can change predicting a day of the year that will be below freezing. By using linear regression, two models were created to show two different trends based off different features.

![first_predict](https://user-images.githubusercontent.com/56700719/171308415-87ee9025-0895-465f-b0cb-f24fd69f53ca.JPG)
![second_predict](https://user-images.githubusercontent.com/56700719/171308424-a8094bc4-3c44-476a-91d3-105c2af557b3.JPG)
![predict_coefficient](https://user-images.githubusercontent.com/56700719/171308427-2d387fa1-971f-4da7-8628-b082304aab63.JPG)

- The last model puts those two features together and uses linear regression to create a best fit line and predict the day of the year in which an average temp and minimum temp (around freezing) will occur.


### Each Program Specifics

- Linear_min_vs_avg.ipynb -> Creates two models using linear regression to show the difference between average temp and minimum temp with their corresponding day of the year.

- Linear_Predict_day.ipynb -> Creates model to try and predict the day of the year in which specific average and minimum temp take place.

- Logistic_classify_day.ipynb -> Creates model to classify a day with frost based on past weather conditions.
