from django.db import models

class LanguageEnum(models.TextChoices):
    PYTHON = 'python'
    JAVASCRIPT = 'javascript'
    TYPESCRIPT = 'typescript'
    HTML = 'html'
    

class AuditableMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True



class Snippet(AuditableMixin):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True, default='', max_length=1000)
    code = models.TextField(blank=False, null=False)
    language = models.CharField(choices=LanguageEnum.choices, max_length=100, blank=False, null=False)
    pinned = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', related_name='tagged_snippets', blank=True)

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name