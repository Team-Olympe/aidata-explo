import mysql.connector
import pandas as pd
from sklearn.linear_model import LinearRegression
import datetime
import matplotlib.pyplot as plt

print("Step 1: Connect to MySQL server")
cnx = mysql.connector.connect(user='288967', password='stur0MAU-heew7seeg',
                              host='mysql-explo-data.alwaysdata.net', database='explo-data_1')

print("Step 2: Query data from MySQL")

query = '''
SELECT DATE(Cle_Temps) AS date, COUNT(*) AS sales, SUM(Marge_Revient) AS profit, SUM(Marge_Revient) / COUNT(*) AS ratio
FROM `Ventes`
WHERE DATE(Cle_Temps) < DATE("2018-12-01")
GROUP BY YEAR(date), MONTH(date) 
'''
df = pd.read_sql(query, cnx)
cnx.close()

print("Step 3: Prepare data for modeling")
df['date']=df['date'].map(datetime.datetime.toordinal) # convert date to datetime object
X = df[['date']] # features
Y = df['sales'] # target variable

print("Step 4: Clean and preprocess data")
# To-do: fill missing data points

print("Step 5: Train model")
model = LinearRegression()
model.fit(X, Y)

# Step 6: Make predictions
print("Step 6: Make predictions")

pY = []
pX = []
date = datetime.date.fromordinal(df['date'][0])
for i in range(len(df['date']) + 6):
    new_data = [[datetime.datetime.toordinal(date)]]
    prediction = model.predict(new_data)
    pX.append(datetime.datetime.toordinal(date))
    pY.append(prediction)
    date += datetime.timedelta(weeks=4)

# Plot the time series
plt.plot(X.applymap(datetime.date.fromordinal), Y,  label = "real data")
plt.plot(list(map(datetime.date.fromordinal, pX)), pY, label = "prediction")

# Add x and y labels
plt.xlabel('Time')
plt.ylabel('Value')

plt.legend()

# Show the plot
plt.show()
