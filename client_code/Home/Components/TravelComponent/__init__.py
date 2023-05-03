from ._anvil_designer import TravelComponentTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .... import navigation
from .... import data_access

from .TravelAdd import TravelAdd

#  Need to  find out why last update didn't save
#  Test if user or spouse, then have them delete before adding.


class TravelComponent(TravelComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)    
    
    #Name Label on the Main Form
    print('calling the_user from TravelComponent')
    user = data_access.the_user()
    print(user['first_name'])
    form = navigation.get_form()    
    if user:
      form.label_name.text = 'Hi ' + user['first_name'] + ', '
      
    self.refresh_data_bindings()
    travel_summary = anvil.server.call('get_travel_from_dt')
    self.repeating_panel_travel.items = travel_summary
    self.repeating_panel_travel.set_event_handler('x-delete-schedule', self.delete_schedule)

  def delete_schedule(self, schedule, **event_args):
      #call data_access function test....
    
      anvil.server.call('delete_schedule', schedule)
      self.repeating_panel_travel.items = anvil.server.call('get_travel_from_dt')

  def btn_add_travel_click(self, **event_args):
    print('self.btn_add_travel_click called')
    user = data_access.the_user()

    # FROM ACTIVITIES
    #Give this a try:
    if user['spouse']:
      spouse = user['spouse']
    else: spouse = None
    either_user_or_spouse = app_tables.travel.search(participant=q.any_of(user, spouse))
    if len(either_user_or_spouse) > 0:
      print('either_user_or_spouse > 0 in TRAVEL: CLIENT CODE')
      print('Couple already HAS TRAVEL PLANS')
      message = "You or your spouse have already entered your travel dates, please delete and re-enter if you'd like to make a change."
      alert(message)
      return     
    #----end of Try


    #END FROMN ACTIVITIES

    
    form = navigation.get_form()
    form.load_component(TravelAdd())

    
    self.refresh_data_bindings()
    self.repeating_panel_travel.items = anvil.server.call('get_travel_from_dt')

        
    
    
    pass

  