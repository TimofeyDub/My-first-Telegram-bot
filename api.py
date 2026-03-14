import requests
from datetime import datetime

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
        return f"Погода во Всеше: Всегда ясно, {temperature}°C"
        
    except Exception as e:
        print(f"Ошибка в api.py: {e}")
        return "😔 Не удалось получить погоду :("
    
def pogoda2():
    try:
        #url
        url = "https://api.open-meteo.com/v1/forecast?latitude=39.4739&longitude=-0.3797&hourly=temperature_2m"
        
        #данные
        response = requests.get(url)
        data = response.json()
        
        #текущее время там
        current_time = datetime.utcnow().strftime("%Y-%m-%dT%H:00")
        
        #индекс текущего часа
        time_list = data['hourly']['time']
        temp_list = data['hourly']['temperature_2m']
        
        #текущее время в массиве
        if current_time in time_list:
            index = time_list.index(current_time)
            temperature = temp_list[index]
        else:
            temperature = temp_list[0]
        
        #сообщение
        return f"Погода в Валенсии: Всегда ясно, {temperature}°C"
        
    except Exception as e:
        print(f"Ошибка в api.py: {e}")
        return "😔 Не удалось получить погоду :("

def pogoda3():
    try:
        #url
        url = "https://api.open-meteo.com/v1/forecast?latitude=41.2647&longitude=69.2163&hourly=temperature_2m"
        
        #данные
        response = requests.get(url)
        data = response.json()
        
        #текущее время там
        current_time = datetime.utcnow().strftime("%Y-%m-%dT%H:00")
        
        #индекс текущего часа
        time_list = data['hourly']['time']
        temp_list = data['hourly']['temperature_2m']
        
        #текущее время в массиве
        if current_time in time_list:
            index = time_list.index(current_time)
            temperature = temp_list[index]
        else:
            temperature = temp_list[0]
        
        #сообщение
        return f"Погода в Ташкенте: Всегда ясно, {temperature}°C"
        
    except Exception as e:
        print(f"Ошибка в api.py: {e}")
        return "😔 Не удалось получить погоду :("

def pogoda4():
    try:
        #url
        url = "https://api.open-meteo.com/v1/forecast?latitude=38.8951&longitude=-77.0364&hourly=temperature_2m"
        
        #данные
        response = requests.get(url)
        data = response.json()
        
        #текущее время там
        current_time = datetime.utcnow().strftime("%Y-%m-%dT%H:00")
        
        #индекс текущего часа
        time_list = data['hourly']['time']
        temp_list = data['hourly']['temperature_2m']
        
        #текущее время в массиве
        if current_time in time_list:
            index = time_list.index(current_time)
            temperature = temp_list[index]
        else:
            temperature = temp_list[0]
        
        #сообщение
        return f"Погода в Washington, DC: Всегда ясно, {temperature}°C"
        
    except Exception as e:
        print(f"Ошибка в api.py: {e}")
        return "😔 Не удалось получить погоду :("