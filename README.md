# CS-351-Project-Auto-Scaling-AWS
CS-351 Project Auto Scaling AWS W/ Alex Roessler

Assuming the AWS EC2 Instance is running:

Step 1: Connect to ssh

Download the "Project.pem" file in the Git repo

SSH into the EC2 instance:
cd $env:USERPROFILE\Downloads
ssh -i "Project.pem" ubuntu@ec2-3-234-218-40.compute-1.amazonaws.com (IPv4 will change)


Step 2: Set up

Once in instance, download any dependencies missing:
sudo apt update
sudo apt install -y git python3-venv

Download the project from GitHub:
cd ~
git clone https://github.com/Drewbal1/CS-351-Project-Auto-Scaling-AWS.git flask
cd flask

Create the virtual env (first time only):
cd ~/flask         #if not already here
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Run Flask app with gunicorn:
cd ~/flask          #if not already here
source venv/bin/activate
nohup gunicorn -b 0.0.0.0:5000 app:app > gunicorn.log 2>&1 &


Step 3: Confirm and connect

Verify server is running:

curl http://127.0.0.1:5000/health
Should see: OK

Connect using the IPv4:

http://<EC2_PUBLIC_IPv4>:5000/
