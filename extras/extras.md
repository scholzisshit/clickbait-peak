## Just a file of my attempts at trying to figure out how to write documentation

So from what I understand the dataset contains online advertisement interactions with columns: Daily Time Spent on Site, Age, Area Income, Daily Internet Usage, Ad Topic Line, City, Sex, Country, Timestamp, and the target “Clicked on Ad” (1 for clicked, 0 for not)

Exploratory Data Analysis (EDA)


Data shape (rows, columns): (1000, 10)
First 5 rows of dataset:
   Daily Time Spent on Site  Age  ...            Timestamp  Clicked on Ad
0                     68.95   35  ...  2016-03-27 00:53:11              0
1                     80.23   31  ...  2016-04-04 01:39:02              0
2                     69.47   26  ...  2016-03-13 20:35:42              0
3                     74.15   29  ...  2016-01-10 02:31:19              0
4                     68.37   35  ...  2016-06-03 03:36:18              0

[5 rows x 10 columns]
Top 10 Cities by frequency:
City
Lisamouth          3
Williamsport       3
West Amanda        2
East Timothy       2
Lake Patrick       2
Wrightburgh        2
New Sheila         2
Port Juan          2
New Jessicaport    2
Millerbury         2
Name: count, dtype: int64
Top 10 Countries by frequency:
Country
Czech Republic    9
France            9
Senegal           8
Peru              8
Greece            8
Australia         8
Micronesia        8
South Africa      8
Turkey            8
Afghanistan       8
Name: count, dtype: int64
Missing values per column:
Daily Time Spent on Site    0
Age                         0
Area Income                 0
Daily Internet Usage        0
Ad Topic Line               0
City                        0
Male                        0
Country                     0
Timestamp                   0
Clicked on Ad               0
dtype: int64
Click class distribution:
Clicked on Ad
0    0.5
1    0.5
Name: proportion, dtype: float64




Missing Values Per Column:
Daily Time Spent on Site    0
Age                         0
Area Income                 0
Daily Internet Usage        0
Ad Topic Line               0
City                        0
Male                        0
Country                     0
Timestamp                   0
Clicked on Ad               0
dtype: int64

Top 10 Cities by frequency:
City
Lisamouth          3
Williamsport       3
West Amanda        2
East Timothy       2
Lake Patrick       2
Wrightburgh        2
New Sheila         2
Port Juan          2
New Jessicaport    2
Millerbury         2
Name: count, dtype: int64

Top 10 Countries by frequency:
Country
Czech Republic    9
France            9
Senegal           8
Peru              8
Greece            8
Australia         8
Micronesia        8
South Africa      8
Turkey            8
Afghanistan       8
Name: count, dtype: int64

Unique Ad Topics: 1000
Top 5 Ad Topics:
Ad Topic Line
Cloned 5thgeneration orchestration       1
Monitored national standardization       1
Organic bottom-line service-desk         1
Triple-buffered reciprocal time-frame    1
Robust logistical utilization            1
Name: count, dtype: int64

Clicked on Ad class distribution:
Clicked on Ad
0    0.5
1    0.5
Name: proportion, dtype: float64



[Running] python -u "f:\ediglobe\Preprocessing.py"
Accuracy: 0.95
Precision: 0.954954954954955
Recall: 0.954954954954955
Confusion Matrix:
 [[ 84   5]
 [  5 106]]

[Done] exited with code=0 in 9.272 seconds


## Model Performance Interpretation
Accuracy: 0.95

95% of test predictions match actual outcomes—shows strong overall performance for balanced classes.

Precision: 0.9549

Of all users predicted as “likely to click,” 95.5% actually clicked—your model avoids false positives and is efficient for targeting.

Recall: 0.9549

Out of all users who clicked, 95.5% were correctly identified—your model effectively finds almost all actual clickers.

Confusion Matrix:

text
[[ 84   5]
 [  5 106]]
Top-left: True negatives (did not click, predicted as not clicking): 84

Bottom-right: True positives (clicked and predicted as clicking): 106

Top-right: False positives (predicted as click but did not): 5

Bottom-left: False negatives (missed actual clickers): 5
