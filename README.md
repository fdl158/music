# music
音乐平台
# 项目文档
### 1.项目说明
>   非常感谢大家可以欣赏music这个项目，中文名称我的音乐，这个项目的本身非常的简单，没有什么技术难度！  

### 2.实现功能  
>   * 搜索功能  
>   * 用户中心的登录,注册  
>   * 音乐分类  
>   * 下载功能  
>   *  歌曲评论  
>   * 404页面等实现
#### 3.所需组件和环境
* 主要环境
>    python   3.6  
Django                  2.1.7  
Pymysql  
Pillow  
httplib2  
diff-match-patch  
odfpy  
openpyxl  
PyYAML 
pytz  
xlrd  
xlwt  
virtualenvwrapper

下载完成后安装依赖包: pip install -r requirment.txt 


### 4.安装  
>    1.下载该项目到你的虚拟环境中，也可以选择不用虚拟环境！  

>    2.下载完后，修改 **music/settings.py**里面的 **DATABASES** 数据库连接信息!  

>   3.然后进入项目下的music下,(根目录下有manage.py的目录)，目录执行 **python manage.py makemigrations**  

>   4.在执行 **python manage.py migrate**  

>   5.最后执行 **python manage.py createsuperuser**  

### 5.运行  
>   6.执行 **python manage.py runserver**  

>   7.然后执行 **http://127.0.0.0:8000**  

>   8.后台地址：**http://127.0.0.0:8000/admin**


###  项目效果图
![Image text](https://github.com/fdl158/music/blob/master/music2.jpg)


