from ._anvil_designer import FutureActivitiesSignupTemplateTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..... import navigation
from ..... import data_access
from ..... import Globals

class FutureActivitiesSignupTemplate(FutureActivitiesSignupTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
       
    user = data_access.the_user()    
    self.repeating_panel_participants.items = anvil.server.call('get_participants_in_activity', self.item)
    self.repeating_panel_participants.set_event_handler('x-update-panel', self.update_panel)

  def update_panel(self, **event_args):
    print('update_panel called')
    self.refresh_data_bindings()
    self.repeating_panel_participants.items = anvil.server.call('get_participants_in_activity', self.item)
    

  def link_signup_click(self, **event_args):
    print('self.link_signup_click called')
    #add participant to sign-up list
    user = data_access.the_user()
  
    if user['spouse']:
      spouse = user['spouse']
    else: spouse = None  

#  FROM ACTIVITY SERVER CODE
    either_user_or_spouse = app_tables.participation.search(activity=self.item, participant=q.any_of(user, spouse))
    if len(either_user_or_spouse) > 0:
      print('either_user_or_spouse > 0 ACTIVITY CLIENT')
      if user['spouse'] == None:
        print('Single person already signed up')
        message = "You have already signed up for this Activity." 
        alert(message)
        return  
      
      print('Couple already signed up')
      message = "You or your spouse have already signed up for one or both of you, please delete and re-sign up if you'd like to make a change."
      alert(message)
      return

# Need to Capture Comment, send to DT, Display on RP.
    
    #If they're not single
    if user['spouse']:
      user_name = user['first_name']
      spouse = user['spouse']
      user_spouse = user['spouse']['first_name']
      user_both = user['couple_name']    
      
      signup_message = f"Enter comments here."    
      t = TextBox(placeholder=signup_message, type="text")
      sign_up_name = alert(title="Enter Signup Comment (if any) and \nSelect Name(s) below ", content=t,
#                title="Activity Sign-Up",
               large=True,
               buttons=[
                 (user_name, user_name),
                 (user_spouse, user_spouse),
                 (user_both, user_both)
               ])
    #else they're single
    else: sign_up_name = user['couple_name']
    
    print(f"The user chose {sign_up_name}")
    comment = t.text
    date_time = self.item['act_date_time']
    message = anvil.server.call('add_participant', self.item, user, sign_up_name, spouse, date_time, comment)  
    alert(message)

    self.refresh_data_bindings()
    self.update_panel()
    
    '''
Above: need to add a dropdown for all participants. 
Thank about using the user['couple_name'] as the default setting?

Dropdown Names from Data Table:
self.drop_down_names.items = [(r["full_name"],r) for r in app_tables.users.search(tables.order_by('full_name', ascending=True))]   
player = self.drop_down_names.selected_value  
    
    '''

  



  

  

