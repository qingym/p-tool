# coding:gbk
__author__ = 'Administrator'
import os
import os.path


def filename_replace(dir):
    for root, dirs, files in os.walk(dir):
        for name in files:
            filename = os.path.join(root, name)
            if -1 != name.find("����-"):# �������������������ʶ��ɾ����
                newfilename = filename.replace("����-", "")
                os.rename(filename, newfilename)
            if -1 != name.find("&amp;"):
                newfilename = filename.replace("&amp;", "&")
                os.rename(filename, newfilename)
            if -1 != name.find("dxq") or -1 != name.find("exe"):#ɾ�������ļ�
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
            if (name.startswith("��") & name.find("��") > 0):
                # print name[name.find("]") + 1]
                filename = os.path.join(root, name)
                newfilename = os.path.join(root, name[name.find("��") + 1:])
                # print filename
                # print newfilename
                # exit()
                os.rename(filename, newfilename)

# ��BT�׷���


if __name__ == '__main__':
    # os.rename("F:\open\TP.201.Ү³��ѧ�����Σ�������ѧ����\\0001.����-���ۣ���ν������ѧ��.flv".decode("utf8").encode("gbk"),"F:\open\TP.201.Ү³��ѧ�����Σ�������ѧ����\\0001.���ۣ���ν������ѧ��.flv".decode("utf8").encode("gbk"));
    # filename_replace("F:\open\B82.201.�����ѧ�����Σ�����-��������Ǻã�")
    file_escape_bracket("F:\movie")
    # filename_replace("D:\open\psychology")
    # filename_replace("F:\open")
    # filename_replace("E:\OS X Yosemite")
