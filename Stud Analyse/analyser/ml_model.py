# analyser/ml_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def train_model():
    # Fake training data for demonstration
    # In production, you can fetch all historical marks, attendance, and activity data from DB
    data = [
        # maths, science, english, attendance%, activity_score, category
        [95, 90, 92, 95, 80, "Excellent"],
        [75, 80, 70, 85, 60, "Good"],
        [60, 65, 70, 70, 50, "Average"],
        [50, 55, 60, 60, 40, "Below Average"],
        [30, 40, 35, 50, 20, "Poor"],
    ]

    df = pd.DataFrame(data, columns=["maths","science","english","attendance","activity","category"])

    X = df[["maths","science","english","attendance","activity"]]
    y = df["category"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_scaled, y)

    return clf, scaler
