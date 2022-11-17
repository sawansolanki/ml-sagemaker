import os

cwd = os.getcwd()

files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
