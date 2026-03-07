import time
import requests

def CountrySearch():
    
    print("Welcome to THE travel agency")
    time.sleep(0.5)
    print("What would you like to do?")
    time.sleep(0.5)
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
        Weather = data[""]
        CurrentLocalTime = data[""]
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
        print(f"Weather: {Weather}")
        print("--------------------------")
        print(f"Current local time: {CurrentLocalTime}")
        print("--------------------------")
        print(f"Current local time: {LandStatus}")
        print("--------------------------")
        print(f"Current local time: {borderingCountries}")

    else:
        print("Error: Could not fetch the data.")

CountrySearch()
    

