import requests
import time

def getInfo():
   url = "https://www.apicountries.com/countries"
   response = requests.get(url)
   if response.status_code == 200:
    info = response.json()
           
    print("Welcome to country finder 3000")
    time.sleep(0.5)
    print("Enter the country's name to recieve its crucial information")
    time.sleep(0.5)
    UserInput = input()

    OfficialCountryName = info["name"]
    CapitalCity = info["capital"]
    RegionSubRegion = info["region"]["subregion"]
    Population = info["population"]
    Currency = info["currency"]
    Languages = info["language"]
    TimeZone = info["timezone"]

    print(f"The official country name: {OfficialCountryName}")
    print("--------------------------")
    print(f"Capital city: {CapitalCity}")
    print("--------------------------")
    print(f"Region and Sub Region: {RegionSubRegion}")
    print("--------------------------")
    print(f"Population: {Population}")
    print("--------------------------")
    print(f"Currency: {Currency}")
    print("--------------------------")
    print(f"Languages: {Languages}")
    print("--------------------------")
    print(f"Timezone: {TimeZone}")

getInfo()

