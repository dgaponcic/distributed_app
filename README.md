# distributed_app
An example of a distributed app for learning CI (with Jenkins running on Raspberry Pi and GitHub web hooks) and continuous deployment  (deploying on RaspberryPi)

The app uses a count min sketch for rate limit purposes.

Used network segmentation in Docker for security.

Encountered issues:

* Initially Jenkins was running on local machine. When deploying on Raspberry Pi encountered incompatibility of arm and x86.

# Workflow:

<img src="https://raw.githubusercontent.com/dgaponcic/distributed_app/master/workflow.png?raw=true" />


# System View

<img src="https://raw.githubusercontent.com/dgaponcic/distributed_app/master/system_view.png?raw=true" />
