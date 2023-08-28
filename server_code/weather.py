import anvil.secrets
import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def get_weather_id():
  return anvil.secrets.get_secret('weather_api')

'''
From Example:

from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.http

class Form1(Form1Template):

  def __init__(self, **properties):
    self.init_components(**properties)

  def text_box_1_pressed_enter(self, **event_args):
    id = anvil.server.call('get_id')
    zipc=self.text_box_1.text
    json = anvil.http.request(
      f'https://api.openweathermap.org/data/2.5/weather?zip={zipc}&appid={id}&units=imperial',
      json=True
    )
    wind = json['wind']['speed']
    self.text_area_2.text = wind
    temp = json['main']['temp']
    self.text_area_3.text = temp




'''