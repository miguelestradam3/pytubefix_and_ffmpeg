class DataClass:

    #Attributes
    data = ''
    os = __import__("os")
    pandas = __import__("pandas")
    flag = False

    #Methods
    def __init__(self):
        print("We are reading your file...")
    
    def save_file(self, data, path:str)->None:
        try:
            self.data = self.pandas.DataFrame(data)
            self.data.to_csv(path, index=False)
        except Exception as error:
            print ("ERROR: {}".format(error))

    def read_file(self, path:str)->str:
        try:
            self.data = self.pandas.read_csv(path)
        except Exception as error:
            print ("ERROR: {}".format(error))

    def __del__(self):
        print("The reading process has finished...")
