class AudioFileMixin:
    def play_audio(self):
        if not hasattr(self, "audio_tracks"):
            raise AttributeError("Отствует поле 'audio_tracks'")
        print(f"Воспроизведение аудио для {self.__class__.__name__}")
        for track in self.audio_tracks:
            print(f"\t{track}")

class VideoFileMixin:
        def play_video(self):
            if not hasattr(self, "video_files"):
                raise AttributeError("Отсутствует поле 'video_files'")
            print(f"Воспроизведение видео для {self.__class__.__name__}")
            for video in self.video_files:
                print(f"\t{video}")

class MediaPlayer(AudioFileMixin):
    def __init__(self, audio_tracks):
        self.audio_tracks = audio_tracks


class Laptop(AudioFileMixin, VideoFileMixin):
    def __init__(self, audio_tracks, video_files):
        self.audio_tracks = audio_tracks
        self.video_files = video_files


tracks = ["AC/DC - Thunderstruck.wav", "Metallica - Master of Puppets.mp3", "Bring Me The Horizon - Chelsea Smile.flac"]
movies = ["Lord of the Rings.mp4", "Interstellar.mov", "Godfather.avi"]

player = MediaPlayer(tracks)
laptop = Laptop(tracks, movies)

laptop.play_audio()
laptop.play_video()
player.play_audio()

try:
    player.play_video()
except AttributeError:
    print("Player has no attribute 'play_video'")
