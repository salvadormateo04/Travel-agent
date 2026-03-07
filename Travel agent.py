import time
import requests
 
def CountrySearch():
    UserInput = input("Country: ").strip()
 
    url = f"https://restcountries.com/v3.1/name/{UserInput}"
    response = requests.get(url)
 
    if response.status_code == 200:
        data = response.json()[0]
 
        OfficialCountryName = data["name"]["official"]
        CapitalCity = data.get("capital", ["Unknown"])[0]
        region = data["region"]
        subregion = data["subregion"]
        Population = data["population"]
        Currency = data["currencies"]
        Languages = data["languages"]
        TimeZone = data["timezones"]
        CountryCode = data["cca2"]
        Location = data["capitalInfo"]["latlng"]
        LandStatus = data["landlocked"]
        borderingCountries = data.get("borders", [])
 
        print("The official country name:", OfficialCountryName)
        print("--------------------------")
        print("Capital city:", CapitalCity)
        print("--------------------------")
        print("Region and Sub Region:", region, "/", subregion)
        print("--------------------------")
        print("Population:", Population)
        print("--------------------------")
        print("Currency:", Currency)
        print("--------------------------")
        print("Languages:", Languages)
        print("--------------------------")
        print("Timezone:", TimeZone)
        print("--------------------------")
        print("Country code:", CountryCode)
        print("--------------------------")
        print("Coordinates:", Location)
        print("--------------------------")
        print("Landlocked country?:", LandStatus)
        print("--------------------------")
        print("Bordering countries:", borderingCountries)
 
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

    TravelDate = input("Estimated travel date: ")
    Notes = input("Notes or special requirements: ")

    DailyAccommodationCost = 100
    TransportationCost = 250
    AgencyFee = 150

    AccommodationCost = TotalDays * DailyAccommodationCost
    TotalCost = AccommodationCost + TransportationCost + AgencyFee

    print("Trip Summary")
    print("Client:", CustomerName)
    print("Countries visited:", AmountOfCountries)
    print("Total days:", TotalDays)
    print("Travel date:", TravelDate)
    print("Notes:", Notes)

    print("Total estimated trip cost:", TotalCost)
 
def Options():
    while True:

        print("Welcome to the teen T.I.T.A.N™ cruise agency")
        time.sleep(0.75)
        print("What would you like to do?")
        time.sleep(0.75)
        print("1. Search for a country, recieve its crucial information")
        print("2. Plan your trip today")
        print("3. Exit")

        option = input("What would you like to do: ")

        if option == "1":
            CountrySearch()

        elif option == "2":
            TripPlan()

        elif option == "3":
            print("Goodbye.")
            break

        else:
            print("Invalid option")
 
Options()