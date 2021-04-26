# Deep_Learning_Data_Process
 深度学习中数据集下载地址及数据处理代码

## Dataset（数据集及处理代码）

### Action Recognition（视频动作识别）

先弄了目前使用的几个，[更多数据集相关请查看](https://paperswithcode.com/task/action-recognition-in-videos)

通用的视频帧数据读取操作

- [x] UCF101
  - [数据集论文排行榜](https://paperswithcode.com/sota/action-recognition-in-videos-on-ucf101)
  - [数据集官方下载地址](https://www.crcv.ucf.edu/data/UCF101.php)
  - 数据集处理
    - [视频分帧](https://github.com/394481125/Deep_Learning_Data_Process/blob/main/UCF101/data_process_UCF101_video_split.py) 
    - [训练集测试集划分](https://github.com/394481125/Deep_Learning_Data_Process/blob/main/UCF101/data_process_UCF101_label_write.py) 
  
- [x] HMDB51
  - [数据集论文排行榜](https://paperswithcode.com/sota/action-recognition-in-videos-on-hmdb-51)
  - [数据集官方下载地址](https://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/)
  - 数据集处理
    - [视频分帧](https://github.com/394481125/Deep_Learning_Data_Process/blob/main/HMDB51/data_process_HMDB_video_split.py) 
    - [训练集测试集划分](https://github.com/394481125/Deep_Learning_Data_Process/blob/main/HMDB51/data_process_HMDB_label_write.py) 

- [x] Kinetics
  - [数据集论文排行榜](https://paperswithcode.com/dataset/kinetics)
  - [数据集官方下载地址](https://deepmind.com/research/open-source/kinetics)
  - 暂无

参考：

- [x] [常用公开数据集（英文）](https://homepages.inf.ed.ac.uk/rbf/CVonline/Imagedbase.htm)
- [x] [常用公开数据集（中文）](https://blog.csdn.net/weixin_41036461/article/details/80667690?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-3.control&dist_request_id=1332048.364.16193541378181833&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-3.control)
- [x] [10个高质量计算机视觉项目数据集](https://www.pianshen.com/article/41431310864/)