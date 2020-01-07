from django.db import models

# Create your models here.



class Blog(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/',blank=True)
    blog_url=models.URLField(blank=True)
    short_body=[]


    def summary(self):
        self.short_body=self.body.split()
        if len(self.short_body)<100:
            return self.body
        else:
            return ' '.join(self.short_body[:100])+'.....'
            

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    
    def __str__(self):
        return self.title
    