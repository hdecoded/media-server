# media-server
Docker-Compose and configuration files to run the Media-Server on Raspberry Pi

## Docker containers being used

1. [Heimdall](https://hub.docker.com/r/linuxserver/heimdall) - Dashboard
2. [Plex](https://hub.docker.com/r/linuxserver/plex)            - Media player
3. [Transmisison](https://hub.docker.com/r/linuxserver/transmission)    - Torrent downloader client
4. [Sonarr](https://hub.docker.com/r/linuxserver/sonarr)          - Searches for TV shows to download
5. [Radarr](https://hub.docker.com/r/linuxserver/radarr)          - Searches for movies to download
6. [LazyLibrarian](https://hub.docker.com/r/linuxserver/lazylibrarian)   - Searches for books to download
7. [Ombi](https://hub.docker.com/r/linuxserver/ombi)            - Allows users to request shows/movies to add to Plex/Sonarr/Radarr
8. [Jackett](https://hub.docker.com/r/linuxserver/jackett)         - Allows Sonarr/Radarr to search torrent trackers
