from PIL import Image

def encrypt(message, key):
    k=key%256
    result=""
    for char in message:
        result+=chr(ord(char)^k)
    return result

def modify_color(color, bit):
    """Set the LSB of `color` to match `bit`, clamping to [0, 255]."""
    bit = int(bit)
    if color % 2 != bit:
        if bit == 1:
            color += 1
        else:
            color -= 1
    # Clamp to valid pixel range so we never get -1 or 256
    return max(0, min(255, color))


def hide_message(image_path,message,key,output_path="secret.png"):
     img = Image.open(image_path)
     width, height = img.size
     full_message=message+"#######"
     if len(full_message) >width * height * 3 // 8:
        return False,"message too long for the image!"

     key = int(key)
     encrypted_message = encrypt(message, key)
     full_payload=encrypted_message+"#######"
     all_bits = ""
     for char in full_payload:
        all_bits += format(ord(char), "08b")



     bit_index = 0

     for y in range(height):
        for x in range(width):
            # 1. Read the current pixel
            r, g, b = img.getpixel((x, y))

            # 2. Modify red channel
            if bit_index < len(all_bits):
                r = modify_color(r, all_bits[bit_index])
                bit_index += 1

            # 3. Modify green channel
            if bit_index < len(all_bits):
                g = modify_color(g, all_bits[bit_index])
                bit_index += 1

            # 4. Modify blue channel
            if bit_index < len(all_bits):
                b = modify_color(b, all_bits[bit_index])
                bit_index += 1

            # 5. Put the modified pixel back into the image
            img.putpixel((x, y), (r, g, b))

            # All bits are hidden — stop looping
            if bit_index >= len(all_bits):
                break

        # Also break the outer loop once all bits are embedded
        if bit_index >= len(all_bits):
            break

     img.save(output_path)
     return True, f"Message hidden in {output_path} successfully!"


