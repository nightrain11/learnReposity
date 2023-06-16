# use this tool to format crawl data like follow
## run  in shell
``` shell
- python3 ./zhihu_process.py ./zhihu_data/
```
- ## origin data before use this tools
``` json
2023 - 06 - 08 15: 50: 07, 069 - zhihu question: {
	"url": "https://www.zhihu.com/question/531279423",
	"answerCount": 12,
	"realAnswerCount": 12,
	"visitCount": 786,
	"followerCount": 14,
	"answers": [{
		"content": "<p data-pid=\"uu9p6vfB\">可以先送去附近宠物医院做个体检，一般正常费用在一百多点。<\/p><p data-pid=\"RDqvmitt\">并且做好驱虫。<\/p><p data-pid=\"5dllsPsC\">年龄过小还是需要购买羊奶粉搭配猫粮喂养。<\/p>",
		"realContentLength": 57,
		"url": "https://www.zhihu.com/question/531279423/answer/-1825491901",
		"voteCount": "<p data-pid=\"uu9p6vfB\">可以先送去附近宠物医院做个体检，一般正常费用在一百多点。<\/p><p data-pid=\"RDqvmitt\">并且做好驱虫。<\/p><p data-pid=\"5dllsPsC\">年龄过小还是需要购买羊奶粉搭配猫粮喂养。<\/p>"
	}, {
		"content": "<p data-pid=\"-4VdRlUn\">这个小猫看起来能吃动幼猫粮了。我家二猫捡回来比这小，还不会从碗里喝奶，就买了羊奶粉和小奶瓶，喂了一个星期，它开始咬奶嘴，把好几个奶嘴咬烂用不成了，只好倒碗里让它自己喝，虽然也会呛着，但是慢慢它会喝了就好了。喝了没几天它开始不喝奶抢着大猫的猫粮吃，就开始改喂幼猫粮了，大半罐羊奶粉最后浪费了。<\/p><p data-pid=\"_pd59w-6\">所以如果它能吃动幼猫粮就给它喂幼猫粮吃也行。只是别给它喂猫罐头，我家二猫偷吃大猫罐头，就大拇指那么大一坨就拉稀拉了一个星期，我差点以为它要死了。肉也先少喂点，没有异常再加量。<\/p>",
		"realContentLength": 233,
		"url": "https://www.zhihu.com/question/531279423/answer/-1825385771",
		"voteCount": "<p data-pid=\"-4VdRlUn\">这个小猫看起来能吃动幼猫粮了。我家二猫捡回来比这小，还不会从碗里喝奶，就买了羊奶粉和小奶瓶，喂了一个星期，它开始咬奶嘴，把好几个奶嘴咬烂用不成了，只好倒碗里让它自己喝，虽然也会呛着，但是慢慢它会喝了就好了。喝了没几天它开始不喝奶抢着大猫的猫粮吃，就开始改喂幼猫粮了，大半罐羊奶粉最后浪费了。<\/p><p data-pid=\"_pd59w-6\">所以如果它能吃动幼猫粮就给它喂幼猫粮吃也行。只是别给它喂猫罐头，我家二猫偷吃大猫罐头，就大拇指那么大一坨就拉稀拉了一个星期，我差点以为它要死了。肉也先少喂点，没有异常再加量。<\/p>"
	}, {
		"content": "<p data-pid=\"cctFsN5f\">主食罐头可以，猫粮可以试着喂，不过猫粮和主食罐头不能一起喂，否则会拉稀的。<\/p><p data-pid=\"a6oEZC8r\">脱乳糖的牛奶可以。羊奶我没试过，不乱说。<\/p>",
		"realContentLength": 58,
		"url": "https://www.zhihu.com/question/531279423/answer/-1825285099",
		"voteCount": "<p data-pid=\"cctFsN5f\">主食罐头可以，猫粮可以试着喂，不过猫粮和主食罐头不能一起喂，否则会拉稀的。<\/p><p data-pid=\"a6oEZC8r\">脱乳糖的牛奶可以。羊奶我没试过，不乱说。<\/p>"
	}, {
		"content": "<p data-pid=\"iImdgg5z\">这看起来一个半月左右，基本的生活自理技能已经学会了<\/p><ul><li data-pid=\"53qQSlrQ\">主要就是喂食，现在这个阶段建议喂食奶糕粮+羊奶粉，等再过半个月左右就可以只喂食干粮<\/li><\/ul><p data-pid=\"6OfojSm7\">可以适当的煮点鸡胸肉但是注意不要吃多引起挑食<\/p><ul><li data-pid=\"Ijd6N5nP\">保温<\/li><\/ul><p data-pid=\"QJy7ekAm\">这个年纪的猫咪很容易生病，要做好保温，最好温度在27摄氏度以上，这样不容易生病<\/p><ul><li data-pid=\"nuZd5mHs\">驱虫<\/li><\/ul><p data-pid=\"fa4KK_lY\">流浪的小猫咪身上或多或少都会有寄生虫，可以用大宠爱<\/p><ul><li data-pid=\"-eFluV41\">打疫苗<\/li><\/ul><p data-pid=\"4Q4DUr9Y\">驱虫后最少3天，接回家饲养一周以上没有问题，精神食欲大小便正常就可以去打疫苗了<\/p><p data-pid=\"xeuW3Lmx\">打完疫苗之后小猫咪才不会感染猫瘟这些病毒<\/p>",
		"realContentLength": 227,
		"url": "https://www.zhihu.com/question/531279423/answer/-1824063295",
		"voteCount": "<p data-pid=\"iImdgg5z\">这看起来一个半月左右，基本的生活自理技能已经学会了<\/p><ul><li data-pid=\"53qQSlrQ\">主要就是喂食，现在这个阶段建议喂食奶糕粮+羊奶粉，等再过半个月左右就可以只喂食干粮<\/li><\/ul><p data-pid=\"6OfojSm7\">可以适当的煮点鸡胸肉但是注意不要吃多引起挑食<\/p><ul><li data-pid=\"Ijd6N5nP\">保温<\/li><\/ul><p data-pid=\"QJy7ekAm\">这个年纪的猫咪很容易生病，要做好保温，最好温度在27摄氏度以上，这样不容易生病<\/p><ul><li data-pid=\"nuZd5mHs\">驱虫<\/li><\/ul><p data-pid=\"fa4KK_lY\">流浪的小猫咪身上或多或少都会有寄生虫，可以用大宠爱<\/p><ul><li data-pid=\"-eFluV41\">打疫苗<\/li><\/ul><p data-pid=\"4Q4DUr9Y\">驱虫后最少3天，接回家饲养一周以上没有问题，精神食欲大小便正常就可以去打疫苗了<\/p><p data-pid=\"xeuW3Lmx\">打完疫苗之后小猫咪才不会感染猫瘟这些病毒<\/p>"
	}, {
		"content": "<p data-pid=\"kLnFj_75\">太可爱了吧。感觉都不到2个月。 喂喂猫粮加羊奶。看看<\/p>",
		"realContentLength": 26,
		"url": "https://www.zhihu.com/question/531279423/answer/-1814240826",
		"voteCount": "<p data-pid=\"kLnFj_75\">太可爱了吧。感觉都不到2个月。 喂喂猫粮加羊奶。看看<\/p>"
	}],
	"topics": [{
		"url": "https://www.zhihu.com/api/v4/topics/19554935",
		"name": "猫"
	}, {
		"url": "https://www.zhihu.com/api/v4/topics/19556592",
		"name": "小区"
	}, {
		"url": "https://www.zhihu.com/api/v4/topics/19661000",
		"name": "野猫"
	}],
	"question": {
		"title": "我在小区捡了一只小猫不知道多大了该怎么喂养 大家帮我看一下?",
		"detail": "<p><\/p><a class=\"video-box\" href=\"https://link.zhihu.com/?target=https%3A//www.zhihu.com/video/1505130749309648896\" target=\"_blank\" data-video-id=\"\" data-video-playable=\"\" data-name=\"这是他的样子\" data-poster=\"https://pic3.zhimg.com/v2-cf0902d6952693938fb2692fa249ac65.jpg\" data-lens-id=\"1505130749309648896\"><img class=\"thumbnail\" src=\"https://pic3.zhimg.com/v2-cf0902d6952693938fb2692fa249ac65.jpg\"/><span class=\"content\"><span class=\"title\">这是他的样子<span class=\"z-ico-extern-gray\"><\/span><span class=\"z-ico-extern-blue\"><\/span><\/span><span class=\"url\"><span class=\"z-ico-video\"><\/span>https://www.zhihu.com/video/1505130749309648896<\/span><\/span><\/a><p><\/p><a class=\"video-box\" href=\"https://link.zhihu.com/?target=https%3A//www.zhihu.com/video/1505130788835934208\" target=\"_blank\" data-video-id=\"\" data-video-playable=\"\" data-name=\"\" data-poster=\"https://pic3.zhimg.com/v2-dda12b0915e4371e3c0531669d32501f.jpg\" data-lens-id=\"1505130788835934208\"><img class=\"thumbnail\" src=\"https://pic3.zhimg.com/v2-dda12b0915e4371e3c0531669d32501f.jpg\"/><span class=\"content\"><span class=\"title\"><span class=\"z-ico-extern-gray\"><\/span><span class=\"z-ico-extern-blue\"><\/span><\/span><span class=\"url\"><span class=\"z-ico-video\"><\/span>https://www.zhihu.com/video/1505130788835934208<\/span><\/span><\/a><p><\/p>"
	}
}
```

