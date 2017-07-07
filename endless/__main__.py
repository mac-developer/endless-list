#!/usr/bin/env python3
from sanic.response import json
from sanic import Sanic

APP = Sanic()
TODO = []


@APP.route("/", methods=["POST", "GET"])
@APP.route("/<index:int>", methods=["PUT", "GET", "DELETE"])
async def main(request, index=None):
    try:
        return json({
            'GET': lambda: None if index is None else TODO[index],
            'DELETE': lambda: (TODO.pop(index), None)[1],
            'POST': lambda: TODO.append(request.form['item'][0]),
            'PUT': lambda: TODO.__setitem__(index, request.form['item'][0])
        }[request.method]() or TODO)
    except IndexError:
        return json({'error': 'Not found'}, status=404)
    except KeyError as err:
        return json({'error': 'Invalid request {}'.format(err)}, status=400)

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=8000)
