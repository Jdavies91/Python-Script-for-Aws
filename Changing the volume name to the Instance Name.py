# 2.Find all EC2 instances in an account and tag the EBS volumes associated 
# with each instance with the same tags from the instance.
# NOT TO SURE IF THIS IS DONE
import boto3

def main():
    findattachvolumes()





#finds all instances and instances 
def findNamesfromid(instanceid):
  ec2 = boto3.resource('ec2')
  insttag=ec2.Instance(instanceid).tags
  #f= instname.tags

  instname=insttag[0]['Value']
  return instname
  
def findNamesfromVolume(volid,vol,instname):
  response= vol.create_tags(Tags= [{'Key': 'Name','Value': instname}],)




# Grab all instance tags.
def findattachvolumes():
  ec2 = boto3.resource('ec2')
  #instance = ec2.Instance('Id')
  for volume in ec2.volumes.all():
      for instattachment in volume.attachments:
        instid = instattachment['InstanceId']
        instname = findNamesfromid(instid)
        volid  = instattachment['VolumeId'] 
        findNamesfromVolume(volid,volume,instname)
                
        print("Instance Name: "+instname +" Volume Name: "+instname )

# do a swap of tags and name and import it to volum
if __name__ == '__main__':
  main()