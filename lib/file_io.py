def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode="w", encoding="utf-8") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode="a", encoding="utf-8") as appendFile:
        appendFile.write(append_content)

def read_file(file_name):
    fileRead = open(f"{file_name}.txt", encoding="utf-8")
    return fileRead.read()

file_name = "test_file"
file_content = "This is a test content."
write_file(file_name, file_content)
file_content_read = read_file(file_name)
print(file_content_read)