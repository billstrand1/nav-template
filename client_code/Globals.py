import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


print('running Globals....')
all_future_activities, future_golf, future_dinners, future_other = anvil.server.call('get_all_future_activities')
all_past_activities = anvil.server.call('get_past_activities')




'''
.strftime("%a %b %d '%y")  #day, month, day, 'year


.strftime("%a %b %d '%y, %I:%M %p")  adds time am/pm
.strftime("%a %b %d '%y, %-I:%M %p")  removes leading zero on Hours

info = [
  {
    'name': r['name'],
    'employed': r['employed'],
  }
  for r in app_tables.people.search()
]

'''

'''
TODO
1. Need to make sure that if an activity is edited, the participation table is edited also.
Currently, the date-time of the activity is loaded in the participation table, need to remove that.

1.  Try to make the app faster by loading participants in the background. 
2.  You will be prompted to sign up when you create an activity, not requiring you to take the extra step to sign up. 
3.  You will be able to sign up everyone, either as couples or individually.  This signup can be edited/deleted by you or that person/couple. 
4.  Create a summary for the home page that lists all activities and participants, similar to the current summary for you and your spouse. 




'''
