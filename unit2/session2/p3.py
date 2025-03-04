def navigate_research_station(station_layout, observations):
    totalTime = 0

    # create a dictionary of key = station layout identifier and value = 0-25 value
    # station layout string turns into dictionary
    listOfIndices = list(range(len(station_layout)))
    zipDict = dict(zip(station_layout, listOfIndices))
    #another way using enumerate
    zipDict2 = {station: index for index, station in enumerate(station_layout)}
    # print(zipDict)

    # create a list of values that show the distance between each letter from observations 
    # string provided
    previousStation = 0
    for station in observations:
        # print("which are we getting now- ", zipDict.get(station))
        totalTime += abs(zipDict.get(station) - previousStation)
        # print("tt- ",totalTime)
        previousStation = zipDict.get(station)
    # print(totalTime)


    return totalTime



station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))
