from ._anvil_designer import ActivitiesEditTemplateTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .... import data_access
from .... import navigation

'''
Done:
Done: Problem with New activity not showing up in summary, need to Update Globals somehow.
Done: Also - check for 0:00 Time as an error
Done: Also - check for more than one Category selected

'''

class ActivitiesEditTemplate(ActivitiesEditTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print('ActivitiesEditTemplate opened')
          
    # print(f"before: {activity_dict['act_date_time']}")
    # activity_dict = dict(list(self.item))
    activity_dict['act_date_time'] = activity_dict['act_date_time'].replace(tzinfo=None)
    # print(f"after: {activity_dict['act_date_time']}")
    
    user = data_access.the_user()
    # print('FutureActivitiesTemplate link_edit_click called')
    #from Add Activity code, need to catch more than one Activity, and Midnight.
    
    #NEED TO FIGURE OUT HOW TO DO ERROR MESSAGES IN ALERT BOXES
    self.label_error_msg.visible = False
    
    error = self.sync_data()
    if error:
      self.label_error_msg.text = error
      self.label_error_msg.visible = True      
      return
    
    def sync_data(self):
      if not self.input_activity_title.text:
        return"Activity Title is required."

      if not self.input_activity_date_picker.date:
        return"Date / Time is required.  Please note this is a 24 hour drop-down, and you must press the Apply button"

      if not self.input_check_box_golf.checked and not self.input_check_box_meals.checked and not self.input_check_box_other.checked:
        return"Please select a Category."

      if self.input_check_box_golf.checked and self.input_check_box_meals.checked:
        return "Please select ONLY 1 Category."

      if self.input_check_box_golf.checked and self.input_check_box_other.checked:
        return "Please select ONLY 1 Category."

      if self.input_check_box_meals.checked and self.input_check_box_other.checked:
        return "Please select ONLY 1 Category."

      return None    
    #END Add Activity code, need to catch more than one Activity, and Midnight.
    
    
    # if alert(content=ActivitiesEditTemplate(item=activity_dict), title="Update Activity Info",
    #          large=True, buttons=[("Save", True), ("Cancel", False)]):


 #-------Need to make Submit Edit Click:
               
      anvil.server.call('edit_activity', self.item, activity_dict)
      self.refresh_data_bindings()
      # self.parent.raise_event('x-edit-activity', activity=activity_dict)
      
    message = f"Update recorded, thanks {user['first_name']}!"
    n = Notification(message)
    n.show()
    navigation.go_activities()
    

  def button_submit_edit_click(self, **event_args):
    pass

  def outlined_button_1_click(self, **event_args):
    navigation.go_activities()







