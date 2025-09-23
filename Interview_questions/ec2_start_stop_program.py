import boto3

def ec2_status_change(instance_id, action, region="us-east-1"):#created a funtion 
    
    ec2 = boto3.client("ec2", region_name=region) #calling aws ec2 client api
    
    if action == "start":
        print("instance is getting started")
        ec2.start_instances(InstanceIds=[instance_id])# calling starting funtion and passing instance
    if action == "stop":
        print("instance is getting stopped")
        ec2.stop_instances(InstanceIds=[instance_id])
        # This is a list of instance IDs you want to stop.
        #Even if you are stopping only one instance, it must be inside a list.
    if action == "terminate":
        print ("Instance is getting destroy")
        ec2.terminate_instances(InstanceIds=[instance_id])
        
    else:
        print("invalid action please enter valid action")

if __name__ == "__main__":
    instance_id = "i-0a2fdf3b77f25c504"
    action = "terminate"
    #region = "us-east-1"
    ec2_status_change(instance_id, action)