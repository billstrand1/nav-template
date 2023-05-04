import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
from datetime import date
import pandas as pd


'''
FOR ACTIVITIES EDIT:

1.  NEED TO REQUIRE LOG-IN
2.  DONE: IF USER or spouse IS OWNER OF ACTIVITY, LET THEM EDIT/DELETE
3.  DONE: IF USER IF ADMIN, LET THEM EDIT/DELETE

'''

#-----------------ACTIVITIES FUNCTIONS (PARTICIPATION BELOW)-----------------
# @anvil.server.callable
def update_activity(activity, activity_dict):
  activity.update(**activity_dict)


@anvil.server.callable
def get_all_future_activities(): 
  print('activities: get_all_future_activities called')
  all_future_activities = app_tables.activities.search(
    tables.order_by("act_date_time", ascending=True), act_date_time=q.greater_than_or_equal_to(date.today()))
 
  future_golf = app_tables.activities.search(
    tables.order_by("act_date_time", ascending=True),
    golf=True, act_date_time=q.greater_than_or_equal_to(date.today()))
 
  future_dinners = app_tables.activities.search(
    tables.order_by("act_date_time", ascending=True),
    dinner=True, act_date_time=q.greater_than_or_equal_to(date.today()))
  
  future_other = app_tables.activities.search(
    tables.order_by("act_date_time", ascending=True),
    other=True, act_date_time=q.greater_than_or_equal_to(date.today()))
  
  return all_future_activities, future_golf, future_dinners, future_other
  
  
@anvil.server.callable
def get_past_activities():  
  print('activities: get_past_activities called')
  return app_tables.activities.search(
    tables.order_by("act_date_time", ascending=True), act_date_time=q.less_than(date.today()))


@anvil.server.callable
def add_activity(activity_title, activity_comments,
                 input_activity_date_picker,input_check_box_golf,
                 input_check_box_meals, input_check_box_other,
                 activity_user):
  print('activities: add_activity called')
  app_tables.activities.add_row(activity=activity_title, comments=activity_comments,act_date_time=input_activity_date_picker,
                               golf=input_check_box_golf, dinner=input_check_box_meals, other=input_check_box_other,
                               owner=activity_user)

  #NEED TO RE-RUN GLOBALS HERE!!
#   Globals.all_activities, Globals.future_golf, Globals.future_dinners, Globals.future_other = get_all_future_activities()

@anvil.server.callable
def delete_activity(activity):
    participants_in_activity = get_participants_in_activity(activity)
    if len(participants_in_activity) > 0:
      print('deleting participants')
      for participant in participants_in_activity:
        if app_tables.participation.has_row(participant):
          participant.delete()
        else:
          raise Exception("Participant does not exist") 
    if app_tables.activities.has_row(activity):
      print('activities: delete_activity called')
      activity.delete()
    else:
      raise Exception("Activity does not exist")
#       activity.delete()
#     Globals.all_activities, Globals.future_golf, Globals.future_dinners, Globals.future_other = get_all_future_activities()

#billstrand1@yahoo.com
@anvil.server.callable
def edit_activity(activity, activity_dict):
    if app_tables.activities.has_row(activity):
      print('activities: edit_activity called')
      activity.update(**activity_dict)  
      
      #Need to update Participation date / time also:
      print(f"Activity Updated, dict date= {activity_dict['act_date_time']}")
      new_date = activity_dict['act_date_time']
      participants_results = app_tables.participation.search(activity=activity)
      for participant in participants_results:
        print(f"Changing date for {participant['participant']['first_name']} ")
        participant['participation_date_time'] = new_date
      
    else:
      raise Exception("Activity does not exist")
#     Globals.all_activities, Globals.future_golf, Globals.future_dinners, Globals.future_other = get_all_future_activities()

#------------------------ACTIVITY PARTICIPANTS----------------------- 
@anvil.server.callable
def get_participants_in_activity(activity):
  participants_results = app_tables.participation.search(activity=activity)
  print(f"Number of participants = {len(participants_results)}")
  return participants_results

@anvil.server.callable
def delete_signup(participant):
  print(f"deleting participant: {participant['participant']['couple_name']}")
  participant.delete()
  
@anvil.server.callable  
def add_participant(activity, participant, sign_up_name, spouse, date_time, comment):
  app_tables.participation.add_row(activity=activity, participant=participant, sign_up_name=sign_up_name, participation_date_time=date_time, comment=comment)

  if '&' in sign_up_name:
    message = f"{sign_up_name} have been signed up."
  else:
    message = f"{sign_up_name} has been signed up."
  return message


#--------TODO: 
#. From HomeDetails:
@anvil.server.callable  
def get_user_or_spouse_activities_str(user, spouse): 
  #Returns 2 messages to display on the HomeDetail page
  # 
#   return 'Message 1', 'Message 2'
    either_user_or_spouse_activities = app_tables.participation.search(
      tables.order_by("participation_date_time", ascending=True), 
      participant=q.any_of(user, spouse))
    if len(either_user_or_spouse_activities) > 0:
      print('either_user_or_spouse_activities > 0 in ACTIVITIES: CLIENT CODE')
      message_activities = 'You have signed up for the following activities:'
    else:
      message_activities = 'You have not signed up for any Activities, please check the Activities link.'
      
    message_activities_detail = ''
    
# Need to format time, then display the activities in order of date.
# Also need to delete 'participation' before deleting 'activities'
# Also need to do FUTURE activities only.

    users_activities = []
    date_list = []
    name_list = []
    activity_list = []
    comment_list = []
    for activity in either_user_or_spouse_activities:
      #go thru participation table and pull out activities
      act_date_time = activity['activity']['act_date_time']
      act_date_time_str = act_date_time.strftime("%a %b %d '%y, %-I:%M %p") + ' | '
      activity_name = activity['activity']['activity'] + ' | '
      sign_up_name = activity['sign_up_name'] + ' | '
      comment = activity['comment']
#       users_activities += [act_date_time_str, activity_name, sign_up_name]
      date_list.append(act_date_time_str)
      name_list.append(sign_up_name)
      activity_list.append(activity_name)
      comment_list.append(comment)
#     print(users_activities)  
    
    activities_df = pd.DataFrame({'Name': name_list, 'Date / Time': date_list, 'Activity': activity_list, 'Your Comment': comment_list})
    if len(activities_df) > 0:
      message_activities_detail = activities_df.to_string(index=False, justify='center', col_space=14)
  
    return message_activities, message_activities_detail
#     self.label_activities_detail.text = users_activities
      
    
                                   
