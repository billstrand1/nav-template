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


'''