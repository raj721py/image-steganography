from PIL import Image

def decrypt(message, key):
    k=key%256
    result = ""
    for char in message:
        result += chr(ord(char) ^ k)
    return result

# ── Open the image that contains the hidden message ──────────────────────────
def extract_message(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    print(f"Reading secret.png  ({width}x{height})")

    # ── Ask user for the decryption key ──────────────────────────────────────────
    key = int(key)

    END_MARKER = "#######"

    # ── Extract bits, decode on the fly, stop at end marker ──────────────────────
    bit_buffer = ""
    message = ""

    outer_done = False

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))

            # Collect 3 bits (one per channel)
            bit_buffer += str(r % 2)
            bit_buffer += str(g % 2)
            bit_buffer += str(b % 2)

            # Decode every complete byte available in the buffer
            while len(bit_buffer) >= 8:
                byte = bit_buffer[:8]
                bit_buffer = bit_buffer[8:]
                char = chr(int(byte, 2))
                message += char

                # Stop as soon as end marker is found
                if message.endswith(END_MARKER):
                    outer_done = True
                    break

            if outer_done:
                break
        if outer_done:
            break

    # ── Strip the end marker, decrypt, and print the real message ────────────────
    if END_MARKER in message:
        encrypted_secret = message[: message.index(END_MARKER)]
        secret = decrypt(encrypted_secret, key)
        return True, secret
    else:
        return False, "No hidden message found (end marker missing)."
