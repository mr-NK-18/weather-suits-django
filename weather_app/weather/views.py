from django.shortcuts import render
import requests

def get_outfit_suggestion(temp, condition):
    # For conditions that require temperature-specific recommendations
    if temp is not None:
        # Check for temperature ranges
        if temp < 0:
            temp_feeling = "It's freezing! Bundle up with warm layers, gloves, and a coat."
        elif 0 <= temp < 10:
            temp_feeling = "It's quite chilly. Wear warm layers, a jacket, and gloves."
        elif 10 <= temp < 20:
            temp_feeling = "It's a bit chilly, a light jacket or sweater will do."
        elif 20 <= temp < 30:
            temp_feeling = "It's warm. Light clothing is recommended."
        else:
            temp_feeling = "It's hot. Wear light, breathable clothing, and stay hydrated."
    else:
        temp_feeling = "Temperature data is unclear."

    # Now handle the weather conditions, giving more specific suggestions
    if condition == "Clear":
        if temp > 30:
            return "Wear sunglasses, light clothes, and sunscreen."
        elif 20 < temp <= 30:
            return "Comfortable light clothing is recommended."
        elif 10 < temp <= 20:
            return "Wear a light jacket."
        elif temp == 0:
            return "It's freezing! Bundle up with warm layers and a coat."
        else:
            return "It's cold. Wear warm clothing, gloves, and a jacket."

    elif condition == "Clouds":
        # Handle clouds condition with the temperature range
        if temp > 20:
            return "Comfortable light clothing is recommended with a light jacket."
        elif 10 <= temp <= 20:
            return "Wear a light jacket or sweater."
        elif 0 <= temp < 10:
            return "Wear warm layers and a coat."
        else:
            return "It's freezing! Bundle up with heavy layers and gloves."

    elif condition == "Rain":
        if temp > 20:
            return "Carry an umbrella and wear a raincoat."
        else:
            return "Wear a warm waterproof jacket and boots."

    elif condition == "Drizzle":
        return "Light raincoat or umbrella."

    elif condition == "Snow":
        return "Bundle up with a heavy jacket, gloves, and boots."

    elif condition == "Windy":
        if temp > 20:
            return "Wear a windbreaker and secure your hat."
        else:
            return "Wear warm clothes and a windproof jacket."

    elif condition == "Thunderstorm":
        return "Avoid going outside. Stay safe indoors."

    elif condition == "Extreme Heat":
        return "Loose cotton clothes, wide-brim hat, sunglasses."

    elif condition == "Extreme Cold":
        return "Multiple warm layers, gloves, wool cap."

    elif condition == "Haze":
        if temp > 30:
            return "The air is hazy and hot. Wear light clothing, but protect your eyes and stay hydrated."
        elif temp > 20:
            return "Hazy conditions with moderate temperatures. Wear a mask if sensitive to air quality, and light layers."
        else:
            return "Haze and chilly weather. Dress warmly, but consider wearing a scarf or mask for air quality."

    elif condition == "Mist":
        return "Light layers; avoid wearing dark colors, carry an umbrella if necessary."

    elif condition == "Tornado":
        return "Stay indoors, find a safe location away from windows. Wear sturdy shoes and cover your head with a cushion or helmet if required."

    elif condition == "Sleet":
        return "Waterproof jacket, boots, gloves, and hat. Consider a scarf to protect from cold winds."

    elif condition == "Dust Storm":
        return "Protective face mask, goggles, long sleeves, sturdy shoes. Avoid exposure to the outdoors."

    elif condition == "Overcast":
        return "Light jacket or layers; might want an umbrella if there’s a chance of rain."

    elif condition == "Humidity":
        return "Light, breathable clothing like cotton or linen. Stay hydrated, and avoid tight clothing."

    elif condition == "Freezing Rain":
        return "Wear warm, waterproof outer layers. Ensure footwear is non-slip for icy surfaces."

    elif condition == "Partly Cloudy":
        return "Light layers; sunglasses recommended for sun exposure."

    elif condition == "Cold Front":
        return "Warm jacket, gloves, and boots. Consider layering."

    elif condition == "Heat Index":
        return "Lightweight and breathable clothing, sunscreen, hat, and sunglasses."

    elif condition == "Mild Weather":
        return "Comfortable clothing; light jacket or sweater, depending on preference."

    elif condition == "High Wind Chill":
        return "Insulated jacket, warm layers, gloves, and hat to protect against cold wind."

    elif condition == "Heavy Showers":
        return "Waterproof rain gear, waterproof footwear, and an umbrella."

    elif condition == "Gale":
        return "Wear a windbreaker or heavy-duty jacket with secure fastenings, avoid loose items that could fly away."

    # New additional weather conditions:
    elif condition == "Polar Night":
        return "Multiple warm layers, thermal wear, winter gear. Stay in well-heated areas when possible."

    elif condition == "Polar Day":
        return "Light, breathable clothing, sunscreen, hat, sunglasses. Be cautious of sun exposure for extended periods."

    elif condition == "Tsunami":
        return "Stay indoors, evacuate to higher ground, wear sturdy shoes."

    elif condition == "Volcanic Ash":
        return "Wear a face mask, goggles, long sleeves, and protective boots."

    elif condition == "Acid Rain":
        return "Protective clothing and gear, avoid contact with skin."

    elif condition == "Frost":
        return "Layer up in warm clothing, wear gloves and insulated boots."

    elif condition == "Drought":
        return "Light clothing, carry extra water, avoid direct sun exposure."

    elif condition == "Monsoon":
        return "Raincoat, waterproof footwear, carry an umbrella."

    elif condition == "Cyclone":
        return "Stay indoors, secure windows, and avoid going outside. Waterproof gear if necessary."

    elif condition == "Hurricane":
        return "Stay indoors, avoid windows. Waterproof gear if necessary when leaving."

    elif condition == "Dust Devil":
        return "Protective face mask, light clothing, avoid open spaces."

    elif condition == "Heatwave":
        return "Lightweight clothing, sunscreen, hat, sunglasses, and stay hydrated."

    elif condition == "Funnel Cloud":
        return "Take shelter, stay away from windows, and protect your head."

    else:
        return "Weather data is unclear. Dress appropriately for the season."

