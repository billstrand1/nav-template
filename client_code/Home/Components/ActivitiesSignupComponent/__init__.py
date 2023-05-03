from ._anvil_designer import ActivitiesSignupComponentTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .... import navigation
from .... import data_access
from .... import Globals

from .FutureActivitiesSignupTemplate import FutureActivitiesSignupTemplate


class ActivitiesSignupComponent(ActivitiesSignupComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    #Name Label on the Main Form
    user = data_access.the_user()
    form = navigation.get_form()
    if user:
      form.label_name.text = 'Hi ' + user['first_name'] + ', '
    
    self.refresh_data_bindings()
    self.repeating_panel_activites.items = Globals.all_future_activities 


  #------------------------WORKING ON EDIT / DELETE / REFRESH-------------
  def refresh_activities(self, **event_args):
    print('refresh_activities called')
    #update should be done in server code:  CANNOT RUN GLOBALS IN SERVER CODE.
    self.refresh_data_bindings()
    Globals.all_future_activities, Globals.future_golf, Globals.future_dinners, Globals.future_other = anvil.server.call('get_all_future_activities')
    self.repeating_panel_activites.items = Globals.all_future_activities
    

  #------------------------CORRECT / TESTED METHODS BELOW-------------

  def link_golf_click(self, **event_args):
#       print('golf only')
      self.repeating_panel_activites.items = Globals.future_golf


  def link_dinner_click(self, **event_args):
#       print('meals only')
      self.repeating_panel_activites.items = Globals.future_dinners
       

  def link_other_click(self, **event_args):
#       print('other only')
      self.repeating_panel_activites.items = Globals.future_other

 
  def link_all_click(self, **event_args):
#      print('all activities')
     self.repeating_panel_activites.items = Globals.all_future_activities

  
  def outlined_button_1_click(self, **event_args):
    navigation.go_activities()







