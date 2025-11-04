# im writing this comment after finishing this ----- Should i write more comments???
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('advertising.csv')  


print("Data shape (rows, columns):", df.shape)
print("First 5 rows of dataset:")
print(df.head())

numerical_features = ['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage']

for feature in numerical_features:
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    sns.histplot(df[feature], bins=30, kde=True)
    plt.title(f'Distribution of {feature}')
    
    plt.subplot(1,2,2)
    sns.boxplot(x=df[feature])
    plt.title(f'Boxplot of {feature}')
    plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x='Male', data=df)
plt.title('Gender Distribution')
plt.show()

print("Top 10 Cities by frequency:")
print(df['City'].value_counts().head(10))

print("Top 10 Countries by frequency:")
print(df['Country'].value_counts().head(10))

print("Missing values per column:")
print(df.isnull().sum())

click_dist = df['Clicked on Ad'].value_counts(normalize=True)
print("Click class distribution:")
print(click_dist)

df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')


df['Hour'] = df['Timestamp'].dt.hour
df['DayOfWeek'] = df['Timestamp'].dt.dayofweek  # Monday=0, Sunday=6
df['Month'] = df['Timestamp'].dt.month









# Visualize time of day clicks
plt.figure(figsize=(8,5))
sns.countplot(x='Hour', hue='Clicked on Ad', data=df)
plt.title('Clicks by Hour of Day')
plt.show()

# Visualize day of week clicks
plt.figure(figsize=(8,5))
sns.countplot(x='DayOfWeek', hue='Clicked on Ad', data=df)
plt.title('Clicks by Day of Week')
plt.show()
