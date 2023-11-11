import tkinter as tk
from tkinter import filedialog
import gzip
import lzma


class FileCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Compressor")

        # Create GUI elements
        self.label = tk.Label(root, text="Choose a file to compress:")
        self.label.pack(pady=10)

        self.choose_button = tk.Button(root, text="Choose File", command=self.choose_file)
        self.choose_button.pack(pady=10)
        self.compression_var = tk.StringVar()
        self.compression_var.set('H')  # Default compression algorithm
        self.gzip_radio = tk.Radiobutton(root, text="Huffman", variable=self.compression_var, value='H')
        self.gzip_radio.pack(pady=5)
        self.lzma_radio = tk.Radiobutton(root, text="LZMA", variable=self.compression_var, value="LZMA")
        self.lzma_radio.pack(pady=5)
        self.compress_button = tk.Button(root, text="Compress", command=self.compress_file)
        self.compress_button.pack(pady=10)

    def choose_file(self):
        file_path = filedialog.askopenfilename()
        self.file_path = file_path
        self.label.config(text=f"Selected file: {file_path}")

    def compress_file(self):
        if not hasattr(self, 'file_path'):
            tk.messagebox.showwarning("Error", "Please choose a file first.")
            return

        compression_options = [
            ("Gzip", ".gz", gzip.compress),
            ("LZMA", ".xz", lzma.compress),
            # Add more compression algorithms as needed
        ]

        file_path = self.file_path
        for option in compression_options:
            compression_name, extension, compression_function = option
            compressed_file_path = file_path + extension

            with open(file_path, 'rb') as f_in, open(compressed_file_path, 'wb') as f_out:
                compressed_data = compression_function(f_in.read())
                f_out.write(compressed_data)

            tk.messagebox.showinfo("Success", f"File compressed using {compression_name}. \n"
                                              f"Compressed file saved as: {compressed_file_path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileCompressorApp(root)
    root.mainloop()
