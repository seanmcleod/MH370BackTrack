import math
import Geo

'''
satelliteInfo1940 = { 'LatLon': (1.640,64.520), 'XYZ' : (18140.934782,38066.764468,1206.206412), 'Velocity': (0.001663,-0.000776,-0.001656),  'LOSSpeed': Geo.knotsToKms(-53.74), 'NextPingTimeOffset': 60.0, 'PingRadius': Geo.nmToKm(1762), 'Color': 'b', 'Elevation': 55.80 }
satelliteInfo2040 = { 'LatLon': (1.576,64.510), 'XYZ' : (18147.379654,38064.186790,1159.122617), 'Velocity': (0.001811,-0.000618,-0.024394),  'LOSSpeed': Geo.knotsToKms(-70.87), 'NextPingTimeOffset': 60.0, 'PingRadius': Geo.nmToKm(1805), 'Color': 'c', 'Elevation': 54.98 }
satelliteInfo2140 = { 'LatLon': (1.404,64.500), 'XYZ' : (18154.399609,38061.901891,1032.716137), 'Velocity': (0.001962,-0.000627,-0.045468),  'LOSSpeed': Geo.knotsToKms(-84.20), 'NextPingTimeOffset': 60.0, 'PingRadius': Geo.nmToKm(1962), 'Color': 'g', 'Elevation': 52.01 }
satelliteInfo2240 = { 'LatLon': (1.136,64.490), 'XYZ' : (18161.767618,38059.215141,835.616356),  'Velocity': (0.001981,-0.000841,-0.063437),  'LOSSpeed': Geo.knotsToKms(-97.14), 'NextPingTimeOffset': 91.0, 'PingRadius': Geo.nmToKm(2199), 'Color': 'r', 'Elevation': 47.54 }
satelliteInfo0011 = { 'LatLon': (0.589,64.471), 'XYZ' : (18173.906276,38051.980584,433.193954),  'Velocity': (0.001476,-0.001458,-0.082097),  'LOSSpeed': Geo.knotsToKms(-111.18),'NextPingTimeOffset':  0.0, 'PingRadius': Geo.nmToKm(2642), 'Color': 'm', 'Elevation': 39.33 }
'''

satelliteInfo1940 = { 'LatLon': (1.640,64.520), 'XYZ' : (18140.934782,38066.764468,1206.206412), 'Velocity': (0.001663,-0.000776,-0.001656),  'LOSSpeed': Geo.knotsToKms(-36.48), 'NextPingTimeOffset': 60.0, 'PingRadius': Geo.nmToKm(1815), 'Color': 'b', 'Elevation': 54.8 }
satelliteInfo2040 = { 'LatLon': (1.576,64.510), 'XYZ' : (18147.379654,38064.186790,1159.122617), 'Velocity': (0.001811,-0.000618,-0.024394),  'LOSSpeed': Geo.knotsToKms(-62.93), 'NextPingTimeOffset': 60.0, 'PingRadius': Geo.nmToKm(1852), 'Color': 'c', 'Elevation': 54.1 }
satelliteInfo2140 = { 'LatLon': (1.404,64.500), 'XYZ' : (18154.399609,38061.901891,1032.716137), 'Velocity': (0.001962,-0.000627,-0.045468),  'LOSSpeed': Geo.knotsToKms(-87.29), 'NextPingTimeOffset': 60.0, 'PingRadius': Geo.nmToKm(1984), 'Color': 'g', 'Elevation': 51.6 }
satelliteInfo2240 = { 'LatLon': (1.136,64.490), 'XYZ' : (18161.767618,38059.215141,835.616356),  'Velocity': (0.001981,-0.000841,-0.063437),  'LOSSpeed': Geo.knotsToKms(-108.42),'NextPingTimeOffset': 91.0, 'PingRadius': Geo.nmToKm(2212), 'Color': 'r', 'Elevation': 47.3 }
satelliteInfo0011 = { 'LatLon': (0.589,64.471), 'XYZ' : (18173.906276,38051.980584,433.193954),  'Velocity': (0.001476,-0.001458,-0.082097),  'LOSSpeed': Geo.knotsToKms(-133.83),'NextPingTimeOffset':  0.0, 'PingRadius': Geo.nmToKm(2599), 'Color': 'm', 'Elevation': 40.1 }

