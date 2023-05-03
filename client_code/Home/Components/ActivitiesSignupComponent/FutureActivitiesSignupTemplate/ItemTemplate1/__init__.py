from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...... import data_access


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    user = data_access.the_user()
    user_spouse = user['spouse']
#     print(f"ItemTemplate1 self.item: {self.item['participant'][]}, {user['couple_name']}, {user['first_name']}")
    self.link_delete_participant.visible = False
    
    if self.item['participant'] == user or self.item['participant'] == user_spouse:
      print('Either user or spouse')
      self.link_delete_participant.visible = True
      
    if user['admin']:
      self.link_delete_participant.visible = True
      

  def link_delete_participant_click(self, **event_args):
    print('delete participant called')
    question = 'Are you sure you want to delete this sign-up?' 
    delete = confirm(question)
        
    if delete:
      anvil.server.call('delete_signup', self.item)
      self.parent.raise_event('x-update-panel')

