# Demo Project: Health Check - EC2 Status Checks

## Technologies Used
- Python
- Boto3
- AWS
- Terraform

## Project Description
- Create EC2 Instances using **Terraform**.
- Write a **Python** script that fetches the status of EC2 instances and prints it to the console.
- Extend the Python script to continuously check the status of EC2 instances at a specified interval.

## Terraform Setup

1. **Create EC2 Instances**

   - Code is in `main.tf`.
   - Region is set to match Boto3:  
     ```hcl
     provider "aws" {
       region = "eu-west-3"
     }
     ```

2. **Create 3 EC2 Instances**

   - Copy and paste the block of code for one instance three times.
   - Rename each instance appropriately.

3. **Deploy the Infrastructure**

```bash
terraform plan
terraform apply --auto-approve
```

4. Verify in AWS Console
- Navigate to VPC to check the network setup.
- Go to EC2 Instances to see the created instances.

## EC2 Status Check with Python

- After creating the EC2 instances with Terraform, we need to check their states (e.g., `initializing`, `running`, etc.) using Python.
- Implement the script in `main.py` to fetch and display the status of EC2 instances.
- Workflow:
  1. Run `main.py` to see the current status of all EC2 instances.
  2. If you remove an instance from the Terraform script (`main.tf`) and apply the changes:
     ```bash
     terraform apply --auto-approve
     ```
  3. Run `main.py` again to verify the updated instance statuses.

## Fetching EC2 Status and Scheduling Checks

- To get the status of EC2 instances, use the **`describe_instance_status`** function from Boto3.
- To check the status every 5 minutes, use the **`schedule`** library:  
  [https://pypi.org/project/schedule/](https://pypi.org/project/schedule/)
- Install the library using pip:
```bash
pip install schedule
```

## Scheduling EC2 Status Checks and Managing Instances

- **Schedule Status Checks in Python:**  
  To check the status every 5 minutes, use:
```python
schedule.every(5).minutes.do(check_instance_status)
```

- Add the third server in main.tf.
Apply the changes:
`terraform apply --auto-approve`

- Run the Python program (main.py) to check the status of all EC2 instances.

- Remove the last EC2 instance from main.tf.
 -> Apply the changes: `terraform apply --auto-approve`

To remove everything from AWS: `terraform destroy`
