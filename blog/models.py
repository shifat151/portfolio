from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.



class Blog(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    description = RichTextUploadingField()
    image=models.ImageField(upload_to='images/')
    blog_url=models.URLField(blank=True)
    short_body=[]

    class Meta:
        ordering=["-pub_date"]

    def summary(self):
        self.short_body=self.description.split()
        if len(self.short_body)<20:
            return self.description
        else:
            return ' '.join(self.short_body[:20])+'.....'
            

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    
    def __str__(self):
        return self.title
    