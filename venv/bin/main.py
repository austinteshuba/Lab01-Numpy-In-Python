## Working with Pandas
## Austin Teshuba

#Import Car Dataset
import pandas as pd
import numpy
path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(path, header = None)

# Question One: Check the bottom ten rows.
bottomTen = df.tail(10)
print(bottomTen)

#Add Headers
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers


# Drop missing values in price
df = df.replace("?", numpy.NaN) # Fix formatting throughout.
df = df.dropna(subset=["price"], axis=0)

#Question Two: Check Header names
print(df.columns)

#Save Updated Dataset to machine
df.to_csv("automobile.csv", index=False)

# Check the statistical summary of only the numeric values
print(df.describe())

# Check the statistical summary of all the values, including the non-numeric (i.e. Object types)
print(df.describe(include = "all"))

# Question Three: Onlu describe the length and compression ratio columns
print(df[["compression-ratio", "length"]].describe())

