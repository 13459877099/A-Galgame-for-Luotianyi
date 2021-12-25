# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define you = Character("你")
define lty = Character("天依",color = "#66ccff")
define Slowdissolve = Dissolve(1.0) #定义溶解转场

# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。

    scene bg 卧室门 #显示场景"bg 卧室门.jpg"
    with Slowdissolve
    "咚咚咚（敲门声）" #旁白
    you"天依,起床啦" 

    scene bg sleep #显示场景"bg sleep.jpg", 非相同分辨率图片不可使用,需统一为1920x1080
    with Slowdissolve
    lty"怎么啦，一大早就叫我起床"
    lty"我还没睡够呢"
    
    scene bg 卧室 #显示场景"卧室"
    with Slowdissolve
    
    show ty tired
    you"……天依最近还是很忙吗"
    "天依抬起头，与你四目相对，绿宝石一样的眼眸里盛满了疲惫"
    lty"最近还好啦，不过下个月还有新的企划曲与演出，早些准备还是比较好吧……"
    
    hide ty tired
    with Slowdissolve
    "你宠溺的捏了捏天依有些婴儿肥的脸"

    show ty shy with Slowdissolve
    with vpunch
    
    
    lty"诶……你干嘛！！"
    you"那我们今天出去逛逛吧，今天天气挺好的"

    hide ty shy
    show ty smile at left with fade
    "少女疲惫的脸上露出了这几天罕见的笑容"
    lty"好呀~"
    you"内心OS:天依真开心啊，共鸣翼都出来了,这是多久没出去玩了啊"
    lty"快走快走！我要去品尝M记的新品！"

    scene bg 公园
    with Slowdissolve
    "你和天依来到了公园"
    show ty smile with fade
    lty"啦啦啦啦啦，今天天气真好呀！"

    scene bg_ty_crema1 with Slowdissolve
    lty"快来快来，快给我拍照"

    scene bg_ty_crema2 with Slowdissolve
    lty"这个角度拍照最好看哦"

    scene bg_ty_crema3 with Slowdissolve
    lty "这个娃娃好可爱！"

    scene bg 公园 with fade
    show ty smile with moveinright
    show ty smile at center with move
    you"我的小公主……我们还是休息一会吧"
    lty"好吧"
    "天依坐在你的旁边，拿出你背包里的矿泉水，咕噜噜地喝了一口"


    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # “eileen happy.png”的文件来将其替换掉。

    # show eileen happy

    # 此处为游戏结尾。

    return
 