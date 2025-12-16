# CS-351-Project-Auto-Scaling-AWS
CS-351 Project Auto Scaling AWS W/ Alex Roessler

Assuming the AWS EC2 Instance is running:

Step 1: Connect to ssh

Download the "Project.pem" file in the git repo

SSH into the EC2 instance:
cd $env:USERPROFILE\Downloads
ssh -i "Project.pem" ubuntu@ec2-3-234-218-40.compute-1.amazonaws.com (IPv4 will change)

Once in, download any dependencies missing:
sudo apt update
sudo apt install -y git python3-venv


