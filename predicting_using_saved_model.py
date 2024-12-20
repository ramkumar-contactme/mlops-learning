# # Load the model
import joblib
salarymodel = joblib.load("mymodel1.pkl")
print(salarymodel.predict([[5]]))