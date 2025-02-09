# YouTube Video Downloader

This is a simple Python script that allows you to download YouTube videos in various formats, including best video + audio, audio-only (MP3), and the best available format. It utilizes the `yt-dlp` library for downloading.

## Features

- Download YouTube videos in the best available quality.
- Extract audio in MP3 format.
- Save videos with their titles as filenames.
- Download and embed video thumbnails and metadata.
- Display real-time download progress.

## Requirements

- Python 3.6+
- `yt-dlp`
- `ffmpeg` (for audio conversion and metadata processing)

## Installation

1. Install Python (if not already installed): [Download Python](https://www.python.org/downloads/)
2. Install `yt-dlp`:
   ```sh
   pip install yt-dlp
   ```
3. Install `ffmpeg` (if not already installed):
   - **Windows**: Download from [FFmpeg official site](https://ffmpeg.org/download.html) and add it to your system PATH.
   - **Mac (Homebrew)**:
     ```sh
     brew install ffmpeg
     ```
   - **Linux (Debian/Ubuntu)**:
     ```sh
     sudo apt install ffmpeg
     ```

## Usage

Run the script with:

```sh
python downloader.py
```

### Steps:

1. Enter the YouTube video URL.
2. Choose the download format:
   - `1`: Best Video + Audio (Highest Quality)
   - `2`: Audio Only (MP3)
   - `3`: Best Available Format (Default)
3. Choose the download path (leave blank for the current directory).
4. The download progress will be displayed, and the file will be saved in the chosen directory.

## Example Output

```
Enter the YouTube Video URL: https://www.youtube.com/watch?v=example

Choose format:
1 - Best Video + Audio (Highest Quality)
2 - Audio Only (MP3)
3 - Best Available Format (Default)
Enter option (1/2/3): 1

Enter download path (leave blank for current directory):
Starting Download ....
Downloading: 45.3% - 00:30 remaining
Download completed!
Download completed! The file is saved in: /your/download/path
```

## License

This project is licensed under the MIT License. Feel free to modify and use it as needed.

## Contributing

Pull requests are welcome. C major changes, please open an issue first to discuss what you would like to change.

## Disclaimer

This script is for personal use only. Downloading videos from YouTube may violate YouTube's terms of service. Ensure you have permission before downloading copyrighted content.

---

Enjoy downloading! 🚀

