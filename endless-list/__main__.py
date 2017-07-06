#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sanic.response import json
from sanic import Sanic

app = Sanic()


@app.route("/")
async def test(request):
    return json({"hello": "world"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
