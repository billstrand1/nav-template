from ._anvil_designer import TravelAddTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..... import data_access
from ..... import navigation
# from .... import data_access

class TravelAdd(TravelAddTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    user = data_access.the_user()
    self.input_travel_arrive.date = None
    self.input_travel_depart.date = None
    self.label_error_msg.text = ''
    self.label_travellers.text = user['couple_name']        

  def button_add_travel_click(self, **event_args):
#         form.load_component(ActivitiesAddTemplate())

    user = data_access.the_user()
    self.label_error_msg.visible = False    
    error = self.sync_data()
    if error:
      self.label_error_msg.text = error
      self.label_error_msg.visible = True      
      return
    
    message = anvil.server.call('add_travel_schedule', user, self.input_travel_arrive.date, self.input_travel_depart.date)
    alert(content = message)
    navigation.go_travel()
  
  def sync_data(self):    
    if not self.input_travel_arrive.date:
      return "Arrival Date is required."
    
    if not self.input_travel_depart.date:
      return "Departure Date is required."
    
    if self.input_travel_arrive.date > self.input_travel_depart.date:
      return "Arrival date must be before Departure date."
    
    return None


