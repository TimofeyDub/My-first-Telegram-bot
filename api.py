import requests

def pogoda():
    try:
        #url
        url = "https://api.open-meteo.com/v1/forecast?latitude=60.015&longitude=30.646&current_weather=true"
        
        #данные
        response = requests.get(url)
        data = response.json()
        
        #температура
        temperature = data['current_weather']['temperature']
        
        #сообщение
        return f"Погода во Всеше: {temperature}°C"
        
    except Exception as e:
        print(f"Ошибка в api.py: {e}")
        return "😔 Не удалось получить погоду :("