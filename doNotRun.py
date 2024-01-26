import subprocess, sys # necessary imports

while True: # Infinite Loop
  # Open a new Subprocess and start this file (sys.argv[0])
  # using the local Python Interpreter (sys.executable).
  # The creationflags indicate that it should create a new
  # console, for the new instance!
  subprocess.POpen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)