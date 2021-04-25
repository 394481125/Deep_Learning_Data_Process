# Deep_Learning_Data_Process
 深度学习中数据集下载地址及数据处理代码

## Dataset（数据集及处理代码）

### Action Recognition（视频动作识别）

先弄了目前使用的几个，[更多数据集相关请查看](https://paperswithcode.com/task/action-recognition-in-videos)

- [x] UCF101
  - [数据集论文排行榜](https://paperswithcode.com/sota/action-recognition-in-videos-on-ucf101)
  - [数据集官方下载地址](https://www.crcv.ucf.edu/data/UCF101.php)
  - 暂无

- [x] HMDB51
  - [数据集论文排行榜](https://paperswithcode.com/sota/action-recognition-in-videos-on-hmdb-51)
  - [数据集官方下载地址](https://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/)
  - 数据集处理
    - [视频分帧](.\HMDB51\data_process_HMDB_video_split.py) 
    - [训练集测试集划分](.\HMDB51\data_process_HMDB_label_write.py) 

- [x] Kinetics
  - [数据集论文排行榜](https://paperswithcode.com/dataset/kinetics)
  - [数据集官方下载地址](https://deepmind.com/research/open-source/kinetics)
  - 暂无