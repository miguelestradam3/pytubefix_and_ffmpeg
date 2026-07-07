# 🎥 YouTube Downloader and Metadata Exporter

A Python application that downloads YouTube videos using **pytubefix** and organizes video information with **pandas**. This project provides a simple workflow for downloading videos while storing metadata in a structured format for further analysis or record keeping.

> **⚠️ Important:** This project **requires FFmpeg to be installed and available in your system's PATH**. Without FFmpeg, audio/video processing and merging will not work correctly.

---

## 📌 Features

- Download YouTube videos
- Download audio streams
- Automatic audio/video merging (requires FFmpeg)
- Export video metadata using Pandas
- Clean and easy-to-understand Python code
- Jupyter Notebook or Python script compatible

---

## 🛠 Technologies Used

- Python
- pytubefix
- pandas
- FFmpeg

---

## 📚 Libraries

```python
pytubefix
pandas
```

---

## 🚀 Getting Started

## Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pytubefix pandas
```

---

# ⚠️ FFmpeg Installation (Required)

This project **will not function correctly without FFmpeg**.

FFmpeg is required for:

- Merging audio and video streams
- Processing downloaded media
- Handling high-quality downloads

### Windows

1. Download FFmpeg from:

https://ffmpeg.org/download.html

or

https://www.gyan.dev/ffmpeg/builds/

2. Extract the downloaded archive.

3. Add the **bin** folder to your system's **PATH**.

Example:

```
C:\ffmpeg\bin
```

4. Restart your terminal or IDE.

Verify the installation:

```bash
ffmpeg -version
```

If installed correctly, you should see the FFmpeg version information.

---

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install ffmpeg
```

Verify:

```bash
ffmpeg -version
```

---

### macOS

Using Homebrew:

```bash
brew install ffmpeg
```

Verify:

```bash
ffmpeg -version
```

---

## ▶️ Running the Project

```bash
python main.py
```

---

## 📊 Example Output

The application may generate a CSV file containing video information such as:

| Title | Author | Duration | Views |
|-------|--------|----------|-------|
| Example Video | Example Channel | 12:34 | 150,000 |

---

## 📁 Output

Downloaded files are typically stored inside:

```
downloads/
```

Metadata can be exported to:

```
data/videos.csv
```

---

## 🎯 Learning Objectives

This project demonstrates how to:

- Download YouTube content using pytubefix
- Process media files with FFmpeg
- Store structured data using Pandas
- Work with CSV files
- Build Python automation scripts

---

## 🔮 Future Improvements

- Playlist downloading
- Batch downloads from CSV
- Download progress indicator
- GUI interface
- Command-line arguments
- Multiple output formats
- Automatic subtitle downloading
- Thumbnail downloading

---

## ❗ Troubleshooting

### FFmpeg not found

If you receive an error similar to:

```
ffmpeg was not found
```

or

```
FileNotFoundError: ffmpeg
```

Make sure:

- FFmpeg is installed.
- FFmpeg has been added to your system's **PATH**.
- Running the following command works from your terminal:

```bash
ffmpeg -version
```

If this command fails, the project will not be able to process downloaded media.


⭐ If you found this project useful, consider giving it a star!

!["Youtube logo](logo.png)
