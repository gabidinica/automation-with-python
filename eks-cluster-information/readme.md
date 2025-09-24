# Demo Project: Automate Displaying EKS Cluster Information

## 🛠 Technologies Used
- Python  
- Boto3  
- AWS EKS  

## 📌 Project Description
This project involves writing a Python script to automate the process of fetching and displaying Amazon EKS (Elastic Kubernetes Service) cluster information. The script uses **Boto3**, the AWS SDK for Python.

--- 

## 📊 Cluster Information Fetched
- EKS cluster **status**  
- Kubernetes **version**  
- Cluster **endpoint**  

## 🚀 Steps to Implement
1. **Create EKS Cluster using Terraform**  
   - Define Terraform scripts to provision an EKS cluster on AWS.  
   - Apply the configuration to deploy the cluster.  

2. **Write a Python Program**  
   - Use the AWS SDK for Python (**Boto3**) to connect with EKS.  
   - Fetch the cluster’s **status**, **Kubernetes version**, and **endpoint**.  
   - Display the information in a readable format.  

## 🔧 Creating an EKS Cluster

To create an EKS cluster, we use the Terraform code from this repository:  
👉 [EKS Cluster Terraform Repo](https://github.com/gabidinica/terraform/tree/main/eks-cluster-terraform)

Run the following command to provision the cluster:

```bash
terraform apply --auto-approve
```

Terraform will automatically create the cluster in the `eu-central-1` region.

-> ✅ Verification

After the deployment, you can check the AWS Management Console:
- 3 EC2 machines will be running (worker nodes).
- 1 EKS cluster will be created.

## 🐍 Using the EKS Client with Boto3

In this project, we will use the **EKS Client** from Boto3:  
👉 [Boto3 EKS Client Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#client)

To fetch details for **individual clusters**, we use the `describe_cluster` method:  
👉 [describe_cluster Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/describe_cluster.html)

