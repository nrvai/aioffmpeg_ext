from dataclasses import dataclass
from typing import Literal, Optional, Self, Union

import aioffmpeg.source.rtsp

from aioffmpeg.common.authentication import Authentication


__all__ = (
    "VideoCodec",
    "Overlays",
    "Source"
)


type VideoCodec = Literal["av1", "h264", "h265", "jpeg", "mpeg4"]
type Overlays = Literal["all", "text", "image", "application", "off"]


@dataclass(kw_only=True)
class Source:
    """
    All stream options are available at: https://developer.axis.com/vapix/network-video/video-streaming/#parameter-specification-rtsp-url
    """

    host: str
    port: Optional[int] = None
    authentication: Optional[Authentication] = None

    video_codec: Optional[VideoCodec] = None
    stream_profile: Optional[str] = None
    recording_id: Optional[str] = None
    resolution: Optional[str] = None
    audio: Optional[bool] = None
    camera: Optional[Union[int, str]] = None
    compression: Optional[int] = None
    color: Optional[bool] = None
    color_level: Optional[int] = None
    palette: Optional[str] = None
    rotation: Optional[int] = None
    fps: Optional[int] = None
    pull: Optional[bool] = None
    overlays: Optional[Overlays] = None

    def rtsp(self: Self) -> aioffmpeg.source.rtsp.Source:
        query = {}

        if self.video_codec is not None:
            query["videocodec"] = self.video_codec

        if self.stream_profile is not None:
            query["streamprofile"] = self.stream_profile
        
        if self.recording_id is not None:
            query["recordingid"] = self.recording_id

        if self.resolution is not None:
            query["resolution"] = self.resolution

        if self.audio is not None:
            query["audio"] = str(int(self.audio))

        if self.camera is not None:
            query["camera"] = str(self.camera)

        if self.compression is not None:
            query["compression"] = str(self.compression)

        if self.color is not None:
            query["color"] = str(int(self.color))

        if self.color_level is not None:
            query["colorlevel"] = str(self.color_level)

        if self.palette is not None:
            query["palette"] = self.palette

        if self.rotation is not None:
            query["rotation"] = str(self.rotation)

        if self.fps is not None:
            query["fps"] = str(self.fps)

        if self.pull is not None:
            query["pull"] = str(int(self.pull))

        if self.overlays is not None:
            query["overlays"] = self.overlays

        return aioffmpeg.source.rtsp.Source(
            host=self.host,
            port=self.port,
            authentication=self.authentication,
            path="/axis-media/media.amp",
            query=query
        )
