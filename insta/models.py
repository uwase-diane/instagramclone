from django.db import models
from django.contrib.auth.models import User
import datetime as dt


class Image(models.Model):
    image = models.ImageField(upload_to='uploads/')
    name = models.CharField(max_length=100, blank=True)
    caption = models.TextField(max_length=100, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=true, null = True)

    @classmethod
    def save_image(self):
        self.save()

    @classmethod
    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, caption):
        captions = cls.objects.filter(caption_id=id).update(image_caption = caption)
        return caption

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    def __str__(self):
        return self.name
             
    

class Profile(models.Model):
    profilepic = models.ImageField(upload_to='',default ='')
    bio = models.TextField(max_length=100, blank=True, default="Bio")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name =  models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.user


    # @classmethod
    # def all_users(cls):
    #     users = cls.objects.all()
    #     return users

    # @classmethod
    # def save_profile(self):
    #     self.save()

    # @classmethod
    # def delete_profile(self):
    #     self.delete()

    # @classmethod
    # def update_profile(cls, id, value):
    #     cls.objects.filter(id = id).update(user_id = new_user)


    @classmethod
    def search_by_profile(cls,search_item):
        name = cls.objects.filter(usr_username_iscontains = search_item)
        return name


class Comment(models.Model):   
    comment = models.TextField()
    post = models.ForeignKey(Image, on_delete = models.CASCADE, )
    created_by = models.ForeignKey(Profile, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def update_comment(self):
        self.update()        


    def __str__(self):
        return self.created_by




class Follow(models.Model):
    followers = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')

    def __str__(self):
        return self.followers