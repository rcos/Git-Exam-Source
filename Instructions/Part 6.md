# Part 6
Our notoriously non-self-sufficient protagonist, Willy Wazoo, is founding a new RCOS project: an entirely new course scheduler that does nothing better than YACS or QuACS other than being even _less_ accurate. (It’s the “Unquestionably Inaccurate Course Scheduler”, abbreviated as “UICS”, which is pronounced “YOO-icks”.) Willy is building a team of RCOS developers, and he needs help figuring out what his team’s contribution process will be. He sees that Git supports two primary ways to combine one branch with another: merging and rebasing. We already have shown Willy how to merge, so let’s try rebasing this time! We’ll also throw in a simple merge to keep Willy on his toes. This will give him a good overview of the different approaches to branch management that he could pick for his team.

True to the name, UICS’s current conflict-detection algorithm is inaccurate, so we’ll additionally fix it along the way and even add some new features!

_The following steps must be completed in `UICS.py`._
1.	Check out the “main” branch.
2.	Create a new branch named “part6-fullname” and check it out.
3.	Modify `full_name()` in `Course` such that it returns a string of the form `"[code]-[number] [name]"`, where “`[code]`” is the course code (`self.code`), “`[number]`” is the course number (`self.number`), and “`[name]`” is the course name (`self.name`).
4.	Commit the change.
5.	Push the commit to your private GitHub repository.
6.	Check out the “main” branch.
7.	Create a new branch named “part6-conflict” and check it out.
8.	Fix `conflict()` in `Course` such that it correctly takes into account the days on which specific courses take place.
	-	Two courses that don’t take place on any of the same days of the week can’t possibly conflict.
9.	Commit the change.
10.	Push the commit to your private GitHub repository.
11.	Check out the “main” branch.
12.	Add a function `hours()` in `Course` that returns the total number of hours per week that are scheduled for a course as an integer, rounded up to the next whole number.
	-	Python’s [`time`](https://docs.python.org/3/library/datetime.html#time-objects) and [`timedelta`](https://docs.python.org/3/library/datetime.html#timedelta-objects) classes might be useful. They have already been imported for you.
	-	Python’s [`ceil()`](https://docs.python.org/3/library/math.html?highlight=ceil#math.ceil) function might also be useful. It, too, has already been imported for you.
	-	There are 3,600 seconds in an hour.
	-	You can assume that all properties of the `time` class besides `hour` and `minute` are `0`.
13.	Commit the change.
14.	Push the commit to your private GitHub repository.
15.	Check out the “part6-conflict” branch.
16.	Merge the “part6-fullname” branch into the “part6-conflict” branch.
17.	Modify `test_conflict()` such that it compares two courses that do indeed conflict with each other.
	-	You may create helper functions if you want to do so.
18.	Commit the change.
19.	Push the commits to your private GitHub repository.
20.	Check out “part6-conflict” branch.
21.	Rebase the “part6-conflict” on the “main” branch, resolving the merge conflicts as you do so.
	-	Make sure to preserve the changes that you made in both branches.
22.	Push the commits to your private GitHub repository.
23.	Check out the “main” branch.
24.	Fast-forward the “main” branch to the new state of the “part6-conflict” branch.
25.	Push the commits to your private GitHub repository.
