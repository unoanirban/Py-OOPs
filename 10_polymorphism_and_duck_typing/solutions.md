# Solutions: 10 — Polymorphism and Duck Typing

## Problem 1 — Payment Methods

```python
class CreditCard:
    def __init__(self, card_number, holder_name):
        self.card_number = card_number
        self.holder_name = holder_name

    def pay(self, amount):
        last_four = self.card_number[-4:]
        print(f"Paid ${amount} via Credit Card ending in {last_four}.")


class UPI:
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"Paid ${amount} via UPI ({self.upi_id}).")


class Cash:
    def pay(self, amount):
        print(f"Paid ${amount} in cash.")


def process_payment(payment_method, amount):
    payment_method.pay(amount)   # works with any object that has a pay() method!


# Try it out
cc = CreditCard("4111222233334444", "Rahul")
upi = UPI("rahul@okaxis")
cash = Cash()

process_payment(cc, 1500)    # Paid $1500 via Credit Card ending in 4444.
process_payment(upi, 800)    # Paid $800 via UPI (rahul@okaxis).
process_payment(cash, 200)   # Paid $200 in cash.

# All three work in a loop — that's polymorphism!
for method in [cc, upi, cash]:
    process_payment(method, 100)
```

**How it works:**
- `process_payment` doesn't know or care what type `payment_method` is.
- It just calls `.pay(amount)`. Python finds the right `pay()` method for each object at runtime.
- This is duck typing: "Does it have a `pay()` method? Then I can use it."

---

## Problem 2 — Notifications

```python
class EmailNotification:
    def __init__(self, email_address):
        self.email_address = email_address

    def send(self, message):
        print(f"Email to {self.email_address}: {message}")


class SMSNotification:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def send(self, message):
        print(f"SMS to {self.phone_number}: {message}")


class PushNotification:
    def __init__(self, device_token):
        self.device_token = device_token

    def send(self, message):
        print(f"Push to {self.device_token}: {message}")


def send_all(channels, message):
    for channel in channels:
        channel.send(message)


# Try it out
channels = [
    EmailNotification("rahul@gmail.com"),
    SMSNotification("+91-9876543210"),
    PushNotification("device_xyz_789"),
]

send_all(channels, "Your order has been shipped!")
# Email to rahul@gmail.com: Your order has been shipped!
# SMS to +91-9876543210: Your order has been shipped!
# Push to device_xyz_789: Your order has been shipped!
```

---

## Problem 3 — Media Player

```python
class AudioFile:
    def __init__(self, filename, duration_seconds):
        self.filename = filename
        self.duration_seconds = duration_seconds

    def play(self):
        print(f"Playing audio: {self.filename} ({self.duration_seconds}s)")

    def get_info(self):
        return f"Audio: {self.filename}"


class VideoFile:
    def __init__(self, filename, resolution):
        self.filename = filename
        self.resolution = resolution

    def play(self):
        print(f"Playing video: {self.filename} at {self.resolution}")

    def get_info(self):
        return f"Video: {self.filename} ({self.resolution})"


class Podcast:
    def __init__(self, title, episode, host):
        self.title = title
        self.episode = episode
        self.host = host

    def play(self):
        print(f"Playing podcast: {self.title} - Episode {self.episode} by {self.host}")

    def get_info(self):
        return f"Podcast: {self.title} Ep.{self.episode}"


class MediaPlayer:
    def __init__(self, name):
        self.name = name
        self.playlist = []

    def add_to_playlist(self, media):
        self.playlist.append(media)

    def play_all(self):
        for media in self.playlist:
            media.play()

    def show_playlist(self):
        for i, media in enumerate(self.playlist, start=1):
            print(f"{i}. {media.get_info()}")


# Try it out
player = MediaPlayer("My Player")
player.add_to_playlist(AudioFile("song.mp3", 180))
player.add_to_playlist(VideoFile("lecture.mp4", "1080p"))
player.add_to_playlist(Podcast("Tech Talk", 42, "Priya"))

player.show_playlist()
# 1. Audio: song.mp3
# 2. Video: lecture.mp4 (1080p)
# 3. Podcast: Tech Talk Ep.42

player.play_all()
# Playing audio: song.mp3 (180s)
# Playing video: lecture.mp4 at 1080p
# Playing podcast: Tech Talk - Episode 42 by Priya
```

**How it works:**
- `AudioFile`, `VideoFile`, and `Podcast` share NO parent class — they're completely independent.
- Yet `play_all()` works on all of them because they all have `play()` and `get_info()` methods.
- This is the essence of duck typing — the interface (method names) matters, not the type.
