from django.db import models

	
def get_post_image_path(instance, filename):
    return 'post/%s/%s' % (instance.pk, filename)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=get_post_image_path, default='')
    
    def save(self, *args, **kwargs):
        if self.id is None:
            # 이미지 제외하고 업로드
            temp_image = self.image
            self.image = None
            super().save(*args, **kwargs)
            
            # 이미지 추가
            self.image = temp_image
        # 이미지만 업로드 => 이때는 pk가 존재!
        super().save(*args, **kwargs)

class PostComent(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
