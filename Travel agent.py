import time
import requests
import random

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

        print(f"\nThe official country name: {OfficialCountryName}")
        print("--------------------------")
        print(f"The capital city: {CapitalCity}")
        print("--------------------------")
        print(f"The region and Sub Region: {region} / {subregion}")
        print("--------------------------")
        print(f"The Population: {Population}")
        print("--------------------------")
        print(f"The Currency: {Currency}")
        print("--------------------------")
        print(f"The Languages: {Languages}")
        print("--------------------------")
        print(f"The Timezone: {TimeZone}")
        print("--------------------------")
        print(f"The Country code: {CountryCode}")
        print("--------------------------")
        print(f"The Coordinates: {Location}")
        print("--------------------------")
        print(f"Is it a Landlocked country?: {LandStatus}")
        print("--------------------------")
        print(f"Bordering countries: {borderingCountries}")
        print("--------------------------")

    else:
        print("Error: Could not fetch the data.")

def TripPlan():
    print("Plan your trip")
    time.sleep(0.75)
 
    CustomerName = input("What is your name?: ")
    AmountOfCountries = int(input("How many countries will you visit: "))
 
    TotalDays = 0
 
    for country in range(AmountOfCountries):
        Country = input("Enter a country: ")
        Days = int(input("How many days will you stay there?: "))
        TotalDays = TotalDays + Days
 
    print("--------------------------")
    TravelDate = input("Estimated travel date in day/month/year: ")
    print("--------------------------")
    Notes = input("Notes or special requirements: ")
    print("--------------------------")
 
    DailyAccommodationCost = random.randint(100,200)
    TransportationCost = random.randint(250,500)
    AgencyFee = random.randint(150,300)
 
    AccommodationCost = TotalDays * DailyAccommodationCost
    TotalCost = AccommodationCost + TransportationCost + AgencyFee
 
    print("--------------------------")
    print("Trip Summary")
    print("--------------------------")
    print("Client's name:", CustomerName)
    print("--------------------------")
    print("Countries:", AmountOfCountries)
    print("--------------------------")
    print("Total days:", TotalDays)
    print("--------------------------")
    print("Travel date:", TravelDate)
    print("--------------------------")
    print("Notes:", Notes)
    print("--------------------------")
    print("Total estimated trip cost in dollars, Enjoy:", TotalCost)
    print("--------------------------")
 
def Options():
    while True:
        
        print("--------------------------")
        print("Welcome to the T.I.T.A.N™ Travel agency")
        time.sleep(0.75)
        print("--------------------------")
        print("What would you like to do?")
        print("--------------------------")
        time.sleep(0.75)
        print("1. Search for a country, recieve its crucial information")
        print("--------------------------")
        print("2. Plan your trip today")
        print("--------------------------")
        print("3. Exit")
        print("--------------------------")

 
        option = input("What would you like to do: ")
        print("--------------------------")
 
        if option == "1":
            CountrySearch()
 
        elif option == "2":
            TripPlan()

        elif option == "3":
            print("Goodbye and thank you for using T.I.T.A.N travel agency.")
            break
 
        else:
            print("Invalid option")
 
Options()