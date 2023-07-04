from django.db import models
from django.db import models
from user_app.models import UserProfile

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,blank=False)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    post_image = models.ImageField(upload_to='post_pics',blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.comment
    
class Like(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.post.title
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to='post_pics',blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.post.title
    
class PostVideo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_video = models.FileField(upload_to='post_videos',blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.post.title
    
class PostAudio(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_audio = models.FileField(upload_to='post_audios',blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.post.title
    
class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_file = models.FileField(upload_to='post_files',blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.post.title
    
class PostLink(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_link = models.URLField(max_length=200,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.post.title
    
class PostPoll(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_poll_question = models.CharField(max_length=100,blank=False)
    post_poll_option1 = models.CharField(max_length=100,blank=False)
    post_poll_option2 = models.CharField(max_length=100,blank=False)
    post_poll_option3 = models.CharField(max_length=100,blank=False)
    post_poll_option4 = models.CharField(max_length=100,blank=False)
    post_poll_option5 = models.CharField(max_length=100,blank=False)
    post_poll_option6 = models.CharField(max_length=100,blank=False)
    post_poll_option7 = models.CharField(max_length=100,blank=False)
    post_poll_option8 = models.CharField(max_length=100,blank=False)
    post_poll_option9 = models.CharField(max_length=100,blank=False)
    post_poll_option10 = models.CharField(max_length=100,blank=False)


class PostPollVote(models.Model):
    post_poll = models.ForeignKey(PostPoll, on_delete=models.CASCADE) #post_poll_id
    post_poll_option = models.CharField(max_length=100,blank=False) #poll option
    post_poll_vote = models.IntegerField(blank=False) #poll vote
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.post_poll.post.title

