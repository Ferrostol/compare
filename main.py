from zipfile import ZipFile


class Zip:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.full_list_files = []
        self.file_zip = ZipFile(self.file_name, 'r')
        self._get_list_file()

    def _get_list_file(self) -> None:
        self.arr = []
        for file in self.file_zip.namelist():
            self.full_list_files.append(file)
        
    def _get_short_name(self, long_name: str) -> str:
        if long_name.count('/') <= 1:
            return long_name
        ind = long_name.rfind('/') - 1
        ind2 = long_name[:ind].rfind('/')
        return long_name[ind2 + 1:]
    
    def get_data_in_file(self, num_file: int):
        return self.file_zip.read(self.full_list_files[num_file])
    

first_file = Zip("zip.zip")
print(first_file.full_list_files)



#second_file = Zip("OLD/ibsobj_old.zip")
#print(second_file.arr)
