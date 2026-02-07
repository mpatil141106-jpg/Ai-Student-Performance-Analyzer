# student_analyzer_batch.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score

# ==========================
# Step 1: Load Student Data
# ==========================
# CSV file should have columns: Name, Attendance, Activity, Grade
# Example CSV:
# Name,Attendance,Activity,Grade
# John,95,80,88
# Alice,60,50,55

data = pd.read_csv('students.csv')

# Features & Labels (we can label performance based on Grade for training)
# Here, we'll create a simple mapping for training purpose
def map_performance(grade):
    if grade >= 85:
        return 'Excellent'
    elif grade >= 70:
        return 'Good'
    elif grade >= 50:
        return 'Average'
    else:
        return 'Poor'

data['Performance'] = data['Grade'].apply(map_performance)

X = data[['Attendance', 'Activity', 'Grade']]
y = data['Performance']

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split for training & testing
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# ==========================
# Step 2: Train Model
# ==========================
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# ==========================
# Step 3: Predict & Suggest
# ==========================
def generate_suggestions(attendance, activity, grade):
    suggestions = []
    if attendance < 75:
        suggestions.append("Increase attendance to at least 75%.")
    if activity < 60:
        suggestions.append("Participate more in extracurricular activities.")
    if grade < 65:
        suggestions.append("Focus on weak subjects, revise regularly, and seek help from teachers.")
    if not suggestions:
        suggestions.append("Keep up the good work!")
    return " | ".join(suggestions)

# Predict performance for all students
data['Predicted_Performance'] = model.predict(scaler.transform(data[['Attendance', 'Activity', 'Grade']]))
data['Improvement_Suggestions'] = data.apply(
    lambda row: generate_suggestions(row['Attendance'], row['Activity'], row['Grade'])
    if row['Predicted_Performance'] in ['Poor', 'Average'] else "🎉 Excellent performance!", axis=1
)

# ==========================
# Step 4: Save Report
# ==========================
data.to_csv('student_performance_report.csv', index=False)
print("\nStudent performance report generated: student_performance_report.csv")
