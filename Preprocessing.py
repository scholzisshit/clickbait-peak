import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# i dont understand much of this code but here is a preprocessing script for the advertising dataset that includes feature engineering and data splitting for model training.



from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix


df = pd.read_csv("advertising.csv")


df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df['Hour'] = df['Timestamp'].dt.hour
df['DayOfWeek'] = df['Timestamp'].dt.dayofweek


features = [
    'Daily Time Spent on Site', 'Age', 'Area Income', 
    'Daily Internet Usage', 'Male', 'Hour', 'DayOfWeek'
]
X = df[features]
y = df['Clicked on Ad']





# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Standardize numeric features
scaler = StandardScaler()
num_features = ['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage']

X_train[num_features] = scaler.fit_transform(X_train[num_features])
X_test[num_features] = scaler.transform(X_test[num_features])


# seems important for model training``

# Create and train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)




# Predict on test set
y_pred = model.predict(X_test)


# Evaluate model performance
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Precision:', precision_score(y_test, y_pred))
print('Recall:', recall_score(y_test, y_pred))
print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred))
