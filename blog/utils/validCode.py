from PIL import Image,ImageDraw,ImageFont
from cnblog.settings import BASE_DIR
from io import BytesIO
import random,string
def get_valid_code_img(request):
    def get_random_color():
        return ((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    def get_random_char():
        random_cha = [random.choice(string.ascii_letters) for i in range(4)]
        return random_cha

    a = get_random_char()
    a = "".join(a)
    #方式一
    # with open("yanz.jpg","rb") as f:
    #     data=f.read()
    #方式二
    #img = Image.new("RGB",(227,33),color=get_random_color())
    #dir = BASE_DIR + "/static/blog/mystyle/img/validCode.png"
    # print(dir)
    # with open(dir, "wb") as f:
    #     img.save(f,"png")
    # with open(dir, "rb") as f:
    #     img = f.read()
    #方式三
    # img = Image.new("RGB",(227,33),color="red")
    # f = BytesIO()
    # img.save(f,"png")
    # img = f.getvalue()

    #方式四
    #生成画布
    img = Image.new("RGB",(227,33),color=get_random_color())
    #画出画布，获取画布对象
    draw = ImageDraw.Draw(img)
    #生成字体
    new_font = ImageFont.truetype("static/font/circleFont.ttf",size=20)

    valid_code_str = ""
    #生成随机字符
    for i in range(5):
        random_num = str(random.randint(0,9))
        random_low_alpha = chr(random.randint(95,122))
        random_upper_alpha = chr(random.randint(65,90))
        random_char = random.choice([random_num,random_low_alpha,random_upper_alpha])

        #验证码画到画布

        draw.text(((i+3)*25,5),random_char,get_random_color(),font=new_font)
        #保存验证码字符串
        valid_code_str+=random_char
    #draw.text((3 * 25, 5), a, get_random_color(), font=new_font)
    #生成噪点
    # width = 227
    # height = 33
    # for i in range(10):
    #     x1 = random.randint(0,width)
    #     x2 = random.randint(0,width)
    #     y1 = random.randint(0,height)
    #     y2 = random.randint(0,height)
    #     draw.line((x1,y1,x2,y2),fill=get_random_color())
    #
    # for i in range(10):
    #     draw.point([random.randint(0,width),random.randint(0,height)],fill=get_random_color())
    #     x = random.randint(0,width)
    #     y = random.randint(0,height)
    #     draw.arc((x,y,x+4,y+4),0,90,fill=get_random_color())
    # 将文件存到内存里而不是硬盘
    request.session["valid_code_str"]  = valid_code_str

    f = BytesIO()
    img.save(f,"png")
    img = f.getvalue()
    print(valid_code_str,"++++++++++++++++++=1111")

    return img
