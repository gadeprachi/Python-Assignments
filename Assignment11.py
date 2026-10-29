ASSIGNMENT-11

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Create dummy categorical data
data = {
    'Age_Group': ['Young', 'Middle', 'Senior', 'Young', 'Middle',
                  'Senior', 'Young', 'Middle'],
    'Income': ['High', 'Low', 'Medium', 'Medium', 'High',
               'Low', 'Low', 'High'],
    'Student': ['No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes'],
    'Purchased': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes']
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Separate features (X) and target (y)
X = df.drop(columns=['Purchased'])A
y = df['Purchased']

# Split into training (75%) and testing (25%) sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# 2. Apply One-Hot Encoding to categorical features
categorical_features = ['Age_Group', 'Income', 'Student']

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ]
)

# 3. Build a pipeline (preprocessing + model)
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

# 4. Train the model
model_pipeline.fit(X_train, y_train)

# 5. Predict on the test set
y_pred = model_pipeline.predict(X_test)

# 6. Evaluate results
print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred, zero_division=0))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))




