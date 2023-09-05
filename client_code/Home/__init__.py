from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from .. import Globals
from .. import navigation
from .. import data_access

'''
TODO:  Check Home Anon, Home Details Main Component contents


'''

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.    
    self.init_components(**properties)
    
    #------------------Comment out before cloning, run from data_functions Server Code
    # print('Calling for log-in')
    # anvil.server.call('force_debug_login')

    
    user = data_access.the_user()
    if user:
      print(f" User is {user['first_name']}")
    
    
    #------------------CREATE MENU LINKS, UPDATE BASED UPON 'FEATURES' TABLE
    #Create the Menu of Links, then update the navigation module
    self.link_home = Link(text='Home', icon='fa:home')
    self.link_travel = Link(text='Travel', icon="fa:calendar")
    self.link_activities = Link(text='Activities', icon='fa:calendar-check-o')
    self.link_contacts = Link(text='Contacts', icon="fa:book")
    self.link_maps = Link(text='Maps', icon='fa:globe')
    self.link_admin = Link(text='Admin', icon='fa:cog')
    self.link_help = Link(text='Help', icon='fa:question-circle')
    
    #------------------GET 'FEATURES' THAT ARE ENABLED from DT
    menu_status = anvil.server.call('get_menu_status')
    
    # Home - Default ON
    self.menu_panel.add_component(self.link_home)
    self.link_home.set_event_handler('click', self.link_home_click)
      
    for tabs in menu_status:
      # Travel    
      if tabs['name']=='travel': 
        self.menu_panel.add_component(self.link_travel)
        self.link_travel.set_event_handler('click', self.link_travel_click)

      #Activities
      if tabs['name']=='activities': 
        self.menu_panel.add_component(self.link_activities)
        self.link_activities.set_event_handler('click', self.link_activities_click)

      #Contacts
      if tabs['name']=='contacts':     
        self.menu_panel.add_component(self.link_contacts)
        self.link_contacts.set_event_handler('click', self.link_contacts_click)

      #Maps
      if tabs['name']=='maps':
        self.menu_panel.add_component(self.link_maps)
        self.link_maps.set_event_handler('click', self.link_maps_click)
    
      # Admin
      if tabs['name']=='admin':      
        self.menu_panel.add_component(self.link_admin)
        self.link_admin.set_event_handler('click', self.link_admin_click)    
        
      # Help
      if tabs['name']=='help':      
        self.menu_panel.add_component(self.link_help)
        self.link_help.set_event_handler('click', self.link_help_click)    
    
    #------------------Set the base title, will be concatenated with the Menu Item Title
    self.base_title = self.label_title.text #title of app on HOME - Design - label_title
    user = data_access.the_user()  #cache's the user info    
    self.set_account_state(user) #logged in or not, sets button visibility
        
    navigation.home_form = self
    navigation.go_home()
    
    form = navigation.get_form()   
    
    #Set Link Visibility based upon log-in and admin status
    #Leaving Home, Maps, and Help visible
    if user:
      form.label_name.text = 'Hi ' + user['first_name'] + ', '
      self.link_activities.visible = True
      self.link_contacts.visible = True
      self.link_travel.visible = True    
      if user['admin']:
        self.link_admin.visible = True        
      else: 
        self.link_admin.visible = False
    else:
      self.link_admin.visible = False
      self.link_activities.visible = False
      self.link_contacts.visible = False
      self.link_travel.visible = False
      

    
  #------------------FUNCTIONS BELOW:
  #------------------Set Active Nave State - called from navigation  
  def set_active_nav(self, state):
    self.link_home.role = 'selected' if state == 'home' else None
    self.link_travel.role = 'selected' if state == 'travel' else None
    self.link_contacts.role = 'selected' if state == 'contacts' else None    
    self.link_maps.role = 'selected' if state == 'maps' else None
    self.link_activities.role = 'selected' if state == 'activities' else None
    self.link_admin.role = 'selected' if state == 'admin' else None
    self.link_help.role = 'selected' if state == 'help' else None

  #------------------LOAD HOME CARD, CALLED FROM NAV MODULE  
  def load_component(self, cmpt):
     self.card_home.clear()
     self.card_home.add_component(cmpt)

  #------------------USER STATE FUNCTIONS, set button visibility
  def set_account_state(self, user):
      self.btn_logout.visible = user is not None
      self.btn_login.visible = user is None  #i.e. is NOT logged in
#       self.btn_register.visible = user is None 
#       self.btn_account.visible = user is not None #i.e. is logged in
      
  #------------------------------BUTTON CLICKS
  def btn_account_click(self, **event_args):
      print('Account button clicked, nothing to do yet....')
      navigation.go_home()
  
  def btn_logout_click(self, **event_args):
    print('Logout button clicked')
#     anvil.users.logout()
    data_access.logout()
    self.set_account_state(None) #logged in or not, sets button visibility
    self.label_name.text = ''
    self.label_name.visible = False
    self.link_admin.visible = False
    self.link_activities.visible = False
    self.link_contacts.visible = False
    self.link_travel.visible = False    
    navigation.go_home()

  def btn_login_click(self, **event_args):
    user = anvil.users.login_with_form(allow_cancel=True)
    user = data_access.the_user()
    self.set_account_state(user)
    
    if user:
      self.label_name.text = f"Hi {user['first_name']},"
      self.label_name.visible = True
      self.link_activities.visible = True
      self.link_contacts.visible = True
      self.link_travel.visible = True        
      if user['admin']:
        self.link_admin.visible = True
      else: 
        self.link_admin.visible = False    
      
    navigation.go_home()

  #Not using Register button at this time - invisible / not enabled
  def btn_register_click(self, **event_args):
    user = anvil.users.signup_with_form(allow_cancel=True)
    navigation.go_home()
    
  #TODO: Add phone, couple's name, etc. entry form after registration
    
  #------------------------------LINK CLICKS      
  def link_home_click(self, **event_args):
    navigation.go_home()
    
  def link_travel_click(self, **event_args):
    navigation.go_travel()
  
  def link_activities_click(self, **event_args):
    navigation.go_activities()

  def link_maps_click(self, **event_args):
    navigation.go_maps()

  def link_contacts_click(self, **event_args):
    navigation.go_contacts()

  def link_admin_click(self, **event_args):
    navigation.go_admin()

  def link_help_click(self, **event_args):
    navigation.go_help()

