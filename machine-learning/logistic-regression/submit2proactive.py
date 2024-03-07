import os
import proactive
import getpass

from dotenv import load_dotenv

# Load environment variables from a .env file, if available
load_dotenv()

print("Logging on proactive-server...")
# Retrieve the ProActive server URL from environment variables or prompt the user if not set
proactive_url = os.getenv("PROACTIVE_URL")
if not proactive_url:
    proactive_url = input("Server (default: https://try.activeeon.com:8443): ")
if proactive_url == "":
    proactive_url = "https://try.activeeon.com:8443"
# Ensure the URL starts with http/https and append a default domain if necessary
if not proactive_url.startswith("http"):
    proactive_url = "https://"+proactive_url+".activeeon.com:8443"

print("Connecting on: " + proactive_url)
# Initialize the ProActive gateway with the given server URL
gateway = proactive.ProActiveGateway(base_url=proactive_url)

# Retrieve username and password from environment variables or prompt the user
username = os.getenv("PROACTIVE_USERNAME")
password = os.getenv("PROACTIVE_PASSWORD")
if not (username and password):
    username = input("Login: ")
    password = getpass.getpass(prompt="Password: ")

# Connect to the ProActive server with the provided credentials
gateway.connect(username, password)
# Assert the connection was successful
assert gateway.isConnected() is True
print("Connected")

try:
    # Start setting up a new job
    print("Creating a proactive job...")
    proactive_job = gateway.createJob()
    proactive_job.setJobName("CIFAR-10_Logistic_Regression_Pipeline")

    # Create and configure the first task of the job
    print("Creating a proactive task #1...")
    proactive_task_1 = gateway.createPythonTask('Train')
    proactive_task_1.setTaskImplementationFromFile("train.py")
    # Set the runtime environment for the task using Docker
    proactive_task_1.setRuntimeEnvironment(
        type="docker", image="python:3.9-slim",
        mount_host_path="/shared", mount_container_path="/shared"
    )
    # Specify input files required by the task
    proactive_task_1.addInputFile('requirements.txt')
    proactive_task_1.addInputFile('dataset/**')

    # Add a pre-script to prepare the environment before the task runs
    print("Adding a pre-script to task #1...")
    pre_script = gateway.createPreScript(language='bash')
    pre_script.setImplementation("""
        apt-get -qq update && apt-get install -y wget unzip
        pip install -r requirements.txt
        chmod +x ./dataset/download_dataset.sh
        cd dataset && ./download_dataset.sh
    """)
    proactive_task_1.setPreScript(pre_script)

    # Add the configured task to the job
    print("Adding proactive tasks to the proactive job...")
    proactive_job.addTask(proactive_task_1)

    # Submit the job to the ProActive scheduler and print the job ID
    print("Submitting the job to the proactive scheduler...")
    job_id = gateway.submitJobWithInputsAndOutputsPaths(proactive_job)
    print("job_id: " + str(job_id))

finally:
    # Ensure the gateway disconnects even if an error occurs
    print("Disconnecting")
    gateway.disconnect()
    print("Disconnected")
    # Terminate the gateway instance
    gateway.terminate()
    print("Finished")
