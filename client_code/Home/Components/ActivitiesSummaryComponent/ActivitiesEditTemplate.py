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




