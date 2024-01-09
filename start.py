import time
import os


from web.ui import UI

sda = None


def find_chromedriver():
    bin_dir = './bin'
    for root, dirs, files in os.walk(bin_dir):
        if 'chromedriver.exe' in files:
            return os.path.join(root, 'chromedriver.exe')
    return None

def main():
    ui = UI()
    ui.start()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass