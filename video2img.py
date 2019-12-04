# ffmpeg video -> image
import video_util
import os

def convert(nm, base_dir='BASE_SAV_DIR/', tm=150):
    dir1 = base_dir+nm
    if not os.path.exists(dir1):
        os.makedirs(dir1)
    video_util.video2img(base_dir+nm+'.mp4', dir1, 2, tm)

if __name__ == '__main__':
    convert('mp4_file_name')
