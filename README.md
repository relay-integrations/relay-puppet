# Relay Integration Template

This repository serves as a template for creating new Relay integration repositories. You can [create a new repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template) from this template. Delete this section from your actual README and start below the horizontal line.

## Directory structure

```
.
├── integration.yaml    # metadata describing the integration as a whole
├── LICENSE             # defaults to Apache, replace if that doesn't suit
├── media               # include a svg icon for your integration
├── README.md           # you're reading it right now
├── steps               # subdirectory for containerized steps
│  └── template           # rename this to your own step's name
|     ├── README.md       # detail about how to use this step
│     ├── Dockerfile      # needed to build the container
│     ├── step.sh         # entrypoint script (plus any additional files)
│     └── step.yaml       # step metadata 
├── triggers            # subdirectory for triggers
│  └── template           # rename this to your trigger's name
|     ├── README.md       # detail about how to use this trigger
│     ├── Dockerfile      # ... 
│     ├── handler.py      # Entrypoint webhook handler script
│     └── trigger.yaml    # trigger metadata
└── workflows           # subdirectory for example workflows
   └── example1           # an example workflow
      ├── README.md          # how to use this workflow
      ├── example1.png       # picture of workflow graph from app
      └── example1.yaml      # the workflow itself
```

## Metadata definition

The example metadata files show the minimum required information. The formal specification for the metadata is in the [Relay Integrations RFC](https://github.com/puppetlabs/relay-rfcs/blob/master/content/0006-integration-layout/rfc.md).

## Naming conventions

Steps and triggers should result in containers that follow a naming scheme like:

```
integrationname-{step|trigger}-descriptor
```

This follows from the directory structure, where `integrationname` is the top-level directory and the `steps` and `triggers` (pluralized names of the type of container) have a subdirectory named `descriptor` for each action that's available.

The descriptors can be as simple as `notify` or `respond` but `noun-verb` constructions are also helpful, like `ticket-close`.

Workflows are less rigidly specified since they are likely to be snippets or example code which end-users will need to modify to use.

--------

# Foobar Integration for Relay.sh

This integration allows you to connect Foobar to Relay. Foobar is a ...

## Steps

| Name | Description |
|------|-------------|
| [foobar-step-notify](steps/foobar-step-notify) | This steps sends a notification to Foobar |

## Triggers

| Name | Description |
|------|-------------|
| [foobar-trigger-receive](triggers/foobar-trigger-receive) | Trigger to handle a webhook event from Foobar |

## Workflows

| Name | Description |
|------|-------------|
| [example1.yaml](workflows/example1/) | This workflow shows you how to link the Foobar steps and triggers together |

## Contributing

### Issues

Feel free to submit issues and enhancement requests.

### Contributing Code

In general, we follow the "fork-and-pull" Git workflow.

 1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Pull request** so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!

### License

As indicated by the repository, this project is licensed under Apache 2.0.

