import boto3

def find_untagged_vpc():  # Define a function to find untagged VPCs
    # Create an EC2 client using boto3 to interact with AWS EC2 service
    ec2 = boto3.client("ec2")  
    
    # Call AWS API to list all VPCs; response is a dictionary (JSON-like structure)
    response = ec2.describe_vpcs()  
    
    # Create an empty list to store untagged VPC IDs
    untagged = []  
    
    # Loop through all VPCs returned in the response
    for vpc in response["Vpcs"]:  
        
        # Check if the VPC has no tags (empty or missing "Tags" key)
        if not vpc.get("Tags", []):  
            # Add the VPC ID to the untagged list
            untagged.append(vpc["VpcId"])    
    
    # Return the list of untagged VPC IDs
    return untagged

# Run this block only if the script is executed directly (not imported as a module)
if __name__ == "__main__":  
    print(find_untagged_vpc())
