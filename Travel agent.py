import time
import requests
 
def CountrySearch():
    UserInput = input("Country: ").strip()
 
    url = f"https://restcountries.com/v3.1/name/{UserInput}"
    response = requests.get(url)
 
    if response.status_code == 200:
        data = response.json()[0]
 
        OfficialCountryName = data["name"]["official"]
        CapitalCity = data["capital"]
        region = data["region"]
        subregion = data["subregion"]
        Population = data["population"]
        Currency = data["currencies"]
        Languages = data["languages"]
        TimeZone = data["timezones"]
        CountryCode = data["cca2"]
        Location = data["capitalInfo"]["latlng"]
        LandStatus = data["landlocked"]
        borderingCountries = data["borders"]
 
        print(f"The official country name: {OfficialCountryName}")
        print("--------------------------")
        print(f"Capital city: {CapitalCity}")
        print("--------------------------")
        print(f"Region and Sub Region: {region} / {subregion}")
        print("--------------------------")
        print(f"Population: {Population}")
        print("--------------------------")
        print(f"Currency: {Currency}")
        print("--------------------------")
        print(f"Languages: {Languages}")
        print("--------------------------")
        print(f"Timezone: {TimeZone}")
        print("--------------------------")
        print(f"Country code: {CountryCode}")
        print("--------------------------")
        print(f"Coordinates: {Location}")
        print("--------------------------")
        print(f"Landlocked country?: {LandStatus}")
        print("--------------------------")
        print(f"Bordering countries: {borderingCountries}")
 
    else:
        print("Error: Could not fetch the data.")
 
def TripPlan():
 
    print("Plan your trip")
    time.sleep(0.75)

    CustomerName = input("What is your name?: ")
    AmountOfCountries = input("How many countries will you visit: ")

    Country1 = input("Enter first country: ")
    Days1 = int(input("How many days will you stay there?: "))

    Country2 = input("Enter second country: ")
    Days2 = int(input("How many days will you stay there?: "))

    TravelDate = input("Estimated travel date: ")
    Notes = input("Notes or special requirements: ")

    DailyAccommodationCost = 100
    TransportationCost = 250
    AgencyFee = 150

    TotalDays = Days1 + Days2
    AccommodationCost = TotalDays * DailyAccommodationCost
    TotalCost = AccommodationCost + TransportationCost + AgencyFee

    print("Trip Summary")
    print("--------------------------")
    print("Client name:", CustomerName)
    print("Countries:", Country1, "and", Country2)
    print("Days:", Days1, "and", Days2)
    print("Travel date:", TravelDate)
    print("Notes:", Notes)

    print("Cost Estimation")
    print("--------------------------")
    print("Accommodation cost:", AccommodationCost)
    print("Transportation cost:", TransportationCost)
    print("Agency fee:", AgencyFee)
    print("Total estimated trip cost:", TotalCost)
 
def Options():
    print("Welcome to the teen T.I.T.A.N™ cruise agency")
    time.sleep(0.75)
    print("What would you like to do?")
    time.sleep(0.75)
    print("1. Search for a country, recieve its crucial information")
    print("2. Plan your trip today")
 
    option = input("What would you like to do")
 
    if option == "1":
        CountrySearch()
 
    if option == "2":
        TripPlan()
 
    else:
        print("Invalid option")
 
Options()