def weather_view(request):
    weather_class = "default"  # Default class if no valid weather condition is found
    temp_feeling = ""  # Default string for temperature feedback
    api_key = 'a3c606a4018a2f405b8f81da0ff6874c'
    city = request.GET.get('city')

    if city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()

                # Check if expected keys are in the response
                if 'main' in data and 'weather' in data:
                    temp = data['main'].get('temp', None)
                    weather_condition = data['weather'][0].get('main', 'Unknown')

                    # Determine weather_class based on condition
                    if weather_condition == 'Clear':
                        weather_class = 'sunny'
                    elif weather_condition == 'Rain':
                        weather_class = 'rainy'
                    elif weather_condition == 'Clouds':
                        weather_class = 'cloudy'
                    elif weather_condition == 'Snow':
                        weather_class = 'snowy'
                    elif weather_condition == 'Thunderstorm':
                        weather_class = 'stormy'
                    elif weather_condition == 'Mist':
                        weather_class = 'misty'
                    else:
                        weather_class = 'default'  # For any other conditions

                    # Determine temperature feedback based on temperature
                    if temp is not None:
                        if temp < 0:
                            temp_feeling = "It's freezing cold! Be careful of frost and ice."
                        elif temp == 0:
                            temp_feeling = "It's exactly 0°C! Prepare for freezing temperatures."
                        elif temp < 15:
                            temp_feeling = "It's quite chilly. Dress warmly."
                        else:
                            temp_feeling = "It's warm, but be ready for possible changes in weather."

                    # Use the `get_outfit_suggestion` function for outfit advice
                    outfit = get_outfit_suggestion(temp, weather_condition)

                    context = {
                        'city': city,
                        'temp': temp,
                        'weather_condition': weather_condition,
                        'outfit': outfit,
                        'weather_class': weather_class,
                        'temp_feeling': temp_feeling  # Add this to show temperature feedback
                    }
                    return render(request, 'weather/weather.html', context)
                else:
                    context = {'error': 'Unexpected data format from weather API.'}
                    return render(request, 'weather/weather.html', context)

            else:
                context = {'error': 'Could not retrieve weather for the city. Please check the city name.'}
                return render(request, 'weather/weather.html', context)
        except requests.exceptions.RequestException as e:
            context = {'error': f"An error occurred while fetching the weather: {e}"}
            return render(request, 'weather/weather.html', context)

    return render(request, 'weather/weather.html')
