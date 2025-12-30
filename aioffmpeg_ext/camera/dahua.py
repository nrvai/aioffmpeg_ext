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
    channel: int
    subtype: int

    def __init__(
        self: Self,
        *,
        host: str,
        port: Optional[int] = None,
        authentication: Optional[Authentication] = None,
        channel: Optional[int] = None,
        subtype: Optional[int] = None
    ) -> None:
        self.host = host
        self.port = port
        self.authentication = authentication
        self.channel = channel if channel is not None else 1
        self.subtype = subtype if subtype is not None else 0

    def rtsp(self: Self) -> aioffmpeg.source.rtsp.Source:
        return aioffmpeg.source.rtsp.Source(
            host=self.host,
            port=self.port,
            authentication=self.authentication,
            path="/cam/realmonitor",
            query={
                "channel": str(self.channel),
                "subtype": str(self.subtype)
            }
        )
