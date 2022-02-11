from django.contrib.auth.models import User
from django.db import models
from core.school_choices import SCHOOL_CHOICES
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="core/static/avatars/")
    account_info = models.OneToOneField(        "AccountInfo", on_delete=models.CASCADE)
    basic_info = models.OneToOneField( "BasicInfo", on_delete=models.CASCADE)
    contact_info = models.OneToOneField(      "ContactInfo", on_delete=models.CASCADE, blank=True, null=True)
    friends = models.ManyToManyField(                                         "Profile", through="Friendship")
    def __str__(self):
        return self.account_info.name
class AccountInfo(models.Model):
    name = models.CharField(max_length=128)
    member_since = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
class BasicInfo(models.Model):
    SEX_CHOICES = (("M", "Male"), ("W", "Women"))
    STATUS_CHOICES = ((1, "Student (Full-Time)"),
(2, "Alumnus/Alumna"), (3, "Faculty"), (4, "Staff"), (5, "Grad Student"))
    school = models.PositiveIntegerField(choices=SCHOOL_CHOICES, blank=True, null=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)
    sex = models.CharField(max_length=1,         choices=SEX_CHOICES, blank=True)
    birthday = models.DateField(     blank=True, null=True)
    hometown = models.CharField(max_length=128,             blank=True)
    high_school = models.CharField(max_length=128,     blank=True)
class ContactInfo(models.Model):
    looking_for = models.CharField(max_length=258,  blank=True)
    interested_for = models.CharField(max_length=258,      blank=True)
    political_views = models.CharField(max_length=258,  blank=True)
    interests = models.CharField(max_length=258,        blank=True)
    clubs_and_jobs = models.CharField(   max_length=258, blank=True)
    favorite_books = models.CharField(  max_length=258, blank=True)
    favorite_movies = models.CharField(  max_length=258, blank=True)
    about_me = models.CharField(  max_length=512, blank=True)
class Friendship(models.Model):
    STATUS_CHOICES = (   (1, "Request for friendship"),
        (         2, "Request accepted"), (3, "Request denied"))
    request_from = models.ForeignKey("Profile",        on_delete=models.CASCADE,
                                     related_name="request_from")
    request_to = models.ForeignKey("Profile", on_delete=models.CASCADE,

                                   related_name="request_to")
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
class Message(models.Model):
    message_from = models.ForeignKey(  Profile,  on_delete=models.CASCADE,              related_name="message_from")
    message_to = models.ForeignKey(Profile,
                    on_delete=models.CASCADE,
               related_name="message_to")
    readed = models.BooleanField(
        default=False)
    created = models.DateTimeField(
        auto_now_add=True)
    title = models.CharField(max_length=35)
    body = models.TextField()
