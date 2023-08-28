import anvil.secrets
import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
from datetime import date


@anvil.server.callable
def get_travel_from_dt():
  all_travel_records = app_tables.travel.search(tables.order_by("arrive", ascending=True))
  return all_travel_records

@anvil.server.callable  
def add_travel_schedule(user, arrival_date, depart_date):    
    message = 'Your travel plans have been added, thanks.'
    app_tables.travel.add_row(participant=user, arrive=arrival_date, depart=depart_date)
    return message
  
@anvil.server.callable
def delete_schedule(schedule):
    if app_tables.travel.has_row(schedule):
      print('deleting schedule called from server code')
      schedule.delete()
    else:
      raise Exception("Schedule does not exist")
#       activity.delete()
  
  
# #NEED TO MOVE ALERT/NOTIFICATION TO CLIENT CODE  

#   print(f"{activity['activity']}, and {participant['first_name']}")  
#   rows_of_signed_up = app_tables.participation.search(activity=activity)
#   for individual_signed_up in rows_of_signed_up:   
#     if individual_signed_up['participant'] == participant or individual_signed_up['participant'] == spouse:
#         message = "You or your spouse have already signed up for one or both of you, please delete and re-sign up if you'd like to make a change."
        
#         if individual_signed_up['participant']['spouse'] == None:
#           message = "You have already signed up for this Activity."
        
#         return message  
#   app_tables.participation.add_row(activity=activity, participant=participant, sign_up_name=sign_up_name)



