# distributed_app
An example of a distributed app for learning CI (with Jenkins and GitHub web hooks) and continuous deployment  (deploying on RaspberryPi)

The app uses a count min sketch for rate limit purposes.

Used network segmentation in Docker for security.

The application is built on local machine, architecture x86 but is deployed on RasberryPi/ARMv7. In order to be able to build arm images on x86 I used qemu. [Link here](https://www.stereolabs.com/docs/docker/building-arm-container-on-x86/?fbclid=IwAR3MGyd9cLLeRp1nxRl0mNk_ttOxNDHjf0uq5C9-9kPMOjHOSn7EdF9s7m4)


# Workflow:

<img src="https://github.com/dgaponcic/distributed_app/blob/master/workflow.png?raw=true" />


# System View

<img src="https://raw.githubusercontent.com/dgaponcic/distributed_app/master/system_view.png?raw=true" />
