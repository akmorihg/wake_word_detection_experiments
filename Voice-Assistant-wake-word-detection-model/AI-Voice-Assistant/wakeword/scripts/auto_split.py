import os


BASE_DIR = "data/environment/"

if __name__ == "__main__":
    file_names = os.listdir(BASE_DIR)
    for file_name in file_names:
        os.system(f"python split_audio_into_chunks.py --seconds 2 --audio_file_name {BASE_DIR + file_name} --save_path data/0")
        print(f"{file_name} split into chunks done!")
