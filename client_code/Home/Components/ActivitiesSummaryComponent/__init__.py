from ._anvil_designer import ActivitiesSummaryComponentTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .... import navigation
from .... import data_access
from .... import Globals

from .ActivitiesAddTemplate import ActivitiesAddTemplate


class ActivitiesSummaryComponent(ActivitiesSummaryComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    #Name Label on the Main Form
    user = data_access.the_user()
    form = navigation.get_form()
    if user:
      form.label_name.text = 'Hi ' + user['first_name'] + ', '
    print(user['first_name'])
    self.refresh_data_bindings()
    
#     Globals.all_future_activities, Globals.future_golf, Globals.future_dinners, Globals.future_other = anvil.server.call('get_all_future_activities')
    self.repeating_panel_activites.items = Globals.all_future_activities 

    self.repeating_panel_activites.set_event_handler('x-delete-activity', self.delete_activity)
    self.repeating_panel_activites.set_event_handler('x-edit-activity', self.edit_activity)

  #------------------------WORKING ON EDIT / DELETE / REFRESH-------------
  def refresh_activities(self, **event_args):
    print('ActivitiesSummaryComponent refresh_activities called')
    self.refresh_data_bindings()
    Globals.all_future_activities, Globals.future_golf, Globals.future_dinners, Globals.future_other = anvil.server.call('get_all_future_activities')
    self.repeating_panel_activites.items = Globals.all_future_activities
    
    
  def delete_activity(self, activity, **event_args):
    print('ActivitiesSummaryComponent delete_activity called')
    anvil.server.call('delete_activity', activity)
    self.refresh_activities()
    
    
  def edit_activity(self, activity, **event_args):
    #call data_access function
    print('ActivitiesSummaryComponent edit_activity called')
#     anvil.server.call('edit_activity', activity, activity_dict)      
    self.refresh_activities()
      
  #------------------------WORKING ON EDIT / DELETE / REFRESH-------------

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


      
  def switch_1_change(self, **event_args):
    if self.switch_1.checked:
      print('Switch True')
      self.repeating_panel_past_activites.items = Globals.all_past_activities
      self.label_past_activities.visibility=True
      self.card_past_activities.visible=True
    else:
      print('Switch False')
      self.label_past_activities.visibility=False
      self.card_past_activities.visible=False
      

  def button_add_click(self, **event_args):
    print('ActivitiesSummaryComponent button_add_click called')    
    form = navigation.get_form()
    form.load_component(ActivitiesAddTemplate())
    
#       navigation.go_activities_add()

  def button_signup_click(self, **event_args):
    navigation.go_activities_signup()







