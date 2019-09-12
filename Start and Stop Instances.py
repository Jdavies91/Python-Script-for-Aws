import boto3
#Didn't put dry run flag in should look into it but after dealing with rest.

def main():
 mainmenu()
#main menu ask the user question and finds information base on that question    
def mainmenu():
  userstatus=userstatuschoice()
  userinstance = userinstancechoice()
  foundornotfound(userstatus, userinstance)

#Asks question if its found or not
def foundornotfound(userstatus,userinstance):
  usergoingagain = ""
  found =getinstances(userinstance,userstatus)
  if found == True:
    print("Would you like to go again? Yes/No")
    usergoingagain = input()
  if found == False:
    print("Could not Find instance. Would you like to try again?")
    usergoingagain = input()
  if usergoingagain.lower() == "yes":
    mainmenu()
#Ask the status The user woulod like to choose
def userstatuschoice():
  while True:  
    print("Please type Start if you want the instance to Start or Stop if you would like a instance to Stop")
    userstatus=input()
    if userstatus.lower()=='start': 
      break 
    if userstatus.lower()== 'stop':
      break
  return userstatus    
#Ask User for input on what instance they would like to choice
def userinstancechoice():
  userinstance=""
  print("Please type the name of the instance")
  userinstance=input()
  return userinstance    

# Gets Instance we are currently looking for
def getinstances(name, status):
  ec2 = boto3.resource('ec2')
  for instance in ec2.instances.all():
    if comparingId(name, instance, status) == True:
      return True
  return False 

#compares if the id is valid to the instance avaible
def comparingId(name, instance,status):
  for value in instance.tags:
        temp= value['Value']
        if(temp == name):
          startingorstoppinginstance(status,instance,name)
          return True
  return False
    
#Change Status of Instance          
def startingorstoppinginstance(status,instance, name):
  start = "start"
  if status.lower()==start:
    startinstance(instance,name)
  else:
    stopinstance(instance,name)

def startinstance(instance,name):
    instance.start()
    print ('Starting '+ name)
def stopinstance(instance,name):
    instance.stop()
    print ('Stopping '+ name)

if __name__ == '__main__':
  main()

