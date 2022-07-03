from command_requests.request_base import RequestBase
import wikipedia

class SimpleGoogleRequest(RequestBase):
    def __init__(self):
        super().__init__()

    def execute(self, string=""):
        try:
            return wikipedia.summary(string, sentences = 5)
        except:
            return "I don't see anything. Try re-phrasing"