from typing import List
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from typing import List, Tuple
import datetime
from sqlalchemy import select,TIMESTAMP,Column
from sqlalchemy import func, desc
from datetime import timedelta


class Base(DeclarativeBase):
    pass


class request(Base):

    __tablename__ = "request"
    count: Mapped[int] = mapped_column(primary_key=True)
    city_name: Mapped[str] = mapped_column(String(30))
    request_time: Mapped[str]
    status: Mapped[str]


    def __repr__(self) -> str:
        return f"request(count={self.count!r}, city_name={self.city_name!r}, request_time={self.request_time!r})"


class response(Base):
    __tablename__ = "response"
    id: Mapped[int] = mapped_column(primary_key=True)
    City_name: Mapped[str] = mapped_column(String(30))
    Tempreture: Mapped[float]
    Feels_like: Mapped[float]
    Last_update: Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"response(id={self.id!r}, City_name={self.City_name!r}, Tempreture={self.Tempreture!r}, Feels_like={self.Feels_like!r}, Last_update={self.Last_update!r})"


engine = create_engine("sqlite:////home/mobin/HW/MobinHajiliDavaji_hw_maktab116/HW16/weather_project/weather.sqlite3",echo = False)
Base.metadata.create_all(engine)

# engine = Session

class WeatherDatabase:
    def __init__(self):
        """
        Initialize a new WeatherDatabase instance.
        """
        pass
    @classmethod
    def save_request_data(cls,city_name: str, request_time: str,request_status) -> None:
        """
        Save request data for a city to the database.
        Args:
        - city_name (str): The name of the city to save request data for.
        - request_time (str): The time the request was made, in ISO format.
        Returns:
        - None
        """

        with Session(engine) as session:
            weather_request = request(
                city_name=city_name,
                request_time=request_time,
                status=request_status
            )

            session.add_all([weather_request])
            session.commit()
    @classmethod
    def save_response_data(cls, city_name: str, response_data: dict) -> None:
        """
        Save response data for a city to the database.
        Args:
        - city_name (str): The name of the city to save response data for.
        - response_data (dict): A dictionary containing weather information for the city, incl
        uding temperature, feels like temperature, and last updated time.
        Returns:
        - None
        """
        pass

        with Session(engine) as session:

            weather_response = response(
                City_name=city_name,
                Tempreture=response_data['main']["temp"],
                Feels_like=response_data['main']["feels_like"],
                Last_update=datetime.datetime.fromtimestamp(response_data['dt']).strftime('%Y-%m-%d %H:%M:%S'),
            )

            session.add_all([weather_response])
            session.commit()
    @classmethod
    def get_request_count(cls) -> int:
        """
        Get the total number of requests made to the server.
        Returns:
        - int: The total number of requests made to the server.
        """
 
        session = Session(engine)
        
        stmt = select(func.max(request.count)).select_from(request)

        return session.scalars(stmt).one()
        
    @classmethod
    def get_successful_request_count(cls) -> int:
        """
        Get the total number of successful requests made to the server.
        Returns:
        - int: The total number of successful requests made to the server.
        """
        session = Session(engine)
        
        stmt = select(func.count('*')).where(request.status == '200')

        return session.scalars(stmt).one()
    @classmethod
    def get_last_hour_requests(cls) -> List[Tuple[str, str]]:
        """
        Get a list of requests made in the last hour.
        Returns:
        - List[Tuple[str, str]]: A list of tuples containing the name of the city and the time
        the request was made, in ISO format.
        """
        pass

        # with engine.connect() as conn:
        #     result = conn.execute(
        #     select(request.city_name, request.request_time)
        #     .where(func.now() func.)
        # )
        #     print(result.all())
        now = datetime.datetime.now()
        one_hours_ago = now - timedelta(hours=1)
        session = Session(engine)
        stmt = session.query(request).filter(request.request_time > one_hours_ago).all()
        # print(stmt)
        
    @classmethod
    def get_city_request_count(cls) -> List[Tuple[str, int]]:
        """
        Get a count of requests made for each city.
        Returns:
        - List[Tuple[str, int]]: A list of tuples containing the name of the city and the numb
        er of requests made for that city.
        """
        pass

        with engine.connect() as conn:
            result = conn.execute(
            select(request.city_name,func.count('*'))
            .group_by(request.city_name)
        )
            return result.all()

        
# print(WeatherDatabase.get_city_request_count())
# print(WeatherDatabase.get_request_count())
# print(WeatherDatabase.get_successful_request_count())
