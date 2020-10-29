# foobar-trigger-template

This is the template webhook trigger for the foobar integration.

## Data Emitted

| Name             | Data type | Description                                |
|------------------|-----------|--------------------------------------------|
| webhook_contents | JSON      | The entire contents of the webhook payload |

## Usage

For a complete usage guide, see the [Using triggers in workflows](https://relay.sh/docs/using-workflows/using-triggers/) documentation.

```yaml
triggers:
- name: default-trigger
  image: relaysh/foobar-trigger-template
  binding:
    parameters:
      webhook: !Data webhook_contents
```
