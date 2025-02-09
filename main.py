import os
import yt_dlp as yd

def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"\rDownloading: {d['_percent_str']} - {d['_eta_str']} remaining", end='', flush=True)
    elif d['status'] == 'finished':
        print("\nDownload completed!")

def download_video(url, save_path, format_choice):
    options = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),  # Save video with title name
        'progress_hooks': [progress_hook],  # Show download progress
        'writethumbnail': True,  # Download video thumbnail
        'postprocessors': [{
            'key': 'FFmpegMetadata'  # Embed metadata in video file
        }]
    }

    # Format selection
    if format_choice == '1':
        options['format'] = 'bestvideo+bestaudio'  # Best quality video
    elif format_choice == '2':
        options['format'] = 'bestaudio'  # Audio only
        options['postprocessors'].append({
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        })  # Convert to MP3
    else:
        options['format'] = 'best'  # Default best format available

    try:
        with yd.YoutubeDL(options) as ydl:
            print("Starting Download ....")
            ydl.download([url])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube Video URL: ")

    # Choose download format
    print("\nChoose format:")
    print("1 - Best Video + Audio (Highest Quality)")
    print("2 - Audio Only (MP3)")
    print("3 - Best Available Format (Default)")
    format_choice = input("Enter option (1/2/3): ")

    # Choose save location
    save_path = input("Enter download path (leave blank for current directory): ") or os.getcwd()

    download_video(video_url, save_path, format_choice)

    print(f"Download completed! The file is saved in: {save_path}")
