from dopy.manager import DoError


class DoMissingVariableError(DoError):
    def __init__(self, message=None):
        self.message = message
        if message is None:
            self.message = "Missing Required Variable"
        super(DoMissingVariableError, self).__init__(self.message)


class DoEnvironmentError(DoError):
    def __init__(self, message=None):
        self.message = message
        if message is None:
            self.message = "Could not find values for DigitalOcean environment. \
                Required for v2: DO_API_TOKEN. Required for v1: DO_CLIENT_ID, DO_API_KEY"
        super(DoEnvironmentError, self).__init__(self.message)
