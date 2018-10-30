from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    post = models.ForeignKey('blog.Blog', on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name_plural = verbose_name = '评论'
        ordering = ['-created_time']

    def __str__(self):
        return self.text[:20]
