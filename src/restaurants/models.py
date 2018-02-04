from django.db import models
from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator
# Create your models here.




class Score(models.Model):
    Score_title = models.CharField(max_length=120,null=True, blank=True)
    Call_number = models.CharField(max_length=20, blank=True)
    collection = models.CharField(max_length=60,null=True, blank=True)
    author = models.CharField(max_length=60,null=True, blank=True)
    arranger = models.CharField(max_length=120,null=True, blank=True)
    editor = models.CharField(max_length=120,null=True, blank=True)
    Uniform_Title = models.CharField(max_length=120,null=True, blank=True)
    publisher = models.CharField(max_length=120,null=True, blank=True)
    place_of_publication =  models.CharField(max_length=120,null=True, blank=True)
    date_of_publication =  models.CharField(max_length=120,null=True, blank=True)
    Plate_Number = models.CharField(max_length=120,null=True, blank=True)
    ISSN = models.CharField(max_length=120,null=True, blank=True)
    Subject = models.CharField(max_length=120,null=True, blank=True)
    collation = models.CharField(max_length=120,null=True, blank=True)
    holdings = models.CharField(max_length=120, null=True,blank=True)
    medium = models.CharField(max_length=120,null=True, blank=True)
    key_signature= models.CharField(max_length=20,null=True, blank=True)
    condition= models.CharField(max_length=20,null=True, blank=True)
    cost= models.CharField(max_length=20,null=True, blank=True)
    acquisition_date= models.CharField(max_length=20,null=True, blank=True)
    notes = models.TextField(max_length=1000,null=True, blank=True, help_text="Enter a brief note")
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.Score_title

    @property
    def title(self):
        return self.Score_title

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
     if not instance.slug:
       instance.slug = unique_slug_generator(instance)
#def rl_post_save_receiver(sender, instance, *args, **kwargs):
 #    print('saved')
  #   print(instance.Call_number)
   #  if not instance.slug:
    #    instance.slug = unique_slug_generator(instance)
     #   instance.save()

pre_save.connect(rl_pre_save_receiver, sender=Score)

#post_save.connect(rl_post_save_receiver, sender=Score)
