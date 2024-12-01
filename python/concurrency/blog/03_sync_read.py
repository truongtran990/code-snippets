def sync_read_file(filepath):
    with open(filepath, "r") as file:
        return file.read()


def sync_read_all(filepaths):
    return [sync_read_file(filepath) for filepath in filepaths]


if __name__ == "__main__":
    filepaths = ["./data/file1.txt", "./data/file2.txt"]
    data = sync_read_all(filepaths)
    print(data)
