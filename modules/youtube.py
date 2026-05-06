class YoutubeClass:

    #Attributes
    os = __import__("os")
    pytubefix = __import__("pytubefix")
    flag = False
    yt = ""

    #Methods
    def __init__(self):
        print("The process has started...")
    
    def download_video(self, url:str, path:str)->bool:
        result = False
        try:
            # url input from user
            self.yt = self.pytubefix.YouTube(str(url))
            # extract only audio
            video = self.yt.streams.filter(only_audio=True).first()
            # download the file
            out_file = video.download(output_path=path)
            # save the file
            base, ext = self.os.path.splitext(out_file)
            new_file = base + '.mp3'
            self.os.rename(out_file, new_file)
            result = True
            return result
        except Exception as error:
            print ("ERROR: {}".format(error))
            return result


    def __del__(self):
        print("The process has finished...")
