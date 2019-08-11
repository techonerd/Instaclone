from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    # password = models.CharField(max_length=10,widget=forms.PasswordInput)

    def __str__(self):
        return self.username

class Post(models.Model):
    picture = models.ImageField()
    upload_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    comments = models.CharField(max_length=255)

    def __str__(self):
        return "Pic"+ str(self.upload_time)

class Profile(models.Model):
    # def get_user(self):
    #     return User.Object.get(user_id=1)
    dis_pic = models.ImageField()
    # user =models.ForeignKey(User, on_delete=models.CASCADE, default=get_user)
    # follower = models.ManyToManyField(to = User)
    # following = models.ManyToManyField(to = User)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    # def __str__(self):
    #     return "dp"+str(self.user.username)

    



