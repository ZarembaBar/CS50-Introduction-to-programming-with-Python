def main():
    name = input("File name: ").strip()

    ext3 = name[-3:]
    ext4 = name[-4:]

    # imges with 3 letter ext. check
    if ext3.lower() == "gif" or ext3.lower() == "jpg" or ext3.lower() == "png":
        print(f"image/{ext3.lower()}")
    # applications with 3 letters ext. check
    elif ext3.lower() == "pdf" or ext3.lower() == "zip":
        print(f"application/{ext3}")
    # text with 3 letters ext. check
    elif ext3.lower() == "txt":
        print("text/plain")
    # images with 4 letters ext. check
    elif ext4.lower() == "jpeg":
        print(f"image/{ext4}")
    else:
        print("application/octet-stream")


if __name__ == "__main__":
    main()
