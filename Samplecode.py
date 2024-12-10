import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix 

data = { 
'income': [25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000, 115000], 
'family_size': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 
'expenses': [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500], 
'assets': [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000], 
'debt': [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000], 
'eligibility': [1, 1, 1, 0, 0, 0, 0, 0, 0, 0] 
} 

df = pd.DataFrame(data) 

X = df.drop('eligibility', axis=1) 
y = df['eligibility'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

model = RandomForestClassifier(n_estimators=100, random_state=42) 
model.fit(X_train, y_train) 

y_pred = model.predict(X_test) 

print("Accuracy:", accuracy_score(y_test, y_pred)) 
print("Classification Report:") 
print(classification_report(y_test, y_pred)) 
print("Confusion Matrix:") 
print(confusion_matrix(y_test, y_pred)) 

def predict_eligibility(income, family_size, expenses, assets, debt): 
user_data = pd.DataFrame({ 
'income': [income], 
'family_size': [family_size], 
'expenses': [expenses], 
'assets': [assets], 
'debt': [debt] 
}) 
prediction = model.predict(user_data) 
return prediction[0] 

# Function to ensure valid float input
def get_float_input(prompt):
while True:
try:
return float(input(prompt))
except ValueError:
print("Invalid input. Please enter a valid number.")

# Function to ensure valid integer input
def get_int_input(prompt):
while True:
try:
return int(input(prompt))
except ValueError:
print("Invalid input. Please enter a valid integer.")

# Function to take user input and display eligibility
def interactive_input():
print("Please answer the following questions to determine eligibility:\n")
income = get_float_input("What is your monthly income? ")
family_size = get_int_input("How many people are in your family? ")
expenses = get_float_input("What are your monthly expenses? ")
assets = get_float_input("What is the total value of your assets? ")
debt = get_float_input("What is the total amount of your debt? ")
eligibility = predict_eligibility(income, family_size, expenses, assets, debt)
if eligibility == 1:
print("\nYou are eligible for the following programs:")
print("- Government assistance programs")
print("- Loan programs with favorable terms")
print("- Investment opportunities")
else:
print("\nYou are not eligible for any of the programs at this time.")

interactive_input()


# We would use this sort of code to figure out/define different charities requirnments for people to have
