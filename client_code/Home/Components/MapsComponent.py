from ._anvil_designer import MapsComponentTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import navigation
from ... import data_access


class MapsComponent(MapsComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  

    #Name Label on the Main Form    
    user = data_access.the_user()
    form = navigation.get_form()    
    if user:
      form.label_name.text = 'Hi ' + user['first_name'] + ', '
      print(user['first_name'])
      
      