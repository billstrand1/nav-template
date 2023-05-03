from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..... import data_access
from ..... import navigation

class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.link_delete.visible = False
        
    user = data_access.the_user()
    if user['admin'] == True:
      self.link_delete.visible = True
 
    owner_of_activity = self.item['participant']
    spouse_of_owner = self.item['participant']['spouse']
    
    if user == owner_of_activity or user == spouse_of_owner:
      self.link_delete.visible = True

  def link_delete_click(self, **event_args):

    user = data_access.the_user()
    if confirm(f"Are you sure you want to delete this entry, {user['first_name']} ?"):
      self.parent.raise_event('x-delete-schedule', schedule=self.item)

