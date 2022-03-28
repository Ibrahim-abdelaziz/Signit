


def get_json_from_request(request, data=True) -> dict:
    return request.get_json() or dict(data=dict() if data else dict())


def read_from_file(path):
    with open(path, "r") as file:
        return file.read()
