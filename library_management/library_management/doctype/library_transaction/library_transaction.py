# Copyright (c) 2023, mak and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibraryTransaction(Document):
	def before_submit(self):
		if self.type == 'Issue':
			self.validate_issue()
			# set the article status to be Issued
			article = frappe.get_doc('Article', self.article)
			article.status = 'Issued'
			article.save()