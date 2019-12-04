import os
import cv2

def mosaic(img, rect, mosaic_rate=15):
    x, y, xmax, ymax = rect
    # if x < 0:
    #     xmax = xmax - x
    #     x = 0
    # if y < 0:
    #     ymax = ymax - x
    #     y = 0
    if x < 0 or y < 0 or xmax < 0 or ymax < 0:
        return img

    w = xmax-x
    h = ymax-y
    face_img = img[y:ymax, x:xmax]
    min_side = min(w, h)

    if min_side <= mosaic_rate:
        mosaic_rate = min_side // 2

    face_img = cv2.resize(face_img, (w // mosaic_rate, h // mosaic_rate))
    face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)
    try:
        img[y:ymax, x:xmax] = face_img
    except Exception as e:
        print('w', w, 'h', h, 'rect', rect, 'mosaic_rate', mosaic_rate)
        print(e)

    return img

def video2img(vdo_path, img_dir, fps, tot_seconds):
    cmd = 'ffmpeg -t '+str(tot_seconds)+' -i "'+vdo_path+'" -r '+str(fps)+' -qscale:v 2 -f image2 '+img_dir+'/img_%d.jpg'
    os.system(cmd)

import pytube
def download_youtube(url, sav_path):
    yt = pytube.YouTube(url)
    vids = yt.streams.all()

    for i in range(len(vids)):
        print(i, '. ', vids[i])

    vnum = int(input('Select video number to download : '))
    vids[vnum].download(sav_path)

if __name__ == '__main__':
    download_youtube('YOUTUBE_URL', 'SAVE_DIR')
