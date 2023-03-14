import re

def main():
    print(parse(input("Html: ")))


def parse(s):
    if re.search(r"^<iframe.+</iframe>$", s):
        try:
            youtube_core = re.search(r"youtube\.com/embed/([^\"]+)", s)
            core = youtube_core.groups()
            return f"https://youtu.be/{core[0]}"
        except:
            return None
    else:
        return None


if __name__ == "__main__":
    main()