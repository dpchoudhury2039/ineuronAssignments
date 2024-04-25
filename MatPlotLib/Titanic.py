import pandas as pd
import matplotlib.pyplot as plt

# Read the Titanic dataset
url = 'https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic = pd.read_csv(url)

# Task 1: Pie Chart for Male/Female Proportion
gender_counts = titanic['sex'].value_counts()  # Count males and females
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Male/Female Proportion in Titanic Dataset')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is a circle
plt.show()

# Task 2: Scatterplot with Fare and Age, Differentiated by Gender
plt.figure(figsize=(8, 6))
colors = {'male': 'blue', 'female': 'red'}  # Define colors for gender

# Drop rows with missing values in 'age' or 'fare'
titanic_filtered = titanic.dropna(subset=['age', 'fare', 'sex'])

# Create the scatter plot with colors based on gender
plt.scatter(
    titanic_filtered['age'],
    titanic_filtered['fare'],
    c=titanic_filtered['sex'].map(colors),  # Map gender to colors
    alpha=0.6,  # Transparency for better visibility
    s=40  # Size of the scatter points
)

plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Scatterplot of Fare Paid vs. Age, Differentiated by Gender')
plt.show()
