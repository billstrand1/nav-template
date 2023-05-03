import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
import anvil.media

@anvil.server.callable
def store_data(file):
  with anvil.media.TempFile(file) as file_name:
    if file.content_type == 'text/csv':
      df = pd.read_csv(file_name)
    else:
      df = pd.read_excel(file_name)
    for d in df.to_dict(orient="records"):
      # d is now a dict of {columnname -> value} for this row
      # We use Python's **kwargs syntax to pass the whole dict as
      # keyword arguments
      app_tables.activities.add_row(**d)
