"""
派生精灵子类
新建plane_sprites.py文件
定义GameSprite 继承自pygame.sprite.Sprite

注意：如果一个类的父类不是object
      在重写初始化方式时，一定要先 super()一下父类的__init__方法
      保证父类中实现__init__代码能够被正常执行

GameSprite   ：image      rect      speed
            __init__(self,image_name,speed=1):
            update(self):

属性：image 精灵图像、使用image_name 加载
      rect 精灵大小、默认使用图像大小
      speed 精灵移动速度，默认为 1
方法  update 每次更新屏幕时在游戏循环内调用
      让精灵的self.rect.y += self.speed

提示：
    image 的 get_rect() 方法 可以返回 矩形对象 -- pygame.Rect(0,0,图像宽,图像高)的对象
"""
