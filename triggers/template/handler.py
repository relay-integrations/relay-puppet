# simple webhook responder that just puts the entire
# content of the webhook into a parameter for use by a 
# workflow.

from relay_sdk import Interface, WebhookServer
from quart import Quart, request, jsonify, make_response

relay = Interface()
app = Quart('my-app')

@app.route('/', methods=['POST'])
async def handler():

    payload = await request.get_json()
    if payload is None:
        return {'message': 'not a valid webhook'}, 400, {}

    relay.events.emit({
          'webhook_contents': payload
      })

    return {'message': 'success'}, 200, {}

if __name__ == '__main__':
    WebhookServer(app).serve_forever()
