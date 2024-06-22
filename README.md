# media-server

Docker-Compose and configuration files to run the Media-Server on Raspberry Pi

## Docker containers being used

1. [Heimdall](https://hub.docker.com/r/linuxserver/heimdall) - Dashboard
2. [Plex](https://hub.docker.com/r/linuxserver/plex) - Media player
3. [Transmisison](https://hub.docker.com/r/linuxserver/transmission) - Torrent downloader client
4. [Sonarr](https://hub.docker.com/r/linuxserver/sonarr) - Searches for TV shows to download
5. [Radarr](https://hub.docker.com/r/linuxserver/radarr) - Searches for movies to download
6. [LazyLibrarian](https://hub.docker.com/r/linuxserver/lazylibrarian) - Searches for books to download
7. [Ombi](https://hub.docker.com/r/linuxserver/ombi) - Allows users to request shows/movies to add to Plex/Sonarr/Radarr
8. [Jackett](https://hub.docker.com/r/linuxserver/jackett) - Allows Sonarr/Radarr to search torrent trackers

## Steps to Bring up Media Server

1. Install [docker](https://docs.docker.com/engine/install/)
2. Install [docker-compose](https://docs.docker.com/compose/install/)
3. Download [docker-compose.yml](https://github.com/hdecoded/media-server/blob/main/docker-compose.yml)
4. Open docker-compose.yml for edit
5. Comment/Remove the services you don't need
6. Change the paths in all volumes `/mnt/media/` according to your operating system and a desired location
7. Open Terminal or Command-Prompt.
8. Navigate to the docker-compose.yml location
9. Enter `docker-compose up -d`
10. Run `docker ps` or `docker-compose ps` to check the status of the containers.
