# Copyright (c) 2023, mak and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LibraryMember(Document):
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name}';
	# to test the controller code from outside the below method introduced
	def getFullName(self):
		return self.full_name;