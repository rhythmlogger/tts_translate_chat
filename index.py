import os
import time
import win32com.client  # pywin32

# github.com/rhythmlogger/tts
folder_path = os.path.dirname(os.path.abspath(__file__)) + "\\log\\"
speaker = win32com.client.Dispatch('SAPI.SpVoice')


def loop_test():
    while True:
        time.sleep(2)
        # Check if the folder exists
        if os.path.exists(folder_path):
            # Get a list of files in the folder
            files = os.listdir(folder_path)
            print(f'There are {len(files)} files in the folder:')
            for file in files:
                with open(folder_path+file, 'r', encoding='utf-8') as f:
                    contents = f.read()
                    print(file)
                    print(contents)
                    speaker.Speak(contents)
                    f.close()
                    os.remove(
                        folder_path+file)
        else:
            print(f'The folder {folder_path} does not exist')


loop_test()
