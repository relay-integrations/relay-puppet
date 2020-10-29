#!/bin/sh

# ni is a CLI utility to interact with the service APIs
# from inside a container - see https://relay.sh/docs/cli/ni/

MESSAGE=${default:-$(ni get -p {.message})}

echo "The workflow parameter 'message' was set to: ${MESSAGE}"
