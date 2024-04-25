from flask import jsonify


class JSONResponse:
    def __init__(self, status, content_type, data):
        self.status = status
        self.content_type = content_type
        self.data = data

    def __call__(self, *args, **kwargs):
        return f"" \
               f"Status : {self.status} " \
               f"Content-Type: {self.content_type}, " \
               f"data : {jsonify(self.data)}"

