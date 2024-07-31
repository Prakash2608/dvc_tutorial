import pandas as pd

Data = [
    {"name":"Prakash", "age":27, "city":"Chennai"},
    {"name":"Arun", "age":26, "city":"Delhi"},
    {"name":"Sivaraj", "age":28, "city":"Bangalore"},
    {"name":"Hari", "age":25, "city":"Noida"}
]

data = pd.DataFrame(Data)

data.to_csv("data/data.csv", index = False)