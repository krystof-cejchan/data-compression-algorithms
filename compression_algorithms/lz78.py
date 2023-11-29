def lz78_compress(data):
    dictionary = {}
    compressed_data = []
    buffer = ""

    for char in data:
        buffer += char
        if buffer not in dictionary:
            if buffer[:-1] in dictionary:
                compressed_data.append((dictionary[buffer[:-1]], buffer[-1]))
            else:
                compressed_data.append((0, buffer[-1]))
            dictionary[buffer] = len(dictionary) + 1
            buffer = ""

    if buffer:
        compressed_data.append((dictionary[buffer[:-1]], buffer[-1]))

    return compressed_data


def lz78_decompress(compressed_data):
    dictionary = {}
    decompressed_data = []
    buffer = ""

    for entry in compressed_data:
        index, char = entry
        substring = dictionary.get(index, "") + char
        decompressed_data.append(substring)
        dictionary[len(dictionary) + 1] = substring

    return "".join(decompressed_data)


# Example usage:
original_data = "ABABABABA"
compressed_data = lz78_compress(original_data)
print("Original Data:", original_data)
print("Compressed Data:", compressed_data)
print("Decompressed Data:", lz78_decompress(compressed_data))
