FROM relaysh/core:latest-python
RUN pip install requests
COPY step.py /
CMD [python3, /step.py]

LABEL "org.opencontainers.image.title"="Wait for a Puppet run to complete"
LABEL "org.opencontainers.image.description"="This step waits until a Puppet run initiated by the `run-start` step completes."
LABEL "com.puppet.nebula.sdk.version"="v1"
