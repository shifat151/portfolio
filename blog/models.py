from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.



class Blog(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    description = RichTextField(verbose_name='Job Description')
    image=models.ImageField(upload_to='images/',blank=True)
    blog_url=models.URLField(blank=True)
    short_body=[]


    def summary(self):
        self.short_body=self.description.split()
        if len(self.short_body)<100:
            return self.description
        else:
            return ' '.join(self.short_body[:100])+'.....'
            

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    
    def __str__(self):
        return self.title
    