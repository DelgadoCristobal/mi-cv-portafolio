import urllib.request
import json

def get_weather():
    url = "https://wttr.in/Sevilla?format=j1"
    
    try:
        with urllib.request.urlopen(url) as response:
            if response.getcode() == 200:
                data = json.loads(response.read().decode())
                
                current = data['current_condition'][0]
                temp_c = current['temp_C']
                feels_like = current['FeelsLikeC']
                weather_desc = current['weatherDesc'][0]['value']
                
                print("="*30)
                print(f"🌍 CLIMA EN SEVILLA")
                print("="*30)
                print(f"🌡️  Temperatura:      {temp_c}°C")
                print(f"🔥 Sensación:        {feels_like}°C")
                print(f"☁️  Estado:           {weather_desc}")
                print("="*30)
            else:
                print(f"❌ Error al conectar con el servicio: {response.getcode()}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    get_weather()
