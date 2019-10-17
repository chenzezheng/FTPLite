import GetFile as GF
import Replace as RP
from settings import ftp_param
from ftplib import FTP
from ftplib import error_perm
import sys
import os

ftp_param['points_dir'] = sys.argv[1]               #目的路径
local_root = os.getcwd()                            #上传的文件默认从当前路径开始遍历
if len(sys.argv) >= 3 :
    if sys.argv[2] != 'current' :                   #若参数为'current'，则以脚本当前所在路径作为目录开始遍历
        local_root = sys.argv[2]                    #若有给定参数，则以该参数作为路径开始遍历

print(local_root)
Files = GF.GetFilePath(local_root)                  #遍历目录下的所有常见图片类型文件

#默认21端口
ftp = FTP(ftp_param['host'])                        #连接到远程主机

#指定端口
#ftp.connect(ftp_param['host'], ftp_param['port'])

ftp.login(ftp_param['user'], ftp_param['pwd'])      #登录
try:
    ftp.cwd(ftp_param['points_dir'])                #尝试转到目的路径
except error_perm:
    ftp.mkd(ftp_param['points_dir'])                #若目的路径不存在，则创建该目录
    ftp.cwd(ftp_param['points_dir'])                #然后转到

for i in range(0, len(Files.names)) :
    print(f'Uploading {Files.names[i]} ...')
    ftp.storbinary('STOR %s' % Files.names[i], open(Files.paths[i], 'rb'), ftp_param['buf'])    #上传文件
ftp.quit()                                          #关闭并退出连接

print('Upload Successfully!')

if len(sys.argv) >= 4 :
    print('Replacing...')
    RP.ReplaceMD(sys.argv[3], ftp_param['alias'] + ftp_param['points_dir'] + '/')
    print('Replace Successfully!')