# Module 10 — Polymorphism and Duck Typing

Polymorphism is the third major pillar of Object-Oriented Programming. In Python, it gives you extraordinary flexibility to write clean, reusable, and extensible code.

---

## 1. Concept Overview: What is Polymorphism?

The word **Polymorphism** comes from two Greek words:
- **Poly** = Many
- **Morph** = Forms

In programming, polymorphism means:
> **The ability of different classes to respond to the exact same method call, each in its own unique way.**

### Analogy: The Universal Remote Control
Think of a **Power Button** on a universal TV remote control.
- When you point it at a **Television** and press Power, the TV turns on its screen and speakers.
- When you point it at an **Air Conditioner** and press Power, the AC starts blowing cool air.
- When you point it at an **Audio Receiver** and press Power, the stereo lights up.

You pressed the **exact same button** (`power()`), but each device responded differently according to its nature. You did not need three separate remotes with different buttons!

```
                Caller: process_payment(gateway, 500)
                                   |
            +----------------------+----------------------+
            |                      |                      |
            v                      v                      v
+-----------------------+ +-----------------------+ +-----------------------+
|  class CreditCard:    | |  class UPIPayment:    | |  class CryptoWallet:  |
|    def pay(amount)    | |    def pay(amount)    | |    def pay(amount)    |
|    (charges card)     | |    (scans QR code)    | |    (signs blockchain) |
+-----------------------+ +-----------------------+ +-----------------------+
```

---

## 2. Polymorphism Eliminates Ugly `if/elif` Chains

Consider how you would process payments **without** polymorphism:

```python
# PROCEDURAL ANTI-PATTERN (Ugly, fragile code):
def checkout(payment_type, details, amount):
    if payment_type == "credit_card":
        charge_credit_card(details["card_num"], amount)
    elif payment_type == "upi":
        send_upi_request(details["vpa"], amount)
    elif payment_type == "crypto":
        transfer_crypto(details["wallet"], amount)
    # What happens when we add 10 more payment methods?
    # This function grows to 500 lines and breaks constantly!
```

Every time a new payment method is introduced, you are forced to modify existing code.

Now look at the **Polymorphic Solution**:
```python
# CLEAN POLYMORPHIC PATTERN:
def checkout(payment_gateway, amount):
    # This function doesn't care WHAT class payment_gateway is!
    # It only cares that payment_gateway has a pay() method!
    return payment_gateway.pay(amount)
```

Now you can add 50 new payment methods tomorrow without changing a single line of `checkout()`! This satisfies the famous **Open/Closed Principle**: *Open for extension, closed for modification*.

---

## 3. Python's Superpower: Duck Typing

In rigid languages like Java or C++, polymorphism requires all classes to inherit from a shared base class or implement a strict interface.

In **Python**, polymorphism is much more flexible thanks to **Duck Typing**:

> *"If it walks like a duck and quacks like a duck, then it's a duck!"*

Python does not check an object's class inheritance tree. Python only asks:
**"Does this object have the method I'm trying to call right now?"** If yes, it runs it!

### Duck Typing in Action:
Notice that these classes **do not share any parent class**, yet they work together polymorphically:

```python
class MP3Player:
    def play(self, file):
        return f"Playing MP3 audio: {file}"

class VideoPlayer:
    def play(self, file):
        return f"Streaming MP4 video: {file}"

class StreamingRadio:
    def play(self, file):
        return f"Broadcasting live stream: {file}"

# A function that operates on ANY object with a play() method:
def start_media(player, media_file):
    print(player.play(media_file))

# They all work seamlessly!
start_media(MP3Player(), "song.mp3")
start_media(VideoPlayer(), "movie.mp4")
start_media(StreamingRadio(), "rock_channel")
```

---

## 4. Python Philosophy: EAFP vs. LBYL

In Python, there are two distinct ways to interact with objects:

### 1. LBYL: "Look Before You Leap"
You check if an object is capable before calling the method:
```python
if hasattr(obj, "play"):
    obj.play()
else:
    print("Cannot play!")
```

### 2. EAFP: "Easier to Ask for Forgiveness than Permission" (The Pythonic Way!)
Assume the method exists, run it, and catch the exception if it doesn't:
```python
try:
    obj.play()
except AttributeError:
    print("This object cannot play media!")
```
Python developers strongly favor **EAFP** because it is faster and avoids redundant type checks.

---

## 5. Common Beginner Pitfalls

### Pitfall 1: Inconsistent Method Signatures
Polymorphism requires methods to accept compatible arguments.
```python
class Dog:
    def speak(self):  # Takes 0 arguments (besides self)
        return "Woof"

class Human:
    def speak(self, language):  # Takes 1 argument!
        return f"Speaking in {language}"

# DISASTER: Calling both in a uniform loop:
for creature in [Dog(), Human()]:
    print(creature.speak())  # Crashes on Human: TypeError: missing 1 required argument!
```
Keep polymorphic method signatures consistent across all classes that share the interface.

---

### Pitfall 2: Overusing `isinstance()` Checks
If you find yourself writing:
```python
if isinstance(pet, Dog):
    pet.bark()
elif isinstance(pet, Cat):
    pet.meow()
```
You are completely missing the point of polymorphism! Give both classes a shared method name (`make_sound()`) and call `pet.make_sound()`.

---

## 6. Key Takeaways Checklist

Before opening `problems.md`:
- [ ] What is polymorphism in simple terms?
- [ ] What is the meaning of "Duck Typing"?
- [ ] Why does polymorphism make code easier to extend in the future?
- [ ] Why should you avoid chains of `if/elif isinstance(...)`?
- [ ] What does Python's EAFP principle mean?

---

## Ready to Practice!
Now open **[problems.md](problems.md)** and practice writing flexible polymorphic code!
