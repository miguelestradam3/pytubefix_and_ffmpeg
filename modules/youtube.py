class YoutubeClass:

    def __init__(self):
        print("The process has started...")
        self.subprocess = __import__("subprocess")
        self.os = __import__("os")
        self.pytubefix = __import__("pytubefix")
        self.flag = False
    
    def download_video(self, url:str)->bool:
        result = False
        try:

            yt = self.pytubefix.YouTube(str(url))

            stream = yt.streams.filter(only_audio=True).first()

            downloaded = stream.download(filename="temp_audio")

            output = f"{yt.title}.m4a"

            command = [
                "ffmpeg",
                "-i", downloaded,
                "-vn",
                "-c:a", "aac",
                "-b:a", "256k",
                "-ar", "44100",
                "-movflags", "+faststart",
                
                # Apple metadata
                "-metadata", f"title={yt.title}",
                "-metadata", f"artist={yt.author}",
                "-metadata", "album=YouTube",
                
                output
            ]

            self.subprocess.run(command)

            self.os.remove(downloaded)

            print("Done:", output)

            result = True
            return result
        
        except Exception as error:

            print ("ERROR: {}".format(error))
            return result
    

    def __del__(self):
        print("The process has finished...")
