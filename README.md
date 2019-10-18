# FTPLite
upload images(or other files) to your server &amp; replace the links in your markdown

这个脚本可以一键上传本地文件到服务器，并且能替换markdown文件中的图片的本地连接（相对路径）为对应文件的url
脚本接受三个参数，参数1是远程主机的目标路径，参数2是开始遍历文件的根目录(使用current参数或者省略则为当前脚本所在路径)，参数3是要替换的markdown文件路径（可省略）

需要在服务器上配置Apache的Alias模块和FTP账户写权限才能正常使用
