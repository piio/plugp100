class TapoRequest(object):
    def __init__(self, method, params):
        self.method = method
        self.params = params

    def get_params(self):
        return self.params

    def get_method(self):
        return self.method

    def set_request_time_milis(self, t: float):
        pass#self.requestTimeMils = t

    def set_terminal_uuid(self, uuid: str):
        pass#self.terminalUUID = uuid
