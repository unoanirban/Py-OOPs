# Practice Problems: Polymorphism and Duck Typing

Learn how the same code can work with objects of different types — as long as they have the right methods.

> **Key idea:** *Polymorphism* means "many forms". A function that calls `obj.make_sound()` works correctly whether `obj` is a `Dog`, `Cat`, or `Cow` — as long as each has a `make_sound()` method. Python doesn't care about the type; it just calls the method. This is also called **duck typing**: "If it walks like a duck and quacks like a duck, it's a duck."

---

## Problem 1 — Payment Methods

### Problem Statement
A retail checkout system must process payments originating from diverse transaction instruments, including credit cards, instant UPI handles, and physical cash. 

Writing separate checkout functions for every payment mechanism (e.g., `pay_with_card`, `pay_with_upi`, `pay_with_cash`) creates fragile code riddled with cumbersome conditional branching. By relying on polymorphism, the checkout processor can instead interact with a single standardized action: `payment_method.pay(amount)`. Regardless of whether an object represents a credit card that masks card numbers, a UPI transaction identified by an address handle, or a cash receipt, any payment object that implements `.pay()` can be passed interchangeably to a single `process_payment` driver function.

### What You'll Learn
- Implementing polymorphic interfaces across independent classes without requiring shared inheritance
- Writing generic processor functions that operate on any object conforming to a method contract
- Applying duck typing principles in payment processing architectures

### Requirements & Specifications

1. **Class `CreditCard`**:
   - Constructor: `__init__(self, card_number, holder_name)`
   - Method `pay(amount)`: Prints `"Paid $<amount> via Credit Card ending in <last 4 digits>."`
     (Hint: `card_number[-4:]` gives the last 4 digits)

2. **Class `UPI`**:
   - Constructor: `__init__(self, upi_id)`
   - Method `pay(amount)`: Prints `"Paid $<amount> via UPI (<upi_id>)."`

3. **Class `Cash`**:
   - Method `pay(amount)`: Prints `"Paid $<amount> in cash."`

4. **Function `process_payment(payment_method, amount)`**:
   - Just calls `payment_method.pay(amount)` — works with any of the above!

### Sample Run
```python
cc = CreditCard("4111222233334444", "Rahul")
upi = UPI("rahul@okaxis")
cash = Cash()

process_payment(cc, 1500)    # Paid $1500 via Credit Card ending in 4444.
process_payment(upi, 800)    # Paid $800 via UPI (rahul@okaxis).
process_payment(cash, 200)   # Paid $200 in cash.

# Works in a loop too:
for method in [cc, upi, cash]:
    process_payment(method, 100)
```

---

## Problem 2 — Notifications

### Problem Statement
An enterprise alert engine dispatches mission-critical event notifications (such as shipment confirmations or security alerts) across multiple delivery channels simultaneously. Recipients may configure their alerts to arrive via Email, SMS text messaging, or mobile push notification services.

Rather than maintaining dedicated dispatcher routines per channel, the dispatch pipeline should treat every communication channel as a pluggable notification provider. Each provider class (`EmailNotification`, `SMSNotification`, `PushNotification`) encapsulates channel-specific endpoints (email address, phone number, device token) and implements a uniform `.send(message)` interface. A centralized batch dispatcher (`send_all`) can then iterate over an arbitrary collection of heterogeneous channel objects and broadcast alerts without concerning itself with their concrete underlying classes.

### What You'll Learn
- Iterating over heterogeneous collections of objects sharing a common method signature
- Decoupling high-level dispatch orchestration from low-level communication protocols
- Leveraging Python's dynamic runtime dispatch for broadcast operations

### Requirements & Specifications

1. **Class `EmailNotification`**:
   - Constructor: `__init__(self, email_address)`
   - Method `send(message)`: Prints `"Email to <email>: <message>"`

2. **Class `SMSNotification`**:
   - Constructor: `__init__(self, phone_number)`
   - Method `send(message)`: Prints `"SMS to <phone>: <message>"`

3. **Class `PushNotification`**:
   - Constructor: `__init__(self, device_token)`
   - Method `send(message)`: Prints `"Push to <device_token>: <message>"`

4. **Function `send_all(channels, message)`**:
   - Takes a **list** of notification objects and a message string.
   - Loops through the list and calls `.send(message)` on each one.

### Sample Run
```python
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

### Problem Statement
A desktop multimedia application needs to manage playlists containing mixed content types. A single playlist can contain compressed audio tracks (with duration metadata), video files (with display resolution specifications), and serialized podcast episodes (with series title and host credits).

Even though these media types represent structurally distinct entities that do not share an inheritance hierarchy, a media player only needs two things from any playable item: a way to display descriptive track info (`.get_info()`) and a way to start playback (`.play()`). By embracing duck typing, the `MediaPlayer` class can aggregate any compatible media objects into a shared playlist, format numbered playlist overviews, and trigger sequential playback seamlessly.

### What You'll Learn
- Embracing duck typing without forcing artificial class inheritance hierarchies
- Aggregating diverse object types within a single container manager class
- Implementing playlist sequencing and index-formatted listing across polymorphic items

### Requirements & Specifications

1. **Class `AudioFile`**:
   - Constructor: `__init__(self, filename, duration_seconds)`
   - Method `play()`: Prints `"Playing audio: <filename> (<duration>s)"`
   - Method `get_info()`: Returns `"Audio: <filename>"`

2. **Class `VideoFile`**:
   - Constructor: `__init__(self, filename, resolution)`
   - Method `play()`: Prints `"Playing video: <filename> at <resolution>"`
   - Method `get_info()`: Returns `"Video: <filename> (<resolution>)"`

3. **Class `Podcast`**:
   - Constructor: `__init__(self, title, episode, host)`
   - Method `play()`: Prints `"Playing podcast: <title> - Episode <episode> by <host>"`
   - Method `get_info()`: Returns `"Podcast: <title> Ep.<episode>"`

4. **Class `MediaPlayer`**:
   - Constructor: `__init__(self, name)`
   - Attribute: `self.playlist = []`
   - Method `add_to_playlist(media)`: Appends any media object to `self.playlist`.
   - Method `play_all()`: Loops through `self.playlist` and calls `.play()` on each.
   - Method `show_playlist()`: Prints each item's `.get_info()`, numbered from 1.

### Sample Run
```python
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
