# PeerTube VOD Architecture

Based on the reverse engineering of the `server/core/models` directory, here is a Mermaid class diagram focusing on the entities involved in **Video on Demand (VOD) uploading and watching** processes.

```mermaid
classDiagram

%% Entities
class UserModel {
  <<Sequelize Model>>
  Represents a registered user
}

class AccountModel {
  <<Sequelize Model>>
  Public profile of a user or remote actor
}

class VideoChannelModel {
  <<Sequelize Model>>
  A channel grouping videos
}

class VideoModel {
  <<Sequelize Model>>
  The core video entity
}

class VideoFileModel {
  <<Sequelize Model>>
  Physical video files (MP4/WebM)
  Different resolutions
}

class VideoStreamingPlaylistModel {
  <<Sequelize Model>>
  HLS (HTTP Live Streaming) playlists
}

class VideoJobInfoModel {
  <<Sequelize Model>>
  Tracks background jobs (transcoding, etc.)
}

class UserVideoHistoryModel {
  <<Sequelize Model>>
  Tracks watch progress for users
}

class AccountVideoRateModel {
  <<Sequelize Model>>
  Likes and Dislikes
}

class VideoCommentModel {
  <<Sequelize Model>>
  User comments on videos
}

%% Relationships for Uploading and Organization
UserModel "1" -- "1" AccountModel : has
AccountModel "1" -- "*" VideoChannelModel : owns
VideoChannelModel "1" -- "*" VideoModel : publishes
VideoModel "1" -- "1" VideoJobInfoModel : has (transcoding/uploading jobs)

%% Relationships for Video Storage (VOD files)
VideoModel "1" -- "*" VideoFileModel : contains WebVideo files
VideoModel "1" -- "*" VideoStreamingPlaylistModel : contains HLS playlists
VideoStreamingPlaylistModel "1" -- "*" VideoFileModel : contains HLS segments

%% Relationships for Watching and Interactions
UserModel "1" -- "*" UserVideoHistoryModel : keeps watch history
UserVideoHistoryModel "*" -- "1" VideoModel : records view progress

AccountModel "1" -- "*" AccountVideoRateModel : rates
AccountVideoRateModel "*" -- "1" VideoModel : is rated by

AccountModel "1" -- "*" VideoCommentModel : authors
VideoCommentModel "*" -- "1" VideoModel : commented on
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
