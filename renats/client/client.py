from .base import BaseNatsClient


class NatsClient(BaseNatsClient):
    async def connect(self, host: str, port: int):
        pass

    async def publish(
            self,
            subject: str,
            payload: bytes = None,
            reply_subject: str = None,
            headers: dict[str, str] = None
    ):
        pass
