import ytmusicapi
import mpv

player = mpv.MPV(vid='no')
ytm = ytmusicapi.YTMusic('oauth.json')

liked_songs = ytm.get_liked_songs()

class Playlist:
    """
    built playlist from youtube liked songs.
    """
    def __init__(self, liked_songs):
        self.id = liked_songs['id']
        self.title = liked_songs['title']
        self.tracks = liked_songs['tracks']

    @staticmethod
    def get_url(track):
        """
        get url from track.
        """
        url = f'https://www.youtube.com/watch?v={track["videoId"]}'
        return url
    
    def _random_play(self, player=player):
        """
        play random song from playlist.
        """
        import random
        track = random.choice(self.tracks)
        title = track['title']
        url = self.get_url(track)
        print(f'Playing:  {title}')
        player.play(url)
        player.wait_for_playback()
        player.stop()

    def random_play(self, player=player):
        """
        play random song from playlist.
        """
        while True:
            self._random_play(player)

    def save_csv(self):
        """
        save playlist to csv file.
        """
        import csv
        with open(f'ytmusic.csv', 'w') as f:
            writer = csv.writer(f)
            for track in self.tracks:
                title = track['title']
                url = self.get_url(track)
                writer.writerow([title, url])

def ytmusic_play(songs=liked_songs):
    """
    play random song from youtube playlist.
    """
    playlist = Playlist(songs)
    playlist.random_play()

def ytmusic_save_csv(songs=liked_songs):
    """
    save playlist to csv file.
    """
    playlist = Playlist(songs)
    playlist.save_csv()

if __name__ == '__main__':
    ytmusic_save_csv()
    ytmusic_play()