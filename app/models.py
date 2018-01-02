from django.db import models

# Create your models here.

class Sample(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=True, default='')
    img_name = models.CharField(max_length=100, blank=True, default='')
    image = models.ImageField(blank=True, upload_to='media/img/sample/%Y/%m/%d', help_text='150x150px', verbose_name='Image link')
    doc = models.FileField(upload_to='doc/', default='doc/none/no-pdf.doc')
    info = models.TextField()   
    owner = models.ForeignKey('auth.user', related_name='sample')
    
    class Meta:
        ordering = ('created',)
    
    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url)
        else:
            return '(No image)'
    image_img.short_description = 'Image'
    image_img.allow_tags = True

    def __unicode__(self):
        return self.name

class Page(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    pageid = models.CharField(max_length=50, blank=False, default='index')
    header = models.CharField(max_length=150, blank=True, default='')    
    message = models.TextField(blank=True)
    urltext = models.CharField(max_length=100, blank=True, default='')
    project = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.user', related_name='page')
    
    class Meta:
        ordering = ('pageid',)

    def __unicode__(self):
        return self.pageid     

class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    page = models.ForeignKey(Page)
    name = models.CharField(max_length=150, blank=True, default='')
    info = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='media/img/item/%Y/%m/%d', help_text='150x150px', verbose_name='Image link')
    doc = models.FileField(upload_to='doc/', default='doc/none/no-pdf.doc')
    button = models.CharField(max_length=100, blank=True, default='')
    urltext = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.user', related_name='items')
    
    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name                

    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url)
        else:
            return '(No image)'
    image_img.short_description = 'Image'
    image_img.allow_tags = True
