
# -*- coding: UTF-8 -*-

# setup.py 自动从当前目录查找代码块文件，并部署到Xcode指定目录中。执行完成后，重启Xcode即可

# 访问Mac os 系统文件路径
import os
# 用于删除非空文件夹
import shutil
# 获取文件夹权限
import stat
# 获取当前时间
import datetime


def detect_walk(dir_path,suffix):

    for root, dirs, files in os.walk(dir_path):
        
        for filename in files:        
            # os.path.splitext():分离文件名与扩展名
            if os.path.splitext(filename)[1] == suffix:
                if root == dir_path:
                    newFileName = filename
                else:
                    temp = root.replace(dir_path+'/','')
                    temp = temp.replace('/','-')
                    newFileName = temp + '-' + filename

                filePath = os.path.join(root,filename)
                targetPath = os.path.join(dst,newFileName)
                # 创建软链接
                os.symlink(filePath, targetPath)

def copyBackupFileIfNeed(_dst,_backup) :
    if os.path.exists(_dst) == False:
        os.mkdir(_dst)
    else: 
        
        if os.path.exists(_backup):
            shutil.rmtree(_backup)
        # 将原有代码段文件夹变更为备份
        os.rename(_dst,_backup)
        print('\n已备份至%s\n' %_backup)
        os.mkdir(_dst)


BASE_HOME = os.environ['HOME']
UserData = BASE_HOME + '/Library/Developer/Xcode/UserData'
dst = BASE_HOME + '/Library/Developer/Xcode/UserData/CodeSnippets'
backup = UserData + "/CodeSnippets." + datetime.datetime.now().strftime('%Y%m%d%H%M%S')

# 生成发布的文件集
# 1 检查系统目录，如果之前存在代码块文件则做个备份
# 2 遍历当前路径
# 2.1 查找根目录下所有后缀名为.codesnippets 的文件
# 2.2 锁定路径
# 2.3 软链接到系统目录
if __name__ == "__main__":
    # 检查Xcode/UserData目录是否存在，不存在，则提示用户检查
    if os.path.exists(UserData) == False:
       print '不存在目录 %s。执行结束\n' %UserData
       exit()

    copyBackupFileIfNeed(dst,backup)
    # if os.path.exists(dst) == False:
    #     os.mkdir(dst)
    # else: 
    #     # 将原有代码段文件夹变更为备份
    #     if os.path.exists(backup):
    #         shutil.rmtree(backup)
    #     os.rename(dst,backup)
    #     os.mkdir(dst)

    # 锁定当前python文件的目录
    localPath = os.path.dirname(os.path.realpath(__file__))
    detect_walk(localPath,".codesnippet")

    print '执行完成\n'
