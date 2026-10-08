# 🔒 Steganography Secret Messenger

A Python application that hides encrypted secret messages inside images using LSB (Least Significant Bit) steganography and XOR PIN-based encryption.

---

## 📁 Project Structure

| File | Purpose |
|---|---|
| [`new.py`](file:///c:/Users/RAJ/python/mini%20project/steganography_app/new.py) | **Encoder Engine** — Hides encrypted messages inside image pixels |
| [`decode.py`](file:///c:/Users/RAJ/python/mini%20project/steganography_app/decode.py) | **Decoder Engine** — Extracts and decrypts hidden messages from image pixels |
| [`encoder_gui.py`](file:///c:/Users/RAJ/python/mini%20project/steganography_app/encoder_gui.py) | **Sender Interface** — Cyber-dark UI to pick images, enter message + PIN, and save |
| [`decoder_gui.py`](file:///c:/Users/RAJ/python/mini%20project/steganography_app/decoder_gui.py) | **Receiver Interface** — Cyber-dark UI to upload image, enter PIN, and reveal secret |

---

## 🚀 How to Run

### 1. Hide a Secret Message (Sender)
```bash
python encoder_gui.py
```
1. Click **Browse Image** to select any picture.
2. Enter your secret message.
3. Enter your secret PIN number (e.g. `1234`).
4. Click **Hide & Save Image** to save `secret.png`.

---

### 2. Reveal the Secret Message (Receiver)
```bash
python decoder_gui.py
```
1. Click **Select Encrypted Image** and pick `secret.png`.
2. Enter the matching PIN number (`1234`).
3. Click **Reveal Secret Message** to see the secret text appear on screen!

