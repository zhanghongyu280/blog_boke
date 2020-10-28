from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def login(request):


    return render(request,"login.html")

#返回验证的图片
import random
def get_validCode_img(request):
    def get_random_color():
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

   #生成一个图片
    from PIL import Image,ImageDraw,ImageFont
    from io import BytesIO
    import random
    img=Image.new("RGB",(270,40),color=get_random_color())
    #画板显示在哪里作画
    draw=ImageDraw.Draw(img)
    kumo_font=ImageFont.truetype("static/font/kumo.ttf",size=32)
    valid_code_str = ""
    for i in range(5):
        random_num = str(random.randint(0, 9))
        random_low_alpha = chr(random.randint(95, 122))
        random_upper_alpha = chr(random.randint(65, 90))
        random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
        draw.text((i * 50 + 20, 5), random_char, get_random_color(), font=kumo_font)
        # 保存验证码
        valid_code_str += random_char

    # 验证码的点和线
    # width=270
    # height=40
    # for i in range(10):
    #     x1=random.randint(0,width)
    #     x2=random.randint(0,width)
    #     y1=random.randint(0,height)
    #     y2=random.randint(0,height)
    #     draw.line((x1,y1,x2,y2),fill=get_random_color())
    #
    # for i in range(100):
    #     draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
    #     x = random.randint(0, width)
    #     y = random.randint(0, height)
    #     draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())

    print("valid_code_str", valid_code_str)
    #内存操作
    f=BytesIO()
    img.save(f,'png')
    data=f.getvalue()

    return HttpResponse(data)
