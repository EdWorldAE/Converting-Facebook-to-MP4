import os
import subprocess
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class FBVideoDownloaderApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Facebook Video Downloader")

        self.url_label = ttk.Label(self, text="Video URL:")
        self.url_label.pack(pady=15)

        self.url_entry = ttk.Entry(self, width=50)
        self.url_entry.pack(pady=15)

        self.ffmpeg_path_label = ttk.Label(self, text="Path to ffmpeg:")
        self.ffmpeg_path_label.pack(pady=15)

        self.ffmpeg_path_entry = ttk.Entry(self, width=50)
        self.ffmpeg_path_entry.pack(pady=5)

        self.ffmpeg_path_btn = ttk.Button(self, text="Browse", command=self.browse_ffmpeg)
        self.ffmpeg_path_btn.pack(pady=5)

        self.yt_dlp_path_label = ttk.Label(self, text="Path to yt-dlp:")
        self.yt_dlp_path_label.pack(pady=15)

        self.yt_dlp_path_entry = ttk.Entry(self, width=50)
        self.yt_dlp_path_entry.pack(pady=5)

        self.yt_dlp_path_btn = ttk.Button(self, text="Browse", command=self.browse_yt_dlp)
        self.yt_dlp_path_btn.pack(pady=5)

        self.save_path_label = ttk.Label(self, text="Save Video to:")
        self.save_path_label.pack(pady=15)

        self.save_path_entry = ttk.Entry(self, width=50)
        self.save_path_entry.pack(pady=5)

        self.save_path_btn = ttk.Button(self, text="Browse", command=self.browse_save_path)
        self.save_path_btn.pack(pady=5)

        self.download_btn = ttk.Button(self, text="Download Video", command=self.download_video)
        self.download_btn.pack(pady=20)

    def browse_ffmpeg(self):
        ffmpeg_path = filedialog.askopenfilename()
        if ffmpeg_path:
            self.ffmpeg_path_entry.delete(0, tk.END)
            self.ffmpeg_path_entry.insert(0, ffmpeg_path)

    def browse_yt_dlp(self):
        yt_dlp_path = filedialog.askopenfilename()
        if yt_dlp_path:
            self.yt_dlp_path_entry.delete(0, tk.END)
            self.yt_dlp_path_entry.insert(0, yt_dlp_path)

    def browse_save_path(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        if save_path:
            self.save_path_entry.delete(0, tk.END)
            self.save_path_entry.insert(0, save_path)

    def download_video(self):
        url = self.url_entry.get()
        ffmpeg_path = self.ffmpeg_path_entry.get()
        yt_dlp_path = self.yt_dlp_path_entry.get()
        save_path = self.save_path_entry.get()

        if not url or not ffmpeg_path or not yt_dlp_path or not save_path:
            messagebox.showwarning("Warning", "Please fill out all fields!")
            return

        cmd = [
            yt_dlp_path,
            '--merge-output-format', 'mp4',
            '--ffmpeg-location', ffmpeg_path,
            '-o', save_path,
            url
        ]

        try:
            subprocess.run(cmd, check=True)
            messagebox.showinfo("Success", "Download complete!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app = FBVideoDownloaderApp()
    app.mainloop()