satelliteInfos = [satelliteInfo1940, satelliteInfo2040, satelliteInfo2140, satelliteInfo2240, satelliteInfo0011] 

satelliteGeo = { 'LatLon': (0.0,64.5), 'XYZ': (18155.08346350262, 38062.92402631797, 0.0), 'Velocity': (0.0,0.0,0.0)}

groundTruth1630 = { 'AircraftLatLon': (2.746700,101.713300), 'AircraftSpeed': Geo.knotsToKms(0.0), 'AircraftTrack' : 230.0 }
groundTruth1642 = { 'AircraftLatLon': (2.813056,101.679722), 'AircraftSpeed': Geo.knotsToKms(201.0), 'AircraftTrack' : 327.0 }
groundTruth1654 = { 'AircraftLatLon': (3.931600,102.161800), 'AircraftSpeed': Geo.knotsToKms(452.0), 'AircraftTrack' : 25.0 }
groundTruth1707 = { 'AircraftLatLon': (5.419167,102.864167), 'AircraftSpeed': Geo.knotsToKms(469.0), 'AircraftTrack' : 25.0 }

groundTruths = [groundTruth1630, groundTruth1642, groundTruth1654, groundTruth1707]

print(Geo.sphericalToECEFAlt(satelliteGeo['LatLon'], 35800))

'''
for satelliteInfo in satelliteInfos:
    print Geo.KmsToKmh(satelliteInfo['LOSSpeed'])
'''

def groundCheckGeoSat(groundspeed, bearing, aircraftPos):
    aircraftECEF = Geo.sphericalToECEF(aircraftPos)
    aircraftECEFVel = Geo.ecefVelocities(aircraftPos, groundspeed, bearing)
    LOSSpeed = Geo.LOSSpeed(satelliteGeo['XYZ'], satelliteGeo['Velocity'], aircraftECEF, aircraftECEFVel)
    print(Geo.KmsToKnots(LOSSpeed), Geo.KmsToKnots(LOSSpeed) * 2.82)

print('Groundtruths')
for groundTruth in groundTruths:
    groundCheckGeoSat(groundTruth['AircraftSpeed'], groundTruth['AircraftTrack'], groundTruth['AircraftLatLon'])

def check(groundspeed, bearing, positions):
    print("Aircraft groundspeed: %f  Bearing: %f" % (groundspeed, bearing))
    for index, aircraftPos in enumerate(positions):
        aircraftECEF = Geo.sphericalToECEF(aircraftPos)
        aircraftECEFVel = Geo.ecefVelocities(aircraftPos, Geo.knotsToKms(groundspeed), bearing)
        LOSSpeed = Geo.LOSSpeed(satelliteInfos[index]['XYZ'], satelliteInfos[index]['Velocity'], aircraftECEF, aircraftECEFVel)
        pingRadius = Geo.greatCircleDistance(aircraftPos, satelliteInfos[index]['LatLon'])
        print(aircraftPos, Geo.KmsToKmh(LOSSpeed), Geo.KmsToKnots(LOSSpeed), Geo.kmToNm(pingRadius))

track1 = [(11.48182338, 95.43727392), (15.52284961, 95.55328146), (19.56393614, 95.66929072), (23.60509651, 95.7853021), (29.73435714, 95.9612575)]
check(242.7, 1.644, track1)

track2 = [(-2.63,93.67), (-10.52,92.29), (-18.42,90.91), (-26.32,89.52), (-38.33,87.42)]
check(481.0, 189.92, track2)

# Victor latest south track matching BFO
track3 = [(1.094,97.075), (-3.646,98.564), (-8.389,100.053), (-13.136,101.544), (-20.353,103.811)]
check(298.4, 162.56, track3)

# Victor latest north track matching BFO
track4 = [(11.743,95.841), (16.006,96.291), (20.271,96.740), (24.536,97.190), (31.008,97.873)]
check(257.4, 6.02, track4)

