def calc_cost(lat, longi):
    return 0.81513876 * lat + -1.84947622 * longi + 0.076020


latit = 37.7069276929
longi = -122.51149999
max_latitude = 37.7069276929
max_longitude = -122.51149999
while latit < 37.8310927851:
    while longi < -122.364758519:
        if calc_cost(latit, longi) > calc_cost(max_latitude, max_longitude):
            max_latitude = latit
            max_longitude = longi
        longi += 0.00001
    print(latit)
    longi = -122.51149999
    latit += 0.00001
print(max_latitude)
print(max_longitude)
print(calc_cost(max_latitude,max_longitude))