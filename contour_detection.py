from PIL import Image

# 求图像img中(x,y)处像素的卷积c
def convolute(img, x, y):
    ########## Begin ##########
    juanjihe = [1,1,1,1,-8,1,1,1,1]
    L = []
    xl = [x - 1, x, x + 1]
    yl = [y - 1, y, y + 1]
    for j in yl:
        for i in xl:
            gray = img.getpixel((i, j))  # 取出灰度值
            L.append(gray)
    c = 0
    for i,j in zip(juanjihe,L):
        c = c + i*j
    ########## End ##########
    return c
 
 
# 对图像文件1进行边缘检测，并将结果保存为图像文件2
# 图像文件1和2的路径分别为path1和path2
def detectEdge(path1, path2):
    img1 = Image.open(path1)  # 图像1
    img1 = img1.convert('L')  # 将图像1转换为灰度图
    w, h = img1.size
    img2 = Image.new('L', (w, h), 'white')  # 图像2
    ########## Begin ##########
    ##此部分功能：依次求img1中每个像素的卷积c，再将c放到img2的对应位置
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            c = convolute(img1, x, y)  # 计算卷积c
            if c>0:
                s=0
            else:
                s=255
            img2.putpixel((x, y), s)  # 再将c放到img2的对应位置
    ########## End ##########
    img2.save(path2)
 
 
path1 = 'blur_test3.jpg'  # 原始图像
path2 = 'blur_test3_detect.jpg'  # 检测到的边缘图像
detectEdge(path1, path2)