from ._anvil_designer import HomeDetailsComponentTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import navigation
from ... import data_access
from datetime import datetime
from datetime import date
from ... import Globals
# import pandas as pd

class HomeDetailsComponent(HomeDetailsComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
    self.label_travel_entry.text = None
    self.label_activities.text = None
    self.label_activities_detail.text = None
    
    #Name Label on the Main Form
    user = data_access.the_user()
    form = navigation.get_form()    
    if user:
      form.label_name.text = 'Hi ' + user['first_name'] + ', '


    #----Get Couple's Travel Info,.
    if user['spouse']:
      spouse = user['spouse']
    else: spouse = None
    either_user_or_spouse_travel = app_tables.travel.search(participant=q.any_of(user, spouse))
    if len(either_user_or_spouse_travel) > 0:
      for info in either_user_or_spouse_travel:
        arrive = info['arrive']
        arrive_text = arrive.strftime("%a %b %d '%y")
        depart = info['depart']
        depart_text = depart.strftime("%a %b %d '%y")
        print('Couple or Single already HAS TRAVEL PLANS')
        message = f"You are scheduled to arrive {arrive_text} and depart {depart_text}."
    else:
      message = 'You have not entered your travel plans yet, if you have them, please add them on the Travel link.'
    self.label_travel_entry.text = message
    
    #----Get Couple's Activities Info,.
    
    activities_message_1, activities_message_2 = anvil.server.call('get_user_or_spouse_activities_str', user, spouse)
    self.label_activities.text = activities_message_1
    self.label_activities_detail.text = activities_message_2
    
    self.label_all_activitites.text = anvil.server.call('get_all_activities_and_participants')

    
    
      
    