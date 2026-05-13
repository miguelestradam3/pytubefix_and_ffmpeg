from modules.youtube import YoutubeClass
from modules.readers import DataClass

PATH = "Musica"

if __name__ == "__main__":
    # Create instances of the classes
    data_buff = DataClass()
    buff = YoutubeClass()

    data_buff.read_file(path="data/output.csv")

    for link in data_buff.data['Link']:
        buff.download_video(url=link)

    #Saving space
    del buff
    del data_buff