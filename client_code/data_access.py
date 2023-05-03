import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import navigation

'''
SECTIONS:
---------ADMIN-----------------------------------
---------ACTIVITIES------------------------------  
---------CONTACTS--------------------------------  
----------MAPS-----------------------------------
---------TRAVEL----------------------------------  

'''

# ---------ADMIN-----------------------------------
__user = None

def the_user():
#     print('the_user running')
    global __user
    if __user:
        return __user

    #first time getting user
    print('no user, must login and store in cache')
    __user = anvil.users.get_user()
    return __user
  
def logout():
  global __user
  __user = None
  anvil.users.logout()
  

# def get_menu_status():
#   return anvil.server.call('get_menu_status')

# # ---------ACTIVITIES------------------------------  
# def get_tables():
# #   all_activities, participants_in_all_activities, name_list, golf, dinners, other = returned
#   return anvil.server.call('get_tables')

# def get_all_activities():
#   return anvil.server.call('get_all_activities')

# def get_individual_activities(): 
#   return anvil.server.call('get_individual_activities')

# def get_future_activities():
#   return anvil.server.call('get_future_activities')

# def get_past_activities():
#   return anvil.server.call('get_past_activities')

# def get_individual_future_activities():
#   return anvil.server.call('get_individual_future_activities')

# def add_activity(activity_title,activity_comments, 
#                  input_activity_date_picker,
#                  input_check_box_golf,
#                  input_check_box_meals, 
#                  input_check_box_other,
#                  activity_user):

#   return anvil.server.call('add_activity', activity_title,activity_comments, 
#                  input_activity_date_picker,
#                  input_check_box_golf,
#                  input_check_box_meals, 
#                  input_check_box_other,
#                  activity_user)

# def delete_activity(activity):
#   anvil.server.call('delete_activity', activity)
  
# def edit_activity(activity, activity_dict):
#   anvil.server.call('edit_activity', activity, activity_dict) 
  
# # def get_participants_in_activity(activity):
# #   return anvil.server.call('get_participants_in_activity', activity)

# def delete_signup(participant):
#   anvil.server.call('delete_signup', participant)
  
# def add_participant(activity, participant, sign_up_name, spouse):
#   anvil.server.call('add_participant', activity, participant, sign_up_name, spouse)
  
  
# # ---------CONTACTS--------------------------------  

# def get_email_list():
#   return anvil.server.call('get_email_list')

# def get_directory():
#   return anvil.server.call('get_directory')

# # ---------TRAVEL----------------------------------  
# def get_travel_schedule():
#   return anvil.server.call('get_travel_schedule')








