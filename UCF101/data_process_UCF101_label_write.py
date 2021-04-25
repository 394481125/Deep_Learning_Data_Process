import argparse
import os

# 获得视频打标签的参数
def get_args():
    parser = argparse.ArgumentParser('UCF101_Video_label_Process')
    parser.add_argument('--data_path',default='E:\\attention-network-master\\UCF-101',type=str)

    return parser.parse_args()

# 统计label字典

def count_label_dic(data_path):
    label_index = 0
    label_dic = {}
    for label_dir in os.listdir(data_path):
        label_dic[label_dir] = label_index
        label_index = label_index +1
    return label_dic

def count_sum_number_dic(data_path,label_dic):
    sum_number_dic = {}

    for label_dir in os.listdir(data_path):
        label = label_dic[label_dir]
        label_dir_path = os.path.join(data_path,label_dir)
        for file_dir in os.listdir(label_dir_path):
            file_dir_path = os.path.join(label_dir_path,file_dir)
            if os.path.isdir(file_dir_path):
                sum_number = num_sum(file_dir_path)
                sum_number_dic[file_dir] = sum_number
    return sum_number_dic

def count_filedir2file_dic(data_path):
    filedir2file_dic = {}
    for filedir in os.listdir(data_path):
        filedir_path = os.path.join(data_path,filedir)
        for file in os.listdir(filedir_path):
            filedir2file_dic[file] = filedir

    return filedir2file_dic

def num_sum(path_dir):
        sum = 0
        ls = os.listdir(path_dir)
        for i in ls:
            if os.path.isfile(os.path.join(path_dir, i)):
                sum += 1
        return str(sum)

def get_train_test_val_text(data_path,train_txt = 'ucf101_split1_train.txt',test_txt = 'ucf101_split1_test.txt'):
    # 视频文件夹->类文件夹
    filedir2file_dic =count_filedir2file_dic(data_path)
    # 文件夹->label编号
    label_dic = count_label_dic(data_path)
    # 视频文件夹->帧数
    sum_number_dic = count_sum_number_dic(data_path,label_dic)

    for class_dir in os.listdir(data_path):
        class_dir_path = os.listdir(os.path.join(data_path,class_dir))
        class_dir_count_sum = len(class_dir_path)
        index = 0
        for file in class_dir_path:

            file_path = os.path.join(data_path,class_dir,file)
            if os.path.isdir(file_path):

                real_file_path = file_path.replace(data_path, 'UCF-101')
                real_file_sum = sum_number_dic[file]
                real_file_label = label_dic[filedir2file_dic[file]]
                path_string = real_file_path + ' ' + str(real_file_sum) + ' ' + str(real_file_label)

                if(index<class_dir_count_sum*0.7):
                    with open(train_txt, 'a', encoding='utf-8') as file:
                        file.writelines(path_string.replace('\\','/'))
                        file.writelines('\n')

                else:
                    with open(test_txt, 'a', encoding='utf-8') as file:
                        file.writelines(path_string.replace('\\','/'))
                        file.writelines('\n')

                index = index + 1

if __name__ == '__main__':

    args = get_args()
    get_train_test_val_text(args.data_path)









