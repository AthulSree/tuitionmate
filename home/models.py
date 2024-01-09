from django.db import models

# Create your models here.
class academicYear(models.Model):
    desc = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    class Meta:
        db_table = 'academic_year'

    def __str__(self):
        return self.desc

class studentClass(models.Model):
    year_id = models.ForeignKey(academicYear, on_delete=models.CASCADE)
    class_desc = models.CharField(max_length=10)

    class Meta:
        db_table = 'student_class'
    def __str__(self):
        return self.class_desc