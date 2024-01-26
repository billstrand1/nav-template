import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a package.

'''
TODO:
x:ContactsComponent:
x:  in the Admin tab, enable the upload of a spreadsheet and populate the Users table
    enable the User to update their info, or let the Admin
  
ActivitiesComponent:
no, switch on/off:  ALL: Uncomment function to show only the listing of Future Activities
  ActivityTemplate - update the Date text to be Day Month Date
x:  Create the ActivitiesSummaryComponent that just shows the listing of Future Activities
  ActivityDisplayComponent - with a template to Edit/Delete an activity
    must be Admin or Created by User.
  ActivityChangeComponent to Edit/Delete and Activity
-----------------  
  self.item['datetime'].strftime("%A %d %b %Y at %I:%M %p") is format for Wednesday 19 Oct 2022 at 09:00 AM
for delete button on RowTemplate:
  def delete_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    confirmed = alert("Are you sure you want to delete this booking?",
                      buttons=[("Yes", True), ("No", False)])
    if confirmed:
      anvil.server.call('delete_booking', self.item)
      get_open_form().content_panel.clear()
      get_open_form().content_panel.add_component(MyBookings())
      

  

  
Golf Sign-up Component
  Log-in required
  Make a RepeatingPanel similar to the BookingApp allowing delete button must be Admin or Created by User
  
Admin component:

   
TravelComponent
  Update to allow Single travel
  Display like shown, make an Update button so they can add/change their travel schedules as couple or single
  Try to make it a Repeating Panel with an edit/delete button must be Admin or Created by User.

'''