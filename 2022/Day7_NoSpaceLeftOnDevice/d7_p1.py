class MaxDirectorySize():
    def __init__(self):
        self.input_file = open('input.txt', 'r').readlines()
        self.directory_dict = {}
        self.current_path = []
        self.last_call_dir = False
        self.size_dict = {}
        
    def main(self):
        # Convert input to dictionary
        for i, line in enumerate(self.input_file):
            line = line.strip('\n')
            str_list = line.split()
            self.check_list(str_list)
        
        # Find directory sizes
        self.get_dir_size(self.directory_dict, '')
        total = 0
        for k in self.size_dict:
            total += self.size_dict.get(k)
        print(total)

    def get_dir_size(self, dir_dict, path):
        keys = dir_dict.keys()
        size = 0
        for k in keys:
            if dir_dict.get(k) is not None:
                if dir_dict.get(k).get('filesize') is None:
                    size += self.get_dir_size(dir_dict.get(k), path+' '+k)
                else:
                    size += int(dir_dict.get(k).get('filesize'))
        if dir_dict.get('filesize') is None and size <= 100000:
            self.size_dict[path] = size
        return size
                    

    def check_list(self, str_list):
        if str_list[0] == '$':
            self.check_list(str_list[1:])
        
        elif str_list[0] == 'cd':
            if str_list[1] == '..':
                self.current_path.pop()
            elif str_list[1] == '/':
                self.current_path = ['/']
            else:
                self.current_path.append(str_list[1])

        elif str_list[0] in ['ls', 'dir']:
            pass
        else:
            temp_dict = self.create_dict_entry(self.current_path, str_list)
            self.directory_dict = self.merge_dict(self.directory_dict, temp_dict)
        
    def create_dict_entry(self, current_path, str_list):
        temp_dict = {}
        if len(current_path) > 1:
            temp_dict = { current_path[0]: self.create_dict_entry(current_path[1:], str_list) }
        else:
            temp_dict = { current_path[0]: { str_list[1]: { 'filesize': int(str_list[0]) } } }
        return temp_dict
    
    def merge_dict(self, dir_dict, temp_dict):
        keys = dir_dict.keys() | temp_dict.keys()
        loop_dict = {}
        for k in keys:
            if dir_dict.get(k) is not None and temp_dict.get(k) is not None:
                if dir_dict.get(k).get('filesize') is None and temp_dict.get(k).get('filesize') is None:
                    loop_dict = loop_dict | { k: self.merge_dict(dir_dict.get(k), temp_dict.get(k)) }
                elif temp_dict.get(k).get('filesize') is not None:
                    loop_dict = loop_dict | { k: temp_dict.get(k) }
                elif dir_dict.get(k).get('filesize') is not None:
                    loop_dict = loop_dict | { k: dir_dict.get(k) }
            elif dir_dict.get(k) is None and temp_dict.get(k) is not None:
                loop_dict = loop_dict | { k: temp_dict.get(k) }
            elif dir_dict.get(k) is not None and temp_dict.get(k) is None:
                loop_dict = loop_dict | { k: dir_dict.get(k) }
        return loop_dict
        
if __name__ == '__main__':
    MaxDirectorySize().main()