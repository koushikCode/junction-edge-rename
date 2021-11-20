import os 
os.system('python junction-id-modification.py')
os.system('python edge-id-modification.py')

if os.path.exists("saltlake_intermediate.net.xml"):
  os.remove("saltlake_intermediate.net.xml")
else:
  print("All good")
