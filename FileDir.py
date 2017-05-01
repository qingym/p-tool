# coding:gbk
__author__ = 'Administrator'
import os
import os.path


def filename_replace(dir):
    for root, dirs, files in os.walk(dir):
        for name in files:
            filename = os.path.join(root, name)
            if -1 != name.find("网易-"):# 从网易下载总有这个标识，删除掉
                newfilename = filename.replace("网易-", "")
                os.rename(filename, newfilename)
            if -1 != name.find("&amp;"):
                newfilename = filename.replace("&amp;", "&")
                os.rename(filename, newfilename)
            if -1 != name.find("dxq") or -1 != name.find("exe"):#删除下载文件
                os.remove(filename)


def file_escape_bracket(dir):
    for root, dirs, files in os.walk(dir):
        for name in files:
            # print name
            if (name.startswith("[") & name.find("]") > 0):
                # print name[name.find("]") + 1]
                filename = os.path.join(root, name)
                newfilename = os.path.join(root, name[name.find("]") + 1:])
                # print filename
                # print newfilename
                # exit()
                os.rename(filename, newfilename)
            if (name.startswith("【") & name.find("】") > 0):
                # print name[name.find("]") + 1]
                filename = os.path.join(root, name)
                newfilename = os.path.join(root, name[name.find("】") + 1:])
                # print filename
                # print newfilename
                # exit()
                os.rename(filename, newfilename)

# 【BT首发】


if __name__ == '__main__':
    # os.rename("F:\open\TP.201.耶鲁大学公开课：政治哲学导论\\0001.网易-导论：何谓政治哲学？.flv".decode("utf8").encode("gbk"),"F:\open\TP.201.耶鲁大学公开课：政治哲学导论\\0001.导论：何谓政治哲学？.flv".decode("utf8").encode("gbk"));
    # filename_replace("F:\open\B82.201.哈佛大学公开课：公正-该如何做是好？")
    file_escape_bracket("F:\movie")
    # filename_replace("D:\open\psychology")
    # filename_replace("F:\open")
    # filename_replace("E:\OS X Yosemite")
