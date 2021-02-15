"""
Created the admin.py module and then imported the Admin class.
Then we check that everything works.
"""

from admin import Admin

super_user = Admin("Roman", "Stupak", 27, "+48579487857")
super_user.admin_privileges.show_privileges()