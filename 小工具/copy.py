import csv
import os
import shutil


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")

        print("---  OK  ---")

    else:
        print("---  There is this folder!  ---")


def through(lujing, key_word):
    file_list = []
    count = 0
    id_list = []
    with open("疑似国内名单(1).csv", 'r', encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            id=row[0]
            id_list.append(id)
    for root, dirs, files in os.walk(lujing):
        for file in files:
            name = os.path.join(root, file)
            if key_word in name:
                for id in id_list:
                    if id in name:
                        count += 1
                        file_list.append(name)
    print(count)
    # print(file_list)
    return file_list


def copyfile(srcfile, dstpath):                       # 复制函数

    if not os.path.isfile(srcfile):
        print("%s not exist!" % srcfile)
    else:
        fpath, fname=os.path.split(srcfile)             # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)                       # 创建路径
        fname = fname.replace('_content', '')
        shutil.copy(srcfile, dstpath + '\\' + fname)          # 复制文件
        print("copy %s -> %s" % (srcfile, dstpath + '\\' + fname))


def main():
    lujing = r"D:\\Web crawler Data"
    key_word = 'content.csv'
    file_list = through(lujing, key_word)
    for value in file_list:
        value2 = value.replace("F:", 'C:')
        row_list = []
        with open(value, 'r', encoding="utf-8-sig") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                row_list.append(row)
        list = value2.split("\\")
        list.pop(-1)
        value3="\\".join(list)
        print(value3)
        # os.mkdir("D:\\数据备份\\涉藏\\第二批\\涉藏全部人根据李江林和丁洪福点赞评论人的基本信息和推文\\_denoncode\\")
        mkdir(value3)
        # os.makedirs("D:\\数据备份\\涉藏\\第二批\\涉藏全部人根据李江林和丁洪福点赞评论人的基本信息和推文")
        with open(value2, 'a+', encoding="utf-8-sig", newline='') as fw:
            csv_write = csv.writer(fw)
            data = row_list
            csv_write.writerows(data)


def main2():
    path_save = 'D:\\Test2021'
    dstpath1 = 'D:\\Web crawler Data\\MaloryCarr'
    dstpath2 = 'D:\\Web crawler Data\\MaloryCarr'
    count = 0
    for parent, dirnames, filenames in os.walk(path_save):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:  # 输出文件信息
            srcfile = os.path.join(parent, filename)
            # print(srcfile)
            # if '_content.csv' in srcfile:
            #     copyfile(srcfile, dstpath1)
            # if '_info.csv' in srcfile:
            #     copyfile(srcfile, dstpath2)
            if 'content.csv' in srcfile:
                copyfile(srcfile, dstpath1)
            count += 1
            print('count:', count)


if __name__ == '__main__':
    main2()
# copyfile(lujing, key_word)
