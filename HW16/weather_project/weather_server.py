import datetime
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from urllib.parse import parse_qsl, urlparse
import requests
from database import *



def proccess_data(data:dict) -> tuple:
    Temp = data['main']['temp'] - 273.15
    feel_like = data['main']['feels_like'] - 273.15
    last_update = datetime.datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
    
    return Temp,feel_like,last_update

def get_city_weather(city_name: str,appid:str = "1f91529791d93931b93c4904d7b72865") -> dict:
    """
 Retrieve weather data from an external API for a given city.
 Args:
 - city_name (str): The name of the city to retrieve weather data for.
 Returns:
 - dict: A dictionary containing weather information for the city, includi
ng temperature, feels like temperature, and last updated time.
    """
    URL = "https://api.openweathermap.org/data/2.5/weather"
    PARAMS = {'q' :city_name ,'appid' :appid }
    request_time = datetime.datetime.now()
    try:
        
        response = requests.get(url= URL,params= PARAMS)
        
        if response.status_code == 200:
            last_update = datetime.datetime.fromtimestamp(response.json()['dt']).strftime('%Y-%m-%d %H:%M:%S')
            
            WeatherDatabase.save_request_data(city_name=city_name,request_time=str(request_time),request_status='200')
            WeatherDatabase.save_response_data(city_name=city_name,response_data=response.json())
            
            return proccess_data(response.json())
        else:
            WeatherDatabase.save_request_data(city_name=city_name,request_time=str(request_time),request_status='403')
            return '403'
    except BaseException as er:
        print(er)


class WebRequestHandler(BaseHTTPRequestHandler):
    # ...

    def do_GET(self) -> None:

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        url = urlparse(self.path)
        query = dict(parse_qsl(url.query))
        # print(url)
        # print(query)
        if url.path == '/weather/':
            self.wfile.write(self.weather_body(query['city_name']).encode("utf-8"))
        elif url.path == '/':
            self.wfile.write(self.main_body().encode("utf-8"))
        
    def weather_body(self,city):
        weather_data = get_city_weather(city)
        return f'''<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>Weather details of {city}</h1>
<p>Tempreture = {weather_data[0]}</p>
<p>like = {weather_data[1]}</p>
<p>Last update time = {weather_data[2]}</p>

</body>
</html> '''
    def main_body(self):
        return f'''<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>Mobin Davaji</h1>
<p>this is a http server for weatherapi</p>

</body>
</html> '''





def start_server() -> None:
    server = HTTPServer(("0.0.0.0", 8000), WebRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    
    start_server()