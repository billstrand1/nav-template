import anvil.secrets
import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

#---------ADMIN----------------------------------- 

@anvil.server.callable
def get_menu_status():
  return app_tables.features.search(
    tables.order_by("order_of_menu_items", ascending=True), enabled=True)

@anvil.server.callable
def get_column_names():
  return app_tables.features.list_columns()


