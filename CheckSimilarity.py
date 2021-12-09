import glob
from math import *
from glob import *
import os
import pprint

def jaccard_similarity(source, target):
    array1 = set(source.split())
    array2 = set(target.split())

    intersection = array1.intersection(array2)

    result = float(len(intersection)/len(array1))

    return round(result, 3) * 100

def scan(source_path, target_path):
    source_path += "/**/*.java"
    target_path += "/**/*.java"
    sp = glob(source_path, recursive=True)

    result = {};
    print("Source 파일의 총 갯수는 : {}개".format(sp.__len__()))
    print("처리중......")
    for source in sp:
        source_file = os.path.join(source_path, source)
        result[source_file.replace("\\", "/")] = scan_target(source_file, target_path)

    result = sorted(result.items(), key=(lambda x:x[1][1]), reverse=True)
    pprint.pprint(result)


def scan_target(source_file, target_path):
    tp = glob(target_path, recursive=True)

    target_dic = {};
    for target in tp:
        target_file = os.path.join(target_path, target)
        source_content = read_text_file(source_file)
        target_content = read_text_file(target_file)
        similarity = jaccard_similarity(source_content, target_content)
        target_dic[target_file.replace("\\", "/")] = similarity

    target_dic = sorted(target_dic.items(), key=(lambda x:x[1]), reverse=True)
    return target_dic[0];


def read_text_file(filePath):
    with open(filePath, 'r', encoding='utf8') as f:
        content = f.read()
    return content

# source = 'I am a boy'
# target = 'I am aaa girl'

# print('유사도 : {} %'.format(jaccard_similarity(source, target) * 100))

# scan("C:/Users/rupin/PycharmProjects/pythonProject", "C:/Users/rupin/test")
# scan("C:/spring/workspace/7.0.0/nexcore.framework.core", "C:/spring/workspace/7.0.0/nexcore.framework.core")
scan("E:/rupinus/훈기문서/IdeaProjects/smell", "C:/spring/workspace/7.0.0/nexcore.framework.core")
