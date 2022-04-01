you will implement a program which is able to estimate approximate travel time according to flight istances

Example run #1:

Departure province:
Izmir
Arrival province:
Ankara
Enter travel type:
Car
I am calculating the distance between IZMIR and ANKARA ...
Distance: 591.91 km
Approximate travel time with CAR: 6 hours 34 minutes
Recommended places close to IZMIR:AYDIN,BALIKESIR,MANISA



Rules:
● We assume that the operations are based on flight distance, so the calculations (distance,
time) are approximate (not precise calculation).
● All user inputs are case-insensitive (e.g. users may enter such things as “AnKaRa”,
“ANKara”, “ankara”).
● Although the actual province names contain Turkish characters, we assume that users can
not enter non-English characters (e.g. users have to write such as “Izmir”, “Gumushane”,
“Duzce”, instead of writing “İzmir”, “Gümüşhane”, “Düzce”).
● We assume that the user has entered at least one character, you do not need to check
empty values.
● The text file (provinces.txt) contains province names, their locations as latitude and
longitude in a format given below. All data are separated by commas.

Travel          Type Speed
Car              90 km/h
Motorcycle       80 km/h
Bicycle          25 km/h

Departure province:
An
Province not found!
Possible provinces:ANKARA,ANTALYA
Departure province:
X
Province not found!
Departure province:
Ankara
Arrival province:
Iz
Province not found!
Possible province:IZMIR
Arrival province:
Izmir
Enter travel type:
Car
Travel Type Speed
Car 90 km/h
Motorcycle 80 km/h
Bicycle 25 km/hI am calculating the distance between ANKARA and IZMIR ...
Distance: 591.91 km
Approximate travel time with CAR: 6 hours 34 minutes
Recommended places close to ANKARA:CANKIRI,KARABUK,KIRIKKALE
Example run #3:
Departure province:
Izmir
Arrival province:
IZMIR
Enter a different province!
Arrival province:
Ankara
Enter travel type:
Car
I am calculating the distance between IZMIR and ANKARA ...
Distance: 591.91 km
Approximate travel time with CAR: 6 hours 34 minutes
Recommended places close to IZMIR:AYDIN,BALIKESIR,MANISA
Example run #4:
Departure province:
Izmir
Arrival province:
Ankara
Enter travel type:
C
Enter travel type:
A
Enter travel type:
CAR
I am calculating the distance between IZMIR and ANKARA ...
Distance: 591.91 km
Approximate travel time with CAR: 6 hours 34 minutes
Recommended places close to IZMIR:AYDIN,BALIKESIR,MANISA