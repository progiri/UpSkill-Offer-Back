from django.db import models

class Offer(models.Model):
    title = models.CharField(max_length=60, verbose_name='title')
    # 如果薪水为0则表示'薪水面谈'
    salary = models.PositiveIntegerField(default=0, verbose_name='salary') 
    org = models.CharField(max_length=60, verbose_name='organization')
    addr = models.CharField(max_length=60, verbose_name='address')
    desc = models.TextField('description')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='create date')

    class Meta:
        db_table = 'offer'
        verbose_name = 'offer'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s' % self.title



class Resume(models.Model):
    full_name = models.CharField(max_length=60, verbose_name='full name')
    github = models.URLField(max_length=200, verbose_name='github link')
    email = models.EmailField(verbose_name='email')
    phone = models.CharField(max_length=20, verbose_name='phone number')
    target_offer = models.ForeignKey(to='offer.Offer', on_delete=models.CASCADE, verbose_name='target offer')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='create date')

    class Meta:
        db_table = 'resume'
        verbose_name = 'resume'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s' % self.full_name
