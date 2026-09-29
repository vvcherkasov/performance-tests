from pydantic import BaseModel

class GRPCClientConfig(BaseModel):
    port: int
    host: str

    @property
    def client_url(self):
        return f"{self.host}:{self.port}"