# GlobusMax digitized southern track
print('GlobusMax 454 Southern Check')
track5 = [(-3.28,93.25), (-10.67,91.68), (-18.18,90.72), (-25.71,90.10), (-37.13,88.91)]
lastBearing = 0.0
for index, pos in enumerate(track5):
    if index < len(track5)-1:
        bearing = Geo.bearing(pos, track5[index+1])
        lastBearing = bearing
    else:
        bearing = lastBearing

    aircraftECEF = Geo.sphericalToECEF(pos)
    aircraftECEFVel = Geo.ecefVelocities(pos, Geo.knotsToKms(454), bearing)
    LOSSpeed = Geo.LOSSpeed(satelliteInfos[index]['XYZ'], satelliteInfos[index]['Velocity'], aircraftECEF, aircraftECEFVel) * -1.0

    print(pos, bearing, Geo.kmToNm(Geo.greatCircleDistance(pos,satelliteInfos[index]['LatLon'])), Geo.KmsToKnots(LOSSpeed))

print('GlobusMax 394 Southern Check')
track6 = [(0.63,93.47), (-5.92,93.69), (-12.47,94.01), (-18.73,96.02), (-28.28,99.06)]
lastBearing = 0.0
for index, pos in enumerate(track6):
    if index < len(track6)-1:
        bearing = Geo.bearing(pos, track6[index+1])
        lastBearing = bearing
    else:
        bearing = lastBearing

    aircraftECEF = Geo.sphericalToECEF(pos)
    aircraftECEFVel = Geo.ecefVelocities(pos, Geo.knotsToKms(394), bearing)
    LOSSpeed = Geo.LOSSpeed(satelliteInfos[index]['XYZ'], satelliteInfos[index]['Velocity'], aircraftECEF, aircraftECEFVel) * -1.0

    print(pos, bearing, Geo.kmToNm(Geo.greatCircleDistance(pos,satelliteInfos[index]['LatLon'])), Geo.KmsToKnots(LOSSpeed))

print('Globus Stationary Aircraft')
track5 = [(-3.28,93.25), (-10.67,91.68), (-18.18,90.72), (-25.71,90.10), (-37.13,88.91)]
lastBearing = 0.0
for index, pos in enumerate(track5):
    if index < len(track5)-1:
        bearing = Geo.bearing(pos, track5[index+1])
        lastBearing = bearing
    else:
        bearing = lastBearing

    aircraftECEF = Geo.sphericalToECEF(pos)
    #aircraftECEFVel = Geo.ecefVelocities(pos, Geo.knotsToKms(454), bearing)
    aircraftECEFVel = (0.0, 0.0, 0.0)
    LOSSpeed = Geo.LOSSpeed(satelliteInfos[index]['XYZ'], satelliteInfos[index]['Velocity'], aircraftECEF, aircraftECEFVel) * -1.0

    print(pos, bearing, Geo.kmToNm(Geo.greatCircleDistance(pos,satelliteInfos[index]['LatLon'])), Geo.KmsToKnots(LOSSpeed))

print('GlobusMax 454 Southern Check - GeoStationary')
track5 = [(-3.28,93.25), (-10.67,91.68), (-18.18,90.72), (-25.71,90.10), (-37.13,88.91)]
lastBearing = 0.0
for index, pos in enumerate(track5):
    if index < len(track5)-1:
        bearing = Geo.bearing(pos, track5[index+1])
        lastBearing = bearing
    else:
        bearing = lastBearing

    aircraftECEF = Geo.sphericalToECEF(pos)
    aircraftECEFVel = Geo.ecefVelocities(pos, Geo.knotsToKms(454), bearing)
    LOSSpeed = Geo.LOSSpeed(satelliteGeo['XYZ'], satelliteGeo['Velocity'], aircraftECEF, aircraftECEFVel) * -1.0

    print(pos, bearing, Geo.KmsToKnots(LOSSpeed),  Geo.KmsToKnots(LOSSpeed) * 2.82)
