# PeerTube VOD Architecture

Based on the reverse engineering of the `server/core/models` directory, here is a Mermaid class diagram focusing on the entities involved in **Video on Demand (VOD) uploading and watching** processes.

```mermaid
classDiagram

%% Entities
class UserModel {
  +id: number
  +username: string
  +email: string
}

class AccountModel {
  +id: number
  +name: string
}

class VideoChannelModel {
  +id: number
  +name: string
  +description: string
}

class VideoModel {
  +id: number
  +name: string
  +uuid: string
  +description: string
  +views: number
  +duration: number
}

class VideoFileModel {
  +id: number
  +resolution: number
  +size: number
  +fps: number
  +fileUrl: string
}

class VideoStreamingPlaylistModel {
  +id: number
  +type: string
  +playlistUrl: string
}

class VideoJobInfoModel {
  +id: number
  +state: string
}

class UserVideoHistoryModel {
  +id: number
  +currentTime: number
}

class AccountVideoRateModel {
  +id: number
  +type: string
}

class VideoCommentModel {
  +id: number
  +text: string
}

%% Relationships for Uploading and Organization
UserModel "1" *-- "1" AccountModel : has
AccountModel "1" *-- "0..*" VideoChannelModel : owns
VideoChannelModel "1" o-- "0..*" VideoModel : publishes
VideoModel "1" *-- "0..1" VideoJobInfoModel : tracked by

%% Relationships for Video Storage (VOD files)
VideoModel "1" *-- "0..*" VideoFileModel : contains WebVideo
VideoModel "1" *-- "0..*" VideoStreamingPlaylistModel : contains HLS
VideoStreamingPlaylistModel "1" *-- "1..*" VideoFileModel : has segments

%% Relationships for Watching and Interactions
UserModel "1" *-- "0..*" UserVideoHistoryModel : keeps history
UserVideoHistoryModel "0..*" --> "1" VideoModel : records progress for

AccountModel "1" *-- "0..*" AccountVideoRateModel : authors
AccountVideoRateModel "0..*" --> "1" VideoModel : rates

AccountModel "1" *-- "0..*" VideoCommentModel : authors
VideoCommentModel "0..*" --> "1" VideoModel : on
```

## Key Workflows

### Video Uploading
1. A **User** (authenticated via `UserModel`) selects a **VideoChannel** (owned by their `AccountModel`).
2. A new **VideoModel** is created.
3. Background processing is tracked via **VideoJobInfoModel**.
4. The server creates either direct **VideoFileModel** entries (for standard WebVideo files) or processes the video into HLS streams, creating a **VideoStreamingPlaylistModel** which in turn contains multiple **VideoFileModel** fragments at different resolutions.

### Video Watching
1. The client requests the video and fetches either the `VideoFile` or the `VideoStreamingPlaylist`.
2. As the user watches, progress is recorded in **UserVideoHistoryModel**.
3. The user can interact with the video by liking/disliking (**AccountVideoRateModel**) or leaving comments (**VideoCommentModel**), which are tied back to their **AccountModel**.
