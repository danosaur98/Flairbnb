import numpy as np
import pandas as pd


def estimate_price(lat, longi):
    error = "Please enter a latitude and longitude within San Francisco! (Between 37.7069276929 and 37.8310927851" \
            " latitude & -122.51149999 and -122.364758519 longitude."
    try:
        lat = float(lat)
        longi = float(longi)
    except:
        return error

    if (lat < 37.7069276929 or lat > 37.8310927851):
        return "lat error" + str(lat)
    if (longi < -122.51149999 or longi > -122.364758519):
        return "longi error" + str(longi)
    df = pd.read_csv("listings.csv", low_memory=False)
    #df = pd.read_csv("/home/ubuntu/Flairbnb/Flairbnb/listings.csv")
    latitude = np.array(df['latitude'])
    longitude = np.array(df['longitude'])
    df['price'] = df['price'].map(lambda x: x[1:].replace(',', '')).astype(float)
    income = np.array(df['price'])

    considered = []
    cost = 0
    tolerance = 0.005
    for i in range(len(latitude)):
        if ((latitude[i] - lat) ** 2 + (longitude[
                                            i] - longi) ** 2) ** .5 < tolerance:  # if the distance is within 0.005, consider it for the estimation
            considered.append(i)
            cost += income[i]
    if len(considered) == 0:
        return "Not enough data in area to give a good estimate!"
    return cost / len(considered)

    # for i in np.arange(37.7069276929, 37.8310927851, 0.001):
    #print(i)
lati = 37.77
longi = -122.42
print(estimate_price(37.77, -122.42))
x = 0.81513876*37.77 + -1.84947622*-122.42 + 0.076020
print(x)
