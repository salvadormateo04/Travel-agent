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

        print(f"\nThe official country name: {OfficialCountryName}")
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
    AmountOfCountries = input("How many countries will you visit")

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