- ## data after process

```json
{
	"text": "我在小区捡了一只小猫不知道多大了该怎么喂养 大家帮我看一下?\n<p></p><a class=\"video-box\" href=\"https://link.zhihu.com/?target=https%3A//www.zhihu.com/video/1505130749309648896\" target=\"_blank\" data-video-id=\"\" data-video-playable=\"\" data-name=\"这是他的样子\" data-poster=\"https://pic3.zhimg.com/v2-cf0902d6952693938fb2692fa249ac65.jpg\" data-lens-id=\"1505130749309648896\"><img class=\"thumbnail\" src=\"https://pic3.zhimg.com/v2-cf0902d6952693938fb2692fa249ac65.jpg\"/><span class=\"content\"><span class=\"title\">这是他的样子<span class=\"z-ico-extern-gray\"></span><span class=\"z-ico-extern-blue\"></span></span><span class=\"url\"><span class=\"z-ico-video\"></span>https://www.zhihu.com/video/1505130749309648896</span></span></a><p></p><a class=\"video-box\" href=\"https://link.zhihu.com/?target=https%3A//www.zhihu.com/video/1505130788835934208\" target=\"_blank\" data-video-id=\"\" data-video-playable=\"\" data-name=\"\" data-poster=\"https://pic3.zhimg.com/v2-dda12b0915e4371e3c0531669d32501f.jpg\" data-lens-id=\"1505130788835934208\"><img class=\"thumbnail\" src=\"https://pic3.zhimg.com/v2-dda12b0915e4371e3c0531669d32501f.jpg\"/><span class=\"content\"><span class=\"title\"><span class=\"z-ico-extern-gray\"></span><span class=\"z-ico-extern-blue\"></span></span><span class=\"url\"><span class=\"z-ico-video\"></span>https://www.zhihu.com/video/1505130788835934208</span></span></a><p></p>\n<p data-pid=\"uu9p6vfB\">可以先送去附近宠物
	医院做个体检， 一般正常费用在一百多点。 < /p><p data-pid=\"RDqvmitt\">并且做好驱虫。</p > < p data - pid = \"5dllsPsC\">年龄过小还是需要购买羊奶粉搭配猫粮喂养。</p>",
	"url": "https://www.zhihu.com/question/531279423/answer/-1825491901"
}

{
	"text": "我在小区捡了一只小猫不知道多大了该怎么喂养 大家帮我看一下?\n<p></p><a class=\"video-box\" href=\"https://link.zhihu.com/?target=https%3A//www.zhihu.com/video/1505130749309648896\" target=\"_blank\" data-video-id=\"\" data-video-playable=\"\" data-name=\"这是他的样子\" data-poster=\"https://pic3.zhimg.com/v2-cf0902d6952693938fb2692fa249ac65.jpg\" data-lens-id=\"1505130749309648896\"><img class=\"thumbnail\" src=\"https://pic3.zhimg.com/v2-cf0902d6952693938fb2692fa249ac65.jpg\"/><span class=\"content\"><span class=\"title\">这是他的样子<span class=\"z-ico-extern-gray\"></span><span class=\"z-ico-extern-blue\"></span></span><span class=\"url\"><span class=\"z-ico-video\"></span>https://www.zhihu.com/video/1505130749309648896</span></span></a><p></p><a class=\"video-box\" href=\"https://link.zhihu.com/?target=https%3A//www.zhihu.com/video/1505130788835934208\" target=\"_blank\" data-video-id=\"\" data-video-playable=\"\" data-name=\"\" data-poster=\"https://pic3.zhimg.com/v2-dda12b0915e4371e3c0531669d32501f.jpg\" data-lens-id=\"1505130788835934208\"><img class=\"thumbnail\" src=\"https://pic3.zhimg.com/v2-dda12b0915e4371e3c0531669d32501f.jpg\"/><span class=\"content\"><span class=\"title\"><span class=\"z-ico-extern-gray\"></span><span class=\"z-ico-extern-blue\"></span></span><span class=\"url\"><span class=\"z-ico-video\"></span>https://www.zhihu.com/video/1505130788835934208</span></span></a><p></p>\n<p data-pid=\"uu9p6vfB\">可以先送去附近宠物
	医院做个体检， 一般正常费用在一百多点。 < /p><p data-pid=\"RDqvmitt\">并且做好驱虫。</p > < p data - pid = \"5dllsPsC\">年龄过小还是需要购买羊奶粉搭配猫粮喂养。</p>",
	"url": "https://www.zhihu.com/question/531279423/answer/-1825491901"
}

```