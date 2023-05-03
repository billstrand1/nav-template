import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.users
import anvil.tables.query as q
from anvil.tables import app_tables
import data_access


from .Home.HomeAnonComponent import HomeAnonComponent
from .Home.HomeDetailsComponent import HomeDetailsComponent
from .Home.Components.TravelComponent import TravelComponent
from .Home.Components.ActivitiesSignupComponent import ActivitiesSignupComponent
from .Home.Components.ActivitiesSummaryComponent import ActivitiesSummaryComponent
from .Home.Components.ContactsComponent import ContactsComponent
from .Home.Components.ContactsComponent.EmailList import EmailList
from .Home.Components.MapsComponent import MapsComponent
from .Home.Components.AdminComponent import AdminComponent
from .Home.Components.HelpComponentLoggedIn import HelpComponentLoggedIn
from .Home.Components.HelpComponentLoggedOut import HelpComponentLoggedOut



"""
Share the navigation module with the Component forms, (import navigation)
Then you can re-direct after a button/link push: navigation.go_home()

---------ADMIN-----------------------------------
  #REMOVE COMMENT FOR PRODUCTION
#   user = require_account()  #USE THIS FOR ALL COMPONENTS THAT REQUIRE LOGIN
#   if not user['admin']:
#     print('Not admin')
#     go_home()
#     return
---------ACTIVITIES------------------------------  
---------CONTACTS--------------------------------  
----------MAPS-----------------------------------
---------TRAVEL----------------------------------  


"""
#---------ADMIN-----------------------------------
home_form = None


def get_form():
  '''
  In the Home form:
    self.base_title = self.label_title.text
    navigation.home_form = self
    navigation.go_home() 
  '''
  if home_form is None:
    raise Exception("You must set the home form first.")
  return home_form

#Update Active Nav State and Title (called from go_link and Home) 
#function name is the same (set_active_nav)
def set_active_nav(state):
  form = get_form()
  form.set_active_nav(state)  
  
def set_title(text):
  form = get_form()
  base_title = form.base_title
  
  if text:
    form.label_title.text = base_title + " - " + text
  else:
    form.label_title.text = base_title
    
def require_account():
  print('require_account running')
  '''
  in functions that require an account, add the following:
  
  user = require_account()
  if not user:
    go_home()
    return
  
  '''
  user = data_access.the_user()
  if user: 
    return user

  user = anvil.users.login_with_form(allow_cancel=True)
  form = get_form()
  form.set_account_state(user) #logged in or not, sets button visibility
  return user

def go_admin():
  print('go_admin')
  set_active_nav('admin')
  set_title("Admin")
  
  user = require_account()  #USE THIS FOR ALL COMPONENTS THAT REQUIRE LOGIN
  if user:
    if not user['admin']:
      print('Not admin')
      go_home()
      return
  
  form = get_form()
  form.load_component(AdminComponent())
    

# ---------HOME---------------------------------      
# load_component is a function from the Home Form    
#Navigation and Form Loading based upon Log-in Status:

def go_home():
  print('go_home')
  set_active_nav('home')
  set_title("")
  form = get_form()

  user = data_access.the_user()
   
  if user:
    form.load_component(HomeDetailsComponent())
  else:
    form.load_component(HomeAnonComponent())
    
# ---------ACTIVITIES------------------------------  
def go_activities():
  print('go_activities')
  set_active_nav('activities')
  set_title("Activities")
  
  user = require_account()
  if not user:
    go_home()
    return  
  
  form = get_form()
  form.load_component(ActivitiesSummaryComponent())
  
def go_activities_signup():
  print('go_activities_add')
  set_active_nav('activities')
  set_title("Activities Signup")

  user = require_account()
  if not user:
    go_home()
    return

  form = get_form()
  form.load_component(ActivitiesSignupComponent())  
  
# ---------CONTACTS-------------------------------- 
def go_contacts():
  print('go_contacts')
  set_active_nav('contacts')
  set_title("Contacts")
  user = require_account()
  if not user:
    go_home()
    return
  form = get_form()
  form.load_component(ContactsComponent())
  
def go_email_list():
  print('go_contacts')
  set_active_nav('contacts')
  set_title("Email List")
  
  user = require_account()
  if not user:
    go_home()
    return
  
  form = get_form()
  form.load_component(EmailList())  

# ----------MAPS-----------------------------------
def go_maps():
  print('go_maps')
  set_active_nav('maps')
  set_title("Maps")
  form = get_form()
  form.load_component(MapsComponent())   
  
# ---------TRAVEL----------------------------------    
def go_travel():
  print('go_travel')
  set_active_nav('travel')
  set_title("Travel")
 
  print('calling require_account from go_travel')
  user = require_account()

  if not user:
    go_home()
    return
  
  form = get_form()
  form.load_component(TravelComponent())
  
# ---------HELP----------------------------------    

def go_help():
  print('go_help')
  set_active_nav('help')
  set_title("Help")
  form = get_form()

  user = data_access.the_user()
   
  if user:
    form.load_component(HelpComponentLoggedIn())
  else:
    form.load_component(HelpComponentLoggedOut())

  




  
  



  

    

      
