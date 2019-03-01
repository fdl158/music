from django.db import models

# Create your models here.
# 歌曲分类表label
class Label(models.Model):
    label_id = models.AutoField(verbose_name='序号', primary_key=True)
    label_name = models.CharField(verbose_name='分类标签', max_length=10)
    def __str__(self):
        return self.label_name
    class Meta:
        # 设置Admin界面的显示内容
        verbose_name = '歌曲分类'
        verbose_name_plural =verbose_name

# 歌曲信息表song
class Song(models.Model):
    song_id = models.AutoField(verbose_name='序号', primary_key=True)
    song_name = models.CharField(verbose_name='歌名', max_length=50)
    song_singer = models.CharField(verbose_name='歌手', max_length=50)
    song_time = models.CharField(verbose_name='时长', max_length=10)
    song_album = models.CharField(verbose_name='专辑', max_length=50)
    song_languages = models.CharField(verbose_name='语种', max_length=20)
    song_type = models.CharField(verbose_name='类型', max_length=20)
    song_release = models.CharField(verbose_name='发行时间', max_length=20)
    song_img = models.ImageField(verbose_name='歌曲图片', max_length=20,upload_to='song_img/%Y/%m')
    song_lyrics = models.CharField(verbose_name='歌词', max_length=50, default='暂无歌词')
    song_file = models.CharField(verbose_name='歌曲文件', max_length=50)
    label = models.ForeignKey(Label, on_delete=models.CASCADE,verbose_name='歌名分类')
    def __str__(self):
        return self.song_name
    class Meta:
        # 设置Admin界面的显示内容
        verbose_name = '歌曲信息'
        verbose_name_plural = verbose_name

# 歌曲动态表dynamic
class Dynamic(models.Model):
    dynamic_id = models.AutoField(verbose_name='序号', primary_key=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='歌名')
    dynamic_plays = models.IntegerField(verbose_name='播放次数')
    dynamic_search = models.IntegerField(verbose_name='搜索次数')
    dynamic_down = models.IntegerField(verbose_name='下载次数')
    class Meta:
        # 设置Admin界面的显示内容
        verbose_name = '歌曲动态'
        verbose_name_plural = verbose_name

# 歌曲点评表comment
class Comment(models.Model):
    comment_id = models.AutoField(verbose_name='序号', primary_key=True)
    comment_text = models.CharField(verbose_name='内容', max_length=500)
    comment_user = models.CharField(verbose_name='用户', max_length=20)
    song = models.ForeignKey(Song, on_delete=models.CASCADE,verbose_name='歌名')
    comment_date = models.CharField(verbose_name='日期', max_length=50)
    class Meta:
        # 设置Admin界面的显示内容
        verbose_name = '歌曲评论'
        verbose_name_plural = verbose_name