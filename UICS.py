# WARNING: Complete the parts and steps in order. Don’t create any commits unless the instructions explicitly ask that you do so. Grading will fail if there are any extraneous commits.
# NOTE: All strings and commit messages are case- and whitespace-sensitive, though trailing whitespace is stripped from commit messages when grading. Don’t include quotation marks.

# PARTS 1–5
# See `Code.py`…

# PART 6
# 1. Check out the “main” branch.
# 2. Create a new branch named “part6-fullname” and check it out.
# 3. Modify `full_name()` in `Course` such that it returns a string of the form `"[code]-[number] [name]"`, where “`[code]`” is the course code (`self.code`), “`[number]`” is the course number (`self.number`), and “`[name]`” is the course name (`self.name`).
# 4. Commit the change.
# 5. Push the commit to your private GitHub repository.
# 6. Check out the “main” branch.
# 7. Create a new branch named “part6-conflict” and check it out.
# 8. Fix `conflict()` in `Course` such that it correctly takes into account the days on which specific courses take place.
# 	- Two courses that don’t take place on any of the same days of the week can’t possibly conflict.
# 9. Commit the change.
# 10. Push the commit to your private GitHub repository.
# 11. Check out the “main” branch.
# 12. Add a function `hours()` in `Course` that returns the total number of hours per week that are scheduled for a course as an integer, rounded up to the next whole number.
# 	- Python’s `time` and `timedelta` classes might be useful. They have already been imported for you.
# 	- Python’s `ceil()` function might also be useful. It, too, has already been imported for you.
# 	- There are 3,600 seconds in an hour.
# 	- You can assume that all properties of the `time` class besides `hour` and `minute` are `0`.
# 13. Commit the change.
# 14. Push the commit to your private GitHub repository.
# 15. Check out the “part6-conflict” branch.
# 16. Merge the “part6-fullname” branch into the “part6-conflict” branch.
# 17. Modify `test_conflict()` such that it compares two courses that do indeed conflict with each other.
# 	- You may create helper functions if you want to do so.
# 18. Commit the change.
# 19. Push the commits to your private GitHub repository.
# 20. Check out “part6-conflict” branch.
# 21. Rebase the “part6-conflict” on the “main” branch, resolving the merge conflicts as you do so.
# 	- Make sure to preserve the changes that you made in both branches.
# 22. Push the commits to your private GitHub repository.
# 23. Check out the “main” branch.
# 24. Fast-forward the “main” branch to the new state of the “part6-conflict” branch.
# 25. Push the commits to your private GitHub repository.

from datetime import time, timedelta
from enum import Enum
from math import ceil

class DayOfWeek(Enum):
	MONDAY		= 1
	TUESDAY 	= 2
	WEDNESDAY	= 3
	THURSDAY	= 4
	FRIDAY		= 5
	SATURDAY	= 6
	SUNDAY		= 7

class Course:

	def __init__(self, code, number, name, start_time, end_time, days_of_week):
		self.code = code
		self.number = number
		self.name = name
		self.start_time = start_time
		self.end_time = end_time
		self.days_of_week = days_of_week
	
	def full_name(self):
		return self.name
	
	def conflict(self, other):
		starts_later = self.start_time > other.end_time
		ends_earlier = self.end_time < other.start_time
		return not (starts_later or ends_earlier)

def rcos():
	start_time = time(hour=16, minute=0)
	end_time = time(hour=17, minute=50)
	days_of_week = set([DayOfWeek.TUESDAY, DayOfWeek.FRIDAY])
	return Course("CSCI", 2961, "Rensselaer Center for Open Source", start_time, end_time, days_of_week)

def rpg():
	start_time = time(hour=16, minute=0)
	end_time = time(hour=17, minute=20)
	days_of_week = set([DayOfWeek.MONDAY, DayOfWeek.THURSDAY])
	return Course("ECSE", 4141, "Renewable Power Generation", start_time, end_time, days_of_week)

def test_conflict():
	rcos_course = rcos()
	rpg_corse = rpg()
	if rcos_course.conflict(rpg_corse):
		return "Conflict!"
	else:
		return "No conflict"

if __name__ == "__main__":
	print(rcos().full_name())
	print(rpg().full_name())
	print(test_conflict())
