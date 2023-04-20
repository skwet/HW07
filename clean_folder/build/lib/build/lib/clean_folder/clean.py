import os
import sys
import shutil


image_ext = ('.jpeg','.jpg','.png')
video_ext = ('.avi','.mp4','.mov')
audio_ext = ('.mp3','.wav')
doc_ext = ('.docx','.doc','.txt','.pdf','.pptx','.xlsx')
archive_ext = ('.zip','.gz','.tar')

path = sys.argv[1]

def normalize(path):
        translit_dict = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ie',
            'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k', 'л': 'l',
            'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
            'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ь': '', 'ю': 'iu',
            'я': 'ia'
        }
        for file in os.listdir(path):
            old_path = os.path.join(path, file)
            name, ext = os.path.splitext(file)
            new_name = ''
        
            for c in name:
                if c.isascii():
                    new_name += c
                elif c.lower() in translit_dict:
                    if c.isupper():
                        new_name += translit_dict[c.lower()].upper()
                    else:
                        new_name += translit_dict[c.lower()]
                else:
                    new_name += '_'
                
            new_name += ext
            new_path = os.path.join(path, new_name)
        
            os.rename(old_path, new_path)

def image_sort(path):
    image_path = os.path.join(path, "images")
    os.makedirs(image_path)
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith(image_ext):
            shutil.move(file_path, os.path.join(image_path, file_name))

def video_sort(path):
    video_folder_path = os.path.join(path, "video")
    os.makedirs(video_folder_path)
    
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith(video_ext):
            shutil.move(file_path, os.path.join(video_folder_path, file_name))

def audio_sort(path):
    audio_path = os.path.join(path, "audio")
    os.makedirs(audio_path)
    
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith(audio_ext):
            shutil.move(file_path, os.path.join(audio_path, file_name))

def doc_sort(path):
    doc_path = os.path.join(path, "documents")
    os.makedirs(doc_path)
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith(doc_ext):
            shutil.move(file_path, os.path.join(doc_path, file_name))


def archive_sort(path):
    archives_folder = os.path.join(path, "archives")
    if not os.path.exists(archives_folder):
        os.makedirs(archives_folder)
        
    for file_name in os.listdir(path):
        if file_name.endswith(archive_ext):
            file_path = os.path.join(path, file_name)
            folder_name = os.path.splitext(file_name)[0]
            destination_path = os.path.join(archives_folder, folder_name)
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            shutil.unpack_archive(file_path, destination_path)

def file_sorter(path):
    normalize(path)
    image_sort(path)
    video_sort(path)
    audio_sort(path)
    doc_sort(path)
    archive_sort(path)
    

if __name__ == '__main__':
    file_sorter(path)    
    