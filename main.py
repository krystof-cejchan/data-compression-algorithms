import os.path
import tkinter
import tkinter as tk
from tkinter import filedialog


class FileCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Compressor")

        # Create GUI elements
        self.label = tk.Label(root, text="Choose a file to compress:")
        self.label.pack(pady=10)
        self.label_size = tk.Label(root, text="")
        self.label_size.pack(pady=10)

        self.choose_button = tk.Button(root, text="Choose File", command=self.choose_file)
        self.choose_button.pack(pady=10)
        self.compression_var = tk.StringVar()
        self.compression_var.set('H')  # Default compression algorithm
        self.radio = tk.Radiobutton(root, text="Huffman", variable=self.compression_var, value='H')
        self.radio.pack(pady=5)
        self.radio = tk.Radiobutton(root, text="LL77", variable=self.compression_var, value="LL77")
        self.radio.pack(pady=5)
        self.radio = tk.Radiobutton(root, text="LL78", variable=self.compression_var, value="LL78")
        self.radio.pack(pady=5)
        self.compress_button = tk.Button(root, text="Compress", command=self.compress_file)
        self.compress_button.pack(pady=10)

    def choose_file(self):
        file_path = filedialog.askopenfilename()
        self.file_path = file_path
        self.label.config(text=f"Selected file: {file_path}")
        self.label_size.config(text=f"File size (kB): {round(os.path.getsize(file_path) / 1000)}")

    def compress_file(self):
        if not hasattr(self, 'file_path'):
            tk.messagebox.showwarning("Error", "Please choose a file first.")
            return

        print(self.compression_var.get())

        # file_path = self.file_path
        # for option in compression_options:
        #     compression_name, extension, compression_function = option
        #     compressed_file_path = file_path + extension
        #
        #     with open(file_path, 'rb') as f_in, open(compressed_file_path, 'wb') as f_out:
        #         compressed_data = compression_function(f_in.read())
        #         f_out.write(compressed_data)
        #
        #     tk.messagebox.showinfo("Success", f"File compressed using {compression_name}. \n"
        #                                       f"Compressed file saved as: {compressed_file_path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileCompressorApp(root)
    root.mainloop()
