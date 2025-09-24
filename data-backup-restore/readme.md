# Demo Project: Data Backup & Restore  

## 🛠️ Technologies Used  
- Python  
- Boto3  
- AWS  

## 📌 Project Description  
This project demonstrates automation of data backup and restore operations for **AWS EC2 Volumes** using Python and Boto3.  

### Features  
1. **Automated Backup**  
   - Python script to create backups of EC2 Volumes.  

2. **Snapshot Cleanup**  
   - Python script to delete old EC2 Volume snapshots.  

3. **Volume Restore**  
   - Python script to restore EC2 Volumes from snapshots.  

---

# Create EC2 Instances  

## Steps  

1. **Login to AWS Console**  
   - Navigate to **EC2 Service**.  

2. **Launch Instances**  
   - Create **2 EC2 servers**.  
   - Use the **default settings** for both.  

3. **Add Tags**  
   - After launching, open each instance.  
   - Go to the **Tags** tab.  
     - For the **first instance**, add the tag:  
       - **Key:** Name  
       - **Value:** dev  
     - For the **second instance**, add the tag:  
       - **Key:** Name  
       - **Value:** prod  

4. **Check Attached Volumes**  
   - In the left panel, scroll down and click **Volumes**.  
   - You’ll see that volumes are attached to both EC2 instances.  

5. **Check Snapshots**  
   - Below **Volumes**, click on **Snapshots**.  
   - Initially, this list will be **empty** (no snapshots yet).  
  
- We run a **daily backup** for EC2 volumes.  
- As a result, **snapshots** will be created for all the volumes.  

## Steps  
1. **List Volumes**  
   - Use the **EC2 client** from Boto3.  
   - Function reference: [describe_volumes](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_volumes.html)  
2. **Create Snapshots**  
   - Iterate over each volume returned by `describe_volumes`.  
   - Create a snapshot for each volume.  
### Outcome  
- All EC2 volumes will have **daily snapshots** available for backup and restore.

Step 1: Create Snapshots  
- To create snapshots, we use the Boto3 EC2 client function:  
  [create_snapshot](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_snapshot.html)  

Step 2: Verify in AWS Console  
- After running the script, go to the **AWS Console → EC2 → Snapshots**.  
- You should see **2 snapshots** (one for each volume).  

Step 3: Automate Backups  
- To automate daily backups, we use the **[schedule](https://pypi.org/project/schedule/)** Python library.  
- This allows us to run the snapshot creation script at regular intervals (e.g., once per day).    

## Snapshots for Production Server Only  

Step 1: Tag the Production Volume  
1. Go to **AWS Console → EC2**.  
2. Select the **Prod EC2 instance**.  
3. Click on the **attached volume**.  
4. Open the **Tags** tab.  
5. Add a tag:  
   - **Key:** Name  
   - **Value:** prod  

Step 2: Filter Volumes in Python  
Use the `describe_volumes` function with filters to only select the **prod** volume:  
```python
volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['prod']
        }
    ]
)
```
---

# Cleanup Snapshots  

## Goal  
- Delete all snapshots **except the 2 most recent snapshots** for each volume.  

### Boto3 Reference  
- We will use the EC2 client function:  
  [describe_snapshots](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_snapshots.html)  


###  Sort Snapshots by Date  
- We sort snapshots in **descending order** (most recent first):  
```python
from operator import itemgetter

sorted_by_date = sorted(
    snapshots['Snapshots'],
    key=itemgetter('StartTime'),
    reverse=True
)
```

- The reverse=True parameter ensures the newest snapshots come first in the list.

- To delete snapshots, we’re gonna use: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_snapshot.html

---

# Restore EC2 Volume  

## Overview  
- To restore data, we **create a new volume from a snapshot** (taken during backups).  
- The new volume is then **attached to an EC2 instance**.    

**Attach Volume to EC2 Instance**  
   - In the **AWS Console**, go to **EC2 → Instances**.  
   - Select the **prod instance**.  
   - Open the **Storage** tab.  
   - You will see the existing volume.  
  
**Update Instance ID and Avalability Zone **  
   - Replace the placeholder below with your actual **EC2 Instance ID** from AWS:  
```python
instance_id = "your-ec2-instance-id"
availability_zone = "your-az"
```

- To create an EC2 resource in Python using Boto3, we use:  
  [boto3.resource('ec2')](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/index.html)  

### Important Note  
- Before attaching, the **EBS volume must be in an `available` state**.  
- To handle timing issues, we need to **check the state of the volume in a loop** until it becomes available.  

### Implementation Idea  
- Use a `while` loop to continuously poll the volume state.  
- Proceed with attaching only when the state is `available`.  

### Verification in AWS Console  
- After running the script, go to the **AWS Console → EC2 → Instances**.  
- Select the **prod instance**.  
- In the **Storage tab**, you should now see **2 volumes attached** to the instance.  


