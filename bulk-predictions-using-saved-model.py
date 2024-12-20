import joblib
model=joblib.load("mymodel1.pkl")

f=open("bulk_experiences.txt",'r')
experiences=[]
for line in f:
    experiences.append([float(line)])
print(experiences)
f.close()

predictions = model.predict(experiences)

for years, salary in zip(experiences,predictions):
    print(f"For {years[0]} of experience, the predicted salary in {salary}")