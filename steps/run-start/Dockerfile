FROM relaysh/core:latest-python
RUN pip install requests
COPY step.py /
CMD ["python3", "/step.py"]

LABEL "org.opencontainers.image.title"="Start a Puppet run"
LABEL "org.opencontainers.image.description"="This step requests a new Puppet run using the Relay API."
LABEL "com.puppet.nebula.sdk.version"="v1"
