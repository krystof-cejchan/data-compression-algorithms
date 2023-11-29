def lz77_compress(input_str, window_size=10):
    compressed_data = []
    i = 0

    while i < len(input_str):
        match_found = False
        match_length = 0
        match_position = 0

        # Search for the longest match within the window
        for j in range(1, min(window_size, i + 1)):
            if input_str[i:i + j] in input_str[max(0, i - window_size):i]:
                match_found = True
                match_length = j
                match_position = i - input_str.rfind(input_str[i:i + j], max(0, i - window_size), i)

        # If a match is found, encode it as (offset, length)
        if match_found:
            compressed_data.append((match_position, match_length))
            i += match_length
        else:
            # No match found, encode the current character as (0, char)
            compressed_data.append((0, input_str[i]))
            i += 1

    return compressed_data


def lz77_decompress(compressed_data):
    decompressed_str = ""

    for (offset, length) in compressed_data:
        if offset == 0:
            decompressed_str += length
        else:
            start = len(decompressed_str) - offset
            for _ in range(length):
                decompressed_str += decompressed_str[start]
                start += 1

    return decompressed_str


# Example usage
input_str = "ABABABABCABABABAB"
compressed_data = lz77_compress(input_str)
print("Compressed data:", compressed_data)

decompressed_str = lz77_decompress(compressed_data)
print("Decompressed string:", decompressed_str)
