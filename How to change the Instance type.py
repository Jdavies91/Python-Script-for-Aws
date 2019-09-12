# 3.	Change the size of an EC2 instance. 
# The program should display a list of existing instances and the current size of the instance.  
# The user should then be able to run the program with a specific instance ID
# and the new size of the instance.

import boto3
class instanceclass: 
   
    def __init__ (self,instancename, instanceid, instancetype ):
        self.name   = instancename
        self.types  = instancetype
        self.instid= instanceid
    

def main():
    no = "no"
    while True:
        instances = grabAllAvaibleInstance()
        displayAllInstance(instances)
        print("Would you Like to go again: Yes or No")
        useranswer = input()
        if useranswer.lower() == "no":
            break
    
    
def displayinstancechange(instances):
    print("\nPlease type in a number beside the instance name that you would like to change its type")
    instanceselection = input()
    changeinstance(instances, instanceselection)
    
def changeinstance(instance, instanceselection):
    # this is where it selects the instance and changes it too a particular instance type
    i = int(instanceselection)
    print("You have selected "+instance[i-1].name+" with type "+ instance[i-1].types)
    userinstancetype=instancetypeselection(instance[i-1].name)
    changeprocess(userinstancetype,instance,i)
    
def instancetypeselection(instancename):
    print("Please Type in the instance type that you want to change for "+instancename)
    userinstancetype = input()
    return userinstancetype

def changeprocess(userinstancetype,instance,instanceselection):
    print("===========================================================================")
    print("Processing")
    print("===========================================================================")
    print("\n"+ instance[instanceselection-1].name+ " changing instance type to "+ userinstancetype)
    client = boto3.client('ec2')
    idValueStart = instance[instanceselection-1]
    stopinstance(client, idValueStart)
    waiter(client, idValueStart)
    client.modify_instance_attribute(InstanceId=idValueStart.instid, Attribute='instanceType', Value=userinstancetype)
    startinstance(client, idValueStart)
    print("Instance Name "+ instance[instanceselection-1].name + " has now changed to " + userinstancetype)
    
def waiter(client, idValueStart):
    print(idValueStart.name+" is waiting to Stop")
    waiter=client.get_waiter('instance_stopped')
    waiter.wait(InstanceIds=[idValueStart.instid])
    
def stopinstance(client, idValueStart):
    print(idValueStart.name+" is now started the stopping process")
    client.stop_instances(InstanceIds=[idValueStart.instid])

def startinstance(client, idValueStart):
    print(idValueStart.name+" is now Starting up")
    client.start_instances(InstanceIds=[idValueStart.instid])
    


def grabAllAvaibleInstance():
    instancearr = []
    types = ""
    ec2 = boto3.resource('ec2')
    for inst in ec2.instances.all():
        name =inst.tags
        ids = inst.id
        n = name[0]['Value']
        instancearr.append(instanceclass(n,ids,inst.instance_type))
        types = ""
    return instancearr
 
def displayAllInstance(instances):
    arrlength=len(instances)
    print("The list Below is all the current instances avaible")
    for i in range(0,arrlength):
        print(str(i+1) +". "+instances[i].name +" " +instances[i].types)
    displayinstancechange(instances)



if __name__ == '__main__':
  main()