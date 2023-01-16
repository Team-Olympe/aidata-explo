import mysql.connector
import pandas as pd
from sklearn.linear_model import LinearRegression
import datetime
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose


# Connect to MySQL server
print("Connect to MySQL server")
cnx = mysql.connector.connect(user='288967', password='stur0MAU-heew7seeg',
                              host='mysql-explo-data.alwaysdata.net', database='explo-data_1')

# Query data from MySQL
print("Query data from MySQL")

query = '''
SELECT DATE(Cle_Temps) AS date, COUNT(*) AS sales, Cle_Produit
FROM `Ventes`
WHERE DATE(Cle_Temps) < DATE("2018-12-01")
GROUP BY YEAR(date), MONTH(date), Cle_Produit 
'''
df = pd.read_sql(query, cnx)
print(df)
cnx.close()

# Prepare data for modeling
print("Prepare data for modeling")
df['date']=df['date'].map(datetime.datetime.toordinal) # convert date to datetime object
X = df[['date']] # features
Y = df['sales'] # target variable

# Perform seasonal decomposition
result = seasonal_decompose(Y, model='additive')

# Extract the trend, seasonality, and residual components
trend = result.trend
seasonality = result.seasonal
residual = result.resid

# Train model
print("Train model")

model = LinearRegression()
model.fit(X, Y)

# Make predictions
print("Make predictions")

pY = []
pX = []
date = datetime.date.fromordinal(df['date'][0])
for i in range(len(df['date']) + 6):
    new_data = [[datetime.datetime.toordinal(date)]]
    prediction = model.predict(new_data)
    pX.append(datetime.datetime.toordinal(date))
    pY.append(prediction)
    date += datetime.timedelta(weeks=4)

# # Plot the time series
plt.plot(X.applymap(datetime.date.fromordinal), Y,  label = "real data")
plt.plot(list(map(datetime.date.fromordinal, pX)), pY, label = "prediction")


# Make long-term trend predictions using the trend component
trend_predictions = []
for i in range(len(pX)):
    trend_predictions.append(trend[i % len(trend)] + seasonality[i % len(seasonality)])

# Make short-term seasonality predictions using the seasonality component
seasonality_predictions = []
for i in range(len(pX)):
    seasonality_predictions.append(seasonality[i % len(seasonality)])

# Combine the trend and seasonality predictions to get the final prediction
predictions = []
for i in range(len(pX)):
    predictions.append(trend_predictions[i] + seasonality_predictions[i])

plt.plot(list(map(datetime.date.fromordinal, pX)), predictions, label = "prediction w/ season")

# Add x and y labels
plt.xlabel('Time')
plt.ylabel('Value')

plt.legend()

# Show the plot
plt.show()
