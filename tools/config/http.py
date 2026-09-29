from pydantic import BaseModel, HttpUrl

class HttpClientConfig(BaseModel):
    url: HttpUrl
    timeout: float = 100.0

    @property
    def client_url(self):
        return str(self.url)