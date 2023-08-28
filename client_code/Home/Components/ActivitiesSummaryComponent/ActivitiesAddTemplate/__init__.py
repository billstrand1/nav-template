from ._anvil_designer import ActivitiesAddTemplateTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..... import data_access
from ..... import navigation
from ..... import Globals
from datetime import datetime, timezone
from datetime import date
'''
Problem with New activity not showing up in summary, need to Update Globals somehow.
Also - check for 0:00 Time as an error
Also - check for more than one Category selected

'''

class ActivitiesAddTemplate(ActivitiesAddTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.activity_user = data_access.the_user()

    self.activity_title = ''
    self.activity_comments = ''
    self.activity_date_picker = None
    self.check_box_golf = None
    self.check_box_meals = None
    self.check_box_other = None
    today = date.today()
    self.input_activity_date_picker.min_date = today
  

  def button_add_activity_click(self, **event_args):
    self.label_error_msg.visible = False
    
    error = self.sync_data()
    if error:
      self.label_error_msg.text = error
      self.label_error_msg.visible = True      
      return

    print(f" ActivitiesAdd: time = {self.input_activity_date_picker.date.time()}")
    
    #From Petoskey-New:
    #Try update to remove tzinfo:
    print('removing tzinfo')
    activity_date = self.input_activity_date_picker.date
    print(f"before: {activity_date}")
    activity_date.astimezone(timezone.utc)
#     activity_date = activity_date.replace(tzinfo=None)
    print(f"after: {activity_date}")      
    
    anvil.server.call('add_activity', self.input_activity_title.text, 
                             self.input_activity_comments.text,
                             self.input_activity_date_picker.date,
                             self.input_check_box_golf.checked,
                             self.input_check_box_meals.checked, 
                             self.input_check_box_other.checked,
                             self.activity_user)
    
    Globals.all_activities, Globals.future_golf, Globals.future_dinners, Globals.future_other = anvil.server.call('get_all_future_activities')
#     Globals.all_activities, Globals.future_golf, Globals.future_dinners, Globals.future_other = anvil.server.launch_background_task('get_all_future_activities')
    
    navigation.go_activities()
  
  def sync_data(self):
    if not self.input_activity_title.text:
      return"Activity Venue Name is required."
    
    if not self.input_activity_date_picker.date:
      return"Date / Time is required.  Please note this is a 24 hour drop-down, and you must press the Apply button"
    
    if not self.input_check_box_golf.checked and not self.input_check_box_meals.checked and not self.input_check_box_other.checked:
      return"Please select a Category."
    
    if self.input_check_box_golf.checked and self.input_check_box_meals.checked:
      return "Please select ONLY 1 Category."
    
    if self.input_check_box_golf.checked and self.input_check_box_other.checked:
      return "Please select ONLY 1 Category."
    
    if self.input_check_box_meals.checked and self.input_check_box_other.checked:
      return "Please select ONLY 1 Category."
    
#     if not self.input_activity_date_picker.date:
#       return"Date / Time is required.  Please note this is a 24 hour drop-down, and you must press the Apply button"
    
    time_picked = self.input_activity_date_picker.date
    str_time_picked = time_picked.strftime('%H:%M:%S')
    if str_time_picked == '00:00:00':
      return "You selected Midnight.  Please note this is a 24 hour drop-down clock, and you must press the Apply button"
    
    return None
 

  def button_cancel_click(self, **event_args):
    navigation.go_activities()

