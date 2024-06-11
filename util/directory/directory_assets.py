class DirectoryAssets :

    def __init__(self) -> None:
        self.dir = "./.config/check_list.txt"

    def return_content_from_file(self, file_name):
        with open(file_name, "r") as file:
            return file.read()
    
    def write_to_file(self, file_name, content):
        with open(file_name, "w") as file:
            file.write(content)

if __name__ == '__main__' :
    directory_assets = DirectoryAssets()
    content = directory_assets.return_content_from_file(directory_assets.dir)
    print(content)