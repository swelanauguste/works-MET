from django.db import models


class Report(models.Model):
    st = models.CharField(verbose_name="st", max_length=10)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    vis = models.IntegerField(default=0)
    t_cld = models.IntegerField(default=0)
    dd = models.IntegerField(default=0)
    fff = models.IntegerField(default=0)
    temp = models.FloatField(default=0)
    dp = models.FloatField(default=0)
    vp = models.FloatField(default=0, blank=True, null=True)
    rh = models.IntegerField(default=0)
    msl = models.FloatField(default=0)
    qnh = models.FloatField(default=0)
    w = models.IntegerField(default=0)
    ww = models.IntegerField(default=0)
    t_lcld = models.IntegerField(default=0)
    cld = models.IntegerField(default=0)
    low = models.IntegerField(default=0)
    mid = models.IntegerField(default=0)
    high = models.IntegerField(default=0)
    high2 = models.IntegerField(default=0)
    maxx = models.FloatField(default=0)
    minn = models.FloatField(default=0)
    rr = models.FloatField(default=0)
    rr_time = models.TimeField(null=True, blank=True)
    archive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return f"{self.st} - {self.date} - {self.time}"
