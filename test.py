import os
import time

FILE_PATH = "/tmp/test-python-file.txt"


def create_file():
    """创建文件"""
    with open(FILE_PATH, "w") as f:
        pass
    print(f"File created at {FILE_PATH}")


def append_to_file():
    """向文件追加内容"""
    with open(FILE_PATH, "a") as f:
        f.write("test, test\n")
    print("Content appended")


def read_file():
    """读取文件内容"""
    with open(FILE_PATH, "r") as f:
        content = f.read()
    print("File content:")
    print(content)


if __name__ == "__main__":
    create_file()
    append_to_file()
    time.sleep(5)
    read_file()
