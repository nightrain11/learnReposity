#vim指定要删除的行范围
.（当前行）
$（文件中的最后一行）
%（所有行）

:10,45d- 从第 10 行删除到第 45 行
:.,$d- 从当前行删除到最后一行
:.,1d- 从当前行删除到文件开头
:dgg- 从当前行删除到文件开头
#删除第9行到第200行的内容(先用200G转到第200行) 
:9,.d 

#vim转到文件结尾
G  
#或转到第9行
9G