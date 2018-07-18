import global_development
import matplotlib.pyplot as plt
list_of_report = global_development.get_reports()

unitedStates_data = []
nicaragua_data = []
years = []

for item in list_of_report:
    if item["Country"] == "United States":
        us_data = item["Data"]["Urban Development"]["Urban Population Percent Growth"]
        unitedStates_data.append(us_data)
        #print(item["Year"])
        year = item["Year"]
        years.append(year)
        print(us_data, year)
    if item["Country"] == "Nicaragua":
        nicaragua_data.append(item["Data"]["Urban Development"]["Urban Population Percent Growth"])


#print(len(unitedStates_data))
#print(unitedStates_data)

def countryData():
    bins = [.5, 1.0, 1.5, 2.0, 2.5]
    #years = [1980, 1990, 2000, 2005, 2010]
    plt.title("Urban Population Growth")
    plt.plot(years, unitedStates_data)
    plt.plot(years, nicaragua_data)
    #plt.plot(years,bins)
    #plt.ylim(0.5, 2.5)
    #plt.xlim(1980, 2010)
    # plt.plot(unitedStates_data)
    # plt.plot(nicaragua_data)5
    plt.xlabel("Years")
    plt.ylabel("Urban Growth Percentage")
    plt.show()

countryData()
