sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
  
}
keys = ["name", "salary"]
alpha={}
for i in keys:
	alpha[i]=sampleDict[i]

print(alpha)