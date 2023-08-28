from ._anvil_designer import FutureActivitiesTemplateTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .... import navigation
from .... import data_access
from .... import Globals

from .ActivitiesEditTemplate import ActivitiesEditTemplate

class FutureActivitiesTemplate(FutureActivitiesTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
#     print('FutureActivitiesTemplate opened')
    self.link_delete.visible = False
    self.link_edit.visible = False
#     self.refresh_data_bindings()
    
    
    user = data_access.the_user()
#     print('testing if user is admin')
    if user['admin'] == True:
      self.link_delete.visible = True
      self.link_edit.visible = True
 
#     print('testing if user is owner of activity')
    owner_of_activity = self.item['owner']
    if owner_of_activity == user:
      self.link_delete.visible = True
      self.link_edit.visible = True
    

  def link_edit_click(self, **event_args):
    activity_dict = dict(list(self.item))
    user = data_access.the_user()
    print('FutureActivitiesTemplate link_edit_click called')
    if not self.input_check_box_golf.checked and not self.input_check_box_meals.checked and not self.input_check_box_other.checked:

    
    if alert(content=ActivitiesEditTemplate(item=activity_dict), title="Update Activity Info",
             large=True, buttons=[("Save", True), ("Cancel", False)]):      
      anvil.server.call('edit_activity', self.item, activity_dict)
      
      activity_date = activity_date.astimezone(timezone.utc)

      self.parent.raise_event('x-edit-activity', activity=activity_dict)
      
    message = f"Update recorded, thanks {user['first_name']}!"
    n = Notification(message)
    n.show()
    


  def link_delete_click(self, **event_args):
    print('FutureActivitiesTemplate link_delete_click called')
    user = data_access.the_user()
    if confirm(f"Are you sure you want to delete this entry, {user['first_name']} ?\n It will also delete the sign-ups for this activity."):
      self.parent.raise_event('x-delete-activity', activity=self.item)



    
    


  

  

