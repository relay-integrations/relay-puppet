# foobar-step-template

This step is just a template, but at least it's well-documented!

## Specification

This step expects the following fields in the `spec` section of a workflow step definition that uses it:

| Setting   | Data type | Description       | Default   | Required |
|-----------|-----------|-------------------|-----------|----------|
|`message`  | String    | A message to emit | "default" | No       |

## Usage

```yaml
step:
  name: emit-message
  image: relaysh/foobar-step-template
  spec:
    message: "This overrides the default"
```
