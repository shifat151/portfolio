from django.db import models

# Create your models here.
class Profile(models.Model):
    pic=models.ImageField(upload_to='images/')
    pub_date=models.DateTimeField(auto_now=True)
    obj=models.TextField(blank=True)

    # ctime() method is for converting datetime string into a string
    def __str__(self):
        return self.pub_date.ctime()
# class Objective(models.Model):
#     obj=models.TextField(blank=True)
#     list_obj=[]
#     def __str__(self):
#         self.list_obj=self.obj.split()
#         return " ".join(self.list_obj[:5])+'...'

class Language(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    lang_name=models.CharField(max_length=20)
    lang_summary=models.CharField(max_length=200)
    

    # For admin views instead of object
    def __str__(self):
        return self.lang_name

class Framework(models.Model):
    framework_name=models.CharField(max_length=20)
    language=models.ForeignKey(Language,on_delete=models.CASCADE)

    def __str__(self):
        return self.framework_name

class Project(models.Model):
    proj_title=models.CharField(max_length=100)
    proj_desc=models.TextField()
    proj_link=models.URLField()
    frameworks=models.ManyToManyField(Framework)

    def __str__(self):
        return self.proj_title

class Academic(models.Model):
    exam_name=models.CharField(max_length=50)
    exam_school=models.CharField(max_length=50)
    exam_gpa=models.FloatField()
    exam_year=models.SmallIntegerField()

    new_list=[]
    adm_list=[]

    def __str__(self):
        self.new_list=self.exam_name.split()
        self.adm_list=list(map(lambda x:x[:1], self.new_list))
        return ".".join(self.adm_list)
        