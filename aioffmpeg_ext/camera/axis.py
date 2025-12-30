from typing import Optional, Self

import aioffmpeg.source.rtsp

from aioffmpeg.source.common import Authentication


__all__ = (
    "Source",
)


class Source:
    host: str
    port: Optional[int]
    authentication: Optional[Authentication]

    def __init__(
        self: Self,
        *,
        host: str,
        port: Optional[int] = None,
        authentication: Optional[Authentication] = None
    ) -> None:
        self.host = host
        self.port = port
        self.authentication = authentication

    def rtsp(self: Self) -> aioffmpeg.source.rtsp.Source:
        return aioffmpeg.source.rtsp.Source(
            host=self.host,
            port=self.port,
            authentication=self.authentication,
            path="/axis-media/media.amp"
        )
