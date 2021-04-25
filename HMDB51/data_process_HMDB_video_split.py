import argparse
import os
import subprocess

# 获得视频分帧的参数
def get_args():
    parser = argparse.ArgumentParser('HMDB_Video_split_Process')
    parser.add_argument('--data_path',default='E:\\HMDB',type=str)
    parser.add_argument('--isdelate',default=False,type=bool)

    return parser.parse_args()

# 使用ffmpeg将视频切分为图像帧jpg
def video_to_images_jpg(vid_file, img_folder, return_info=False):

    command = ['ffmpeg',
               '-i', vid_file,
               '-f', 'image2',
               '-v', 'error',
               f'{img_folder}/%d.jpg']
    print(f'Running \"{" ".join(command)}\"')
    subprocess.call(command)
    print(f'Images saved to \"{img_folder}\"')

# 根据文件夹将图像切分
def video_dir_split_imges_jpg(data_path,isdelate=False):

    dir_path_list = []

    video_path_list = []

    for one_dir in os.listdir(data_path):
        one_dir_path = os.path.join(data_path, one_dir)
        one_dir_files = os.listdir(one_dir_path)
        for video_file in one_dir_files:
            video_and_dir_path = os.path.join(one_dir_path,video_file)
            if(os.path.isfile(video_and_dir_path)):
                if len(video_file.split('.'))>1 and video_file.split('.')[1]=='avi':
                    sub_video_file_path = video_and_dir_path
                    sub_video_dir_path = os.path.join(one_dir_path, video_file.split('.')[0])
                    if not os.path.exists(sub_video_dir_path):
                        os.makedirs(sub_video_dir_path,mode=0o755)
                    dir_path_list.append(sub_video_dir_path)
                    video_path_list.append(sub_video_file_path)
                    print(sub_video_file_path,'文件夹创建完毕')


    for index in range(len(dir_path_list)):
        video_to_images_jpg(video_path_list[index],dir_path_list[index])
        print(video_path_list[index], '视频分割完毕')
        if (isdelate):
            os.remove(video_path_list[index])
            print(video_path_list[index], '视频已经移除')


# 根据参数将视频分帧
if __name__ == '__main__':
    args = get_args()
    video_dir_split_imges_jpg(args.data_path,args.isdelate)
