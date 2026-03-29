from api.weather.services.weather_api import get_weather

def main():

    location: str = input("Enter the City -> ")
    aqi: str = input("Do you want AQI ? (yes/no) ->  ")

    weather_data = get_weather(location, aqi)

    if weather_data:
        print(f"City -> {location}")
        print(f"Region->", weather_data["location"]["region"])
        print(f"Temperature (Celcius)", weather_data["current"]["temp_c"])
        if aqi == "yes":
            print(f"AQI ", weather_data["current"]["air_quality"])
    else:
        print("Could not fetch weather data.")

if __name__ == "__main__":
    main()
