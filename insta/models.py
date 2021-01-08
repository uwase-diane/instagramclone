from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Profile(models.Model):
    firstname = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to = 'profile_photos/', null=True)
    bio = HTMLField()
    date = models.DateTimeField(auto_now_add=True, null=True)



    @classmethod
    def get_all_instagram_users(cls):
        instagram_users = cls.objects.all()
        return instagram_users

    def save_profile(self):
        self.save()
        
    def delete_profile():
        self.delete()

    @classmethod
    def update_profile(cls, id, value):
        cls.objects.filter(id = id).update(user_id = new_user)


    @classmethod
    def search_by_profile(cls, username):
        certain_user = cls.objects.filter(user__username__icontains = username)
        return certain_user

    def __str__(self):
        return self.user


class Image(models.Model):
    image_name = models.CharField(max_length=100, null=True)
    image_caption = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='uploads/', null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    likes = models.IntegerField(default=0)


    @classmethod
    def get_all_images(cls):
        images = cls.objects.all().prefetch_related('comments_set')
        return images

    def save_images(self):
        self.save()

    def delete_image(self):
        self.delete()


    @classmethod
    def update_caption(cls,id,caption):
        update_image = cls.objects.filter(id = id).update(image_caption = caption)
        return update_image

    def __str__(self):
        return self.image_caption

class Comments(models.Model):
    comment = models.CharField(max_length=100)
    posted_by = models.ForeignKey(Profile,on_delete=models.CASCADE, null = True)
    commented_image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

    def save_comments(self):
        self.save()

    def delete_comments(self):
        self.delete()

    def update_comment(self):
        self.update()

    def __str__(self):
        return self.posted_by

class Follow(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.from_user)
