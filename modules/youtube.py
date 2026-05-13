class YoutubeClass:

    #Attributes
    os = __import__("os")
    pytubefix = __import__("pytubefix")
    flag = False

    #Methods
    def __init__(self):
        print("The process has started...")
    
    def download_video(self, url:str)->bool:
        result = False
        try:
            import subprocess
            import os

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

            subprocess.run(command)

            os.remove(downloaded)

            print("Done:", output)

            result = True
            return result
        
        except Exception as error:

            print ("ERROR: {}".format(error))
            return result
    

    def __del__(self):
        print("The process has finished...")
