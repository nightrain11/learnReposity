import re
from bs4 import BeautifulSoup
from lxml import etree
 
# soup = BeautifulSoup("<p><\/p><a class=\"video-box\" href=\"https://link.zhihu.com/?target=https%3A//www.zhihu.com/video/1505130749309648896\" target=\"_blank\" data-video-id=\"\" data-video-playable=\"\" data-name=\"这是他的样子\" data-poster=\"https://pic3.zhimg.com/v2-cf0902d6952693938fb2692fa249ac65.jpg\" data-lens-id=\"1505130749309648896\"><img class=\"thumbnail\" src=\"https://pic3.zhimg.com/v2-cf0902d6952693938fb2692fa249ac65.jpg\"/><span class=\"content\"><span class=\"title\">这是他的样子<span class=\"z-ico-extern-gray\"><\/span><span class=\"z-ico-extern-blue\"><\/span><\/span><span class=\"url\"><span class=\"z-ico-video\"><\/span>https://www.zhihu.com/video/1505130749309648896<\/span><\/span><\/a><p><\/p><a class=\"video-box\" href=\"https://link.zhihu.com/?target=https%3A//www.zhihu.com/video/1505130788835934208\" target=\"_blank\" data-video-id=\"\" data-video-playable=\"\" data-name=\"\" data-poster=\"https://pic3.zhimg.com/v2-dda12b0915e4371e3c0531669d32501f.jpg\" data-lens-id=\"1505130788835934208\"><img class=\"thumbnail\" src=\"https://pic3.zhimg.com/v2-dda12b0915e4371e3c0531669d32501f.jpg\"/><span class=\"content\"><span class=\"title\"><span class=\"z-ico-extern-gray\"><\/span><span class=\"z-ico-extern-blue\"><\/span><\/span><span class=\"url\"><span class=\"z-ico-video\"><\/span>https://www.zhihu.com/video/1505130788835934208<\/span><\/span><\/a><p><\/p>")
# # soup = BeautifulSoup("<p><\/p><a class=\"video-box\" href=\"https://link.zhihu.com/?target=https%3A//www.zhihu.com/video/1505130749309648896\" target=\"_blank\" data-video-id=\"\" data-video-playable=\"\" data-name=\"这是他的样子\" data-poster=\"https://pic3.zhimg.com/v2-cf0902d6952693938fb2692fa249ac65.jpg\" data-lens-id=\"1505130749309648896\"><img class=\"thumbnail\" src=\"https://pic3.zhimg.com/v2-cf0902d6952693938fb2692fa249ac65.jpg\"/><span class=\"content\"><span class=\"title\">这是他的样子<span class=\"z-ico-extern-gray\"><\/span><span class=\"z-ico-extern-blue\"><\/span><\/span><span class=\"url\"><span class=\"z-ico-video\"><\/span>https://www.zhihu.com/video/1505130749309648896<\/span><\/span><\/a><p><\/p><a class=\"video-box\" href=\"https://link.zhihu.com/?target=https%3A//www.zhihu.com/video/1505130788835934208\" target=\"_blank\" data-video-id=\"\" data-video-playable=\"\" data-name=\"\" data-poster=\"https://pic3.zhimg.com/v2-dda12b0915e4371e3c0531669d32501f.jpg\" data-lens-id=\"1505130788835934208\"><img class=\"thumbnail\" src=\"https://pic3.zhimg.com/v2-dda12b0915e4371e3c0531669d32501f.jpg\"/><span class=\"content\"><span class=\"title\"><span class=\"z-ico-extern-gray\"><\/span><span class=\"z-ico-extern-blue\"><\/span><\/span><span class=\"url\"><span class=\"z-ico-video\"><\/span>https://www.zhihu.com/video/1505130788835934208<\/span><\/span><\/a><p><\/p>")
# anchors1 = soup.find_all('p')
# anchors2 = soup.find_all('br')
# anchors3 = soup.find_all('div')
# for i, item in enumerate(anchors1):
#     if i == len(anchors1) - 1:
#         continue
#     item.append('&&')
#     print (item)
ss ="样子https://www.zhihu.com/video/1505130749309648896\n太可爱了\nhttps://www.zhihu.com/video/1505130788835934208sssssssssss\n太可爱了吧"
result = re.sub(r'http\S+', '', ss)
# replace the url pattern
print(result)
# for item in enumerate(anchors2):
#     if i != len(anchors2) - 1:
#         continue
#     item.append('\n')
#     print (item)

# for item in enumerate(anchors3):
#     if i != len(anchors3) - 1:
#         item.append('\n')
#     print (item)
# pattern = re.compile(r'<[^>]+>',re.S)
# result = pattern.sub('', soup.get_text().strip())
# result.replace("&&", "/n")
# print(result)
# # 方法一

# for string in soup.stripped_strings:
#     print(repr(string))
# print(soup.stripped_strings)


# coding:utf-8
# from bs4 import BeautifulSoup
 
# soup = BeautifulSoup("<p><\/p><a class=\"video-box\" href=\"https://link.zhihu.com/?target=https%3A//www.zhihu.com/video/1505130749309648896\" target=\"_blank\" data-video-id=\"\" data-video-playable=\"\" data-name=\"这是他的样子\" data-poster=\"https://pic3.zhimg.com/v2-cf0902d6952693938fb2692fa249ac65.jpg\" data-lens-id=\"1505130749309648896\"><img class=\"thumbnail\" src=\"https://pic3.zhimg.com/v2-cf0902d6952693938fb2692fa249ac65.jpg\"/><span class=\"content\"><span class=\"title\">这是他的样子<span class=\"z-ico-extern-gray\"><\/span><span class=\"z-ico-extern-blue\"><\/span><\/span><span class=\"url\"><span class=\"z-ico-video\"><\/span>https://www.zhihu.com/video/1505130749309648896<\/span><\/span><\/a><p><\/p><a class=\"video-box\" href=\"https://link.zhihu.com/?target=https%3A//www.zhihu.com/video/1505130788835934208\" target=\"_blank\" data-video-id=\"\" data-video-playable=\"\" data-name=\"\" data-poster=\"https://pic3.zhimg.com/v2-dda12b0915e4371e3c0531669d32501f.jpg\" data-lens-id=\"1505130788835934208\"><img class=\"thumbnail\" src=\"https://pic3.zhimg.com/v2-dda12b0915e4371e3c0531669d32501f.jpg\"/><span class=\"content\"><span class=\"title\"><span class=\"z-ico-extern-gray\"><\/span><span class=\"z-ico-extern-blue\"><\/span><\/span><span class=\"url\"><span class=\"z-ico-video\"><\/span>https://www.zhihu.com/video/1505130788835934208<\/span><\/span><\/a><p><\/p>")
# # info = [s.extract() for s in soup('div')]
# for doc in soup.find_all('div'):
#     doc.decompose()
# print(soup)
# print(soup.text)