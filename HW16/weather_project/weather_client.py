from weather_server import get_city_weather
from database import WeatherDatabase


def start_client() -> str:
    
    try:
        while True:
            city_name = input("Enter a city name(or quit for exit): ")
            if city_name == 'quit':
                break
            data_weather = get_city_weather(city_name)
            if data_weather == '403':
                print('Error retrieving weather data: No matching location found. ')
                city_name = input("Enter a new city name: ")
                data_weather = get_city_weather(city_name)
                print('Temperature: %.2f\nFeels like: %.2f\nLast updated: %s' % (data_weather[0],data_weather[1],data_weather[2]))
            else:
                print('Temperature: %.2f\nFeels like: %.2f\nLast updated: %s' % (data_weather[0],data_weather[1],data_weather[2]))
    except BaseException as e:
        print(e)

def request_details() -> str:
    return f'Request count: {WeatherDatabase.get_request_count()}\nSuccessful request count: {WeatherDatabase.get_successful_request_count()}\nCity request counts: \n{WeatherDatabase.get_city_request_count()}'
        
if __name__ == '__main__':
    start_client()
    print(request_details())