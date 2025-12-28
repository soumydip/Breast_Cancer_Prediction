import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('data.csv')
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})
X = data.drop(['id', 'diagnosis'], axis=1)
Y = data['diagnosis']
# find min and max value for each feature
min_values = X.min()
max_values = X.max()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)

# model acuracy
model_accuracy = accuracy_score(Y_test, model.predict(X_test))
print(f"Model Accuracy: {model_accuracy * 100:.2f}%")

def get_user_prediction():
    print("\n" + "="*60)
    print("Breast Cancer Prediction System ")
    print("="*60)
    
    user_data = []
    
    for feature in X.columns:
        low = min_values[feature]
        high = max_values[feature]
        
        while True:
            try:
                val = float(input(f"Enter {feature} (Range: {low:.2f} - {high:.2f}): "))
                
                if val < low or val > high:
                    print(f"Wrong! Please enter a number between {low:.2f} and {high:.2f}.")
                else:
                    user_data.append(val)
                    break 
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

    final_input = np.array(user_data).reshape(1, -1)
    prediction = model.predict(final_input)
    prob = model.predict_proba(final_input)

    print("\n" + "*"*40)
    if prediction[0] == 1:
        print("result: MALIGNANT (M) -  Consert a doctor immediately!")
    else:
        print("result: BENIGN (B) - You are safe.")
    
    print(f"Model Confidence: {np.max(prob) * 100:.2f}%")
    print("*"*40)

# Run the prediction function
get_user_prediction()