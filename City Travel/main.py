myfile = open('provinces.txt')
myfile = myfile.read()
myfile_ =  myfile.split("\n")

provinces = []
latitude = []
longtitude = []
recommend = []
places = []
possible_d = []
possible_a = []

car = 90
motor = 80
bicycle = 25

for i in myfile_:
    b = i.split(",")
    provinces.append(b[0])
    latitude .append(b[1])
    longtitude.append(b[2])

departure = input("Departure province:\n")

while departure.upper() not in provinces:
    print('Province not found!')
    for i in provinces:
        if departure.upper() in i:
            if i.index(departure.upper()) == 0:
                possible_d.append(i)
    if len(possible_d) == 1:
        print("Possible province:" + ",".join(sorted(possible_d)))
    elif len(possible_d) > 1:
        print("Possible provinces:" + ",".join(sorted(possible_d)))
    departure = input("Departure province:\n")
    possible_d = []
    continue

arrival = input("Arrival province:\n")

while arrival.upper() not in provinces:
    print('Province not found!')
    for i in provinces:
        if arrival.upper() in i:
            if i.index(arrival.upper()) == 0:
                possible_a.append(i)

    if len(possible_a) == 1:
        print("Possible province:" + ",".join(sorted(possible_a)))
    elif len(possible_a) > 1:
        print("Possible provinces:" + ",".join(sorted(possible_a)))
    arrival = input("Arrival province:\n")
    possible_a = []
    continue

type1 = input("Enter travel type:\n")

while type1.upper() != 'CAR' and type1.upper() != 'MOTORCYCLE' and type1.upper() != 'BICYCLE':
        type1 = input("Enter travel type:\n")
        continue

print('\nI am calculating the distance between ' + departure.upper() + ' and ' + arrival.upper() + ' ...')
print('')

dx = (float(latitude[provinces.index(arrival.upper())]) - float(latitude[provinces.index(departure.upper())]))
dy = (float(longtitude[provinces.index(arrival.upper())]) - float(longtitude[provinces.index(departure.upper())]))
distance = (dx**2+dy**2)**0.5
distance_km = distance*100

print('Distance: '+ str(distance_km.__round__(2)) + ' km')

if type1.upper() == "CAR":
    time = distance_km/car
elif type1.upper() == "MOTORCYCLE":
    time = distance_km/motor
elif type1.upper() == "BICYCLE":
    time = distance_km/bicycle

hours = int(time)
minute = (time-hours)*60
minute = int(minute)

print('Approximate travel time with ' + type1.upper() + ': '+ str(hours) + ' hours ' + str(minute) + ' minutes')

for i in provinces:
    dx = (float(latitude[provinces.index(i)]) - float(latitude[provinces.index(departure.upper())]))
    dy = (float(longtitude[provinces.index(i)]) - float(longtitude[provinces.index(departure.upper())]))
    distance = (dx ** 2 + dy ** 2) ** 0.5
    distance_km = distance * 100
    recommend.append(distance_km)

a = min(recommend)
provinces.remove(provinces[recommend.index(a)])
recommend.remove(a)

for j in range(3):
    g = min(recommend)
    places.append((provinces[(recommend.index(g))]))
    provinces.remove(provinces[recommend.index(g)])
    recommend.remove(g)

print('Recommended places close to '+ departure.upper() + ':' +  ",".join(sorted(places)))