"""
## Problem 3 — Media Player

### Requirements

Class AudioFile:
   __init__(self, filename, duration_seconds)
   play(): Prints "Playing audio: <filename> (<duration>s)"
   get_info(): Returns "Audio: <filename>"

Class VideoFile:
   __init__(self, filename, resolution)
   play(): Prints "Playing video: <filename> at <resolution>"
   get_info(): Returns "Video: <filename> (<resolution>)"

Class Podcast:
   __init__(self, title, episode, host)
   play(): Prints "Playing podcast: <title> - Episode <episode> by <host>"
   get_info(): Returns "Podcast: <title> Ep.<episode>"

Class MediaPlayer:
   __init__(self, name)
   self.playlist = []
   add_to_playlist(media): Appends any media object.
   play_all(): Calls .play() on each item.
   show_playlist(): Prints numbered list using .get_info()

### Sample Run
player = MediaPlayer("My Player")
player.add_to_playlist(AudioFile("song.mp3", 180))
player.add_to_playlist(VideoFile("lecture.mp4", "1080p"))
player.add_to_playlist(Podcast("Tech Talk", 42, "Priya"))

player.show_playlist()
# 1. Audio: song.mp3
# 2. Video: lecture.mp4 (1080p)
# 3. Podcast: Tech Talk Ep.42

player.play_all()

----------------------------------------------------------------------
Write your solution below. Refer to solutions.md only when stuck.
----------------------------------------------------------------------
"""

# Write your solution here:

