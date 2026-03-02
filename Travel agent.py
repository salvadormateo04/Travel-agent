import requests
import time

def getInfo():
    url = "https://www.apicountries.com/countries"
    response = requests.get(url)
    
    if response.status_code == 200:
        allCountries = response.json()  
        
        print("Welcome to THE travel agency")
        time.sleep(0.5)
        print("Enter the country's name to receive its crucial information")
        time.sleep(0.5)
        UserInput = input("Country: ").strip().lower()
        
        FoundCountry = None
        for country in allCountries:
            countryName = country.get("name", "").lower()
            if UserInput in countryName.lower() or countryName in UserInput.lower():
                FoundCountry = country
                break
        
        if FoundCountry:
            OfficialCountryName = FoundCountry.get("name", "N/A")
            CapitalCity = FoundCountry.get("capital", "N/A")
            region = FoundCountry.get("region", "N/A")
            subregion = FoundCountry.get("subregion", "N/A")
            RegionSubRegion = f"{region} / {subregion}"
            Population = FoundCountry.get("population", "N/A")
            Currency = FoundCountry.get("currency", "N/A")
            Languages = FoundCountry.get("language", "N/A")
            TimeZone = FoundCountry.get("timezone", "N/A")
            
            print(f"\nThe official country name: {OfficialCountryName}")
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
        else:
            print(f"Country '{UserInput}' not found!")
    else:
        print(f"Error: Could not fetch data. Status code: {response.status_code}")

getInfo()