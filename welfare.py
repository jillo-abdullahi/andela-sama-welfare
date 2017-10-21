class SamaMember(object):
	"""Class boiler plate for Samasource as a whole"""
	sama_members = {}
	def __init__(self,payroll_number):
		self.payroll_number = payroll_number
	#Register a new member of Samasource
	def register(self,name,gender,project):
		self.member = {}
		self.member['name'] = name
		self.member['gender'] = gender
		self.member['project'] = project

		SamaMember.sama_members[self.payroll_number] = self.member

	def display_sama_members(self):
		return SamaMember.sama_members


class WelfareMember(SamaMember):
	"""Welfare class for members of Welfare"""

	#Class variable to hold a list of members of Welfare
	welfare_members = {}
	
	def __init__(self,payroll_number,joining_date):
		self.payroll_number = payroll_number
		self.joining_date = joining_date

	#Register a new member of Welfare but check if they are a member of Samasource first
	def register(self):
		if self.payroll_number not in SamaMember.sama_members:
			return "That payroll number doesn't exist at Samasource"
		else:
			WelfareMember.welfare_members[self.payroll_number] = self.joining_date
			return "Member successfully added to welfare"

	#Check if someone is a member of Welfare
	def get_member_details(self,payroll_number):
		if self.payroll_number not in WelfareMember.welfare_members:
			return "Not a member of Samasource Welfare"
		else:
			return [WelfareMember.welfare_members[self.payroll_number]]

	#Display all members of Samasource welfare
	def display_welfare_members(self):
		return WelfareMember.welfare_members






