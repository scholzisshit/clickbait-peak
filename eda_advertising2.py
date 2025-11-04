

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("advertising.csv")


for feature in ['Age', 'Area Income', 'Daily Internet Usage']:
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    sns.histplot(df[feature], bins=30, kde=True)
    plt.title(f'Distribution of {feature}')
        
    plt.subplot(1,2,2)
    sns.boxplot(x=df[feature])
    plt.title(f'Boxplot of {feature}')
    plt.show()

print("\nMissing Values Per Column:")
print(df.isnull().sum())


plt.figure(figsize=(6,4))
sns.countplot(x='Male', data=df)
plt.title('Gender Distribution')
plt.show()


print("\nTop 10 Cities by frequency:")
print(df['City'].value_counts().head(10))

print("\nTop 10 Countries by frequency:")
print(df['Country'].value_counts().head(10))


print("\nUnique Ad Topics:", df['Ad Topic Line'].nunique())
print("Top 5 Ad Topics:")
print(df['Ad Topic Line'].value_counts().head(5))


click_dist = df['Clicked on Ad'].value_counts(normalize=True)
print("\nClicked on Ad class distribution:")
print(click_dist)


# Extract time-based features
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')