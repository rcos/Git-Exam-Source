# WARNING: Complete the parts and steps in order. Don’t create any commits unless the instructions explicitly ask that you do so. Grading will fail if there are any extraneous commits.
# NOTE: All strings and commit messages are case- and whitespace-sensitive, though trailing whitespace is stripped from commit messages when grading. Don’t include quotation marks.

# PART 1
# 1. Check out the “main” branch.
# 2. Modify `rcos()` so that it returns the string `"Rensselaer Center for Open Source"`.
# 3. Commit the change with a message that starts with “[Part 1]”.
# 4. Push the commit to your private GitHub repository.

# PART 2
# 1. Check out the “main” branch.
# 2. Create a new branched named “part2” and check it out.
# 3. Modify `alyssa_p()` so that it returns the string `"p. hacker"`.
# 4. Commit the change with a message that starts with “[Part 2]”.
# 5. Push the commit to your private GitHub repository.
# 6. Check out the “main” branch.
# 7. Rename `alyssa_p()` to `alyssa()`.
# 8. Commit the change with a different message that starts with “[Part 2]”.
# 9. Push the commit to your private GitHub repository.

# PART 3
# 1. Check out the “main” branch.
# 2. Merge the “part2” branch into the “main” branch. Don’t automatically commit the merge.
# 3. If there’s a merge conflict, then resolve it. (There might not be a merge conflict.)
#	- Resolve the merge conflict (if there is one) such that a single function `alyssa()` returns the string `"p. hacker"`.
# 4. Create a merge commit with a message that starts with “[Part 3]”.
# 5. Push the commit to your private GitHub repository.

# PART 4
# 1. Check out the “main” branch.
# 2. Create a new branch named “part4” and check it out.
# 3. Add a new function `ben()` that returns the string `"wazoo"`.
# 4. Commit the change with a message that starts with “[Part 4]”.
# 5. Push the commit to your private GitHub repository.
# 6. Check out the “main” branch.
# 7. Add a new function `willy()` that returns the string `"bitdiddle"`.
# 8. Commit the change with a different message that starts with “[Part 4]”.
# 9. Push the commit to your private GitHub repository.

# PART 5
# 1. Check out the “main” branch.
# 2. Merge the “part4” branch into the “main” branch.
# 3. Resolve the merge conflict such that the function `ben()` returns the string `"bitdiddle"` and the function `willy()` returns the string `"wazoo"`.
# 4. Create a merge commit with a message that starts with “[Part 5]”.
# 5. Push the commit to your private GitHub repository.

# PART 6
# See `UICS.py`…

def rcos():
	return "Rensselaer Center for Open Software"

def alyssa_p():
	surname = "hapck.er"
	remove = ". p"
	return "".join(letter for letter in surname if letter not in remove)
