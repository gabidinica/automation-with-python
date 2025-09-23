# Demo Project: Automate Configuring EC2 Server Instances

## 🛠️ Technologies Used
- Python  
- Boto3  
- AWS  

## 📌 Project Description
This project demonstrates how to automate the configuration of EC2 server instances using Python.  
A script is written with **Boto3 (AWS SDK for Python)** to automatically add **environment tags** to all EC2 server instances, ensuring better resource management and cost tracking.

---

## 🔍 Step 1: Describe Instances
To work with EC2 instances, we first need to see the response structure of the `describe_instances()` call.  
[Boto3 Docs – describe_instances](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instances.html)

## Step 2: 📌 Step 2: Collect Instance IDs

We only need Instance IDs for tagging.
- collect all instance ids into a list
- add tags for all instances at once
To create tags in EC2, we need a **resource** that contains the list of instance IDs.  

📖 Reference: [Boto3 Docs – create_tags](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/create_tags.html)

- `Resources` → a list of **Instance IDs**  
- `Tags` → key-value pairs you want to apply 

## 🚀 Launching EC2 Instances and Tagging

### 1. Launch EC2 Instances
1. Go to the **AWS Console → EC2 → Launch Instance**.  
2. Keep all settings as **default**.  
3. Set the **number of instances** to **2**.  
4. Launch the instances in the **Frankfurt region**.  
5. Repeat the same steps for the **Paris region**.

---

### 2. Run the Tagging Script
1. Execute the Python script that automates tagging of EC2 instances.  
2. Go to the **AWS Console → EC2 → Select any instance → Tags tab**.  
3. Verify that the tags are applied correctly.  
4. Change the **region** in the console and check that the tags appear in the other region as well.

---

### 3. Cleanup
- Delete all EC2 instances to avoid unnecessary charges.  
  **AWS Console → EC2 → Select instances → Actions → Terminate Instances**

