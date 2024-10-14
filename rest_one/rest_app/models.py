from django.db import models



class Program(models.Model):
    program_name = models.CharField(max_length= 100)
    program_code =  models.CharField(max_length= 20)
    program_duration = models.CharField(max_length= 6, default= "3 yrs")

    def __str__(self):
        return  self.program_code

    class Meta:
        db_table = 'program'


class Student(models.Model):
    CHOICES = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    )
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    gender = models.CharField(max_length=10, choices=CHOICES)
    phone_number = models.CharField(max_length= 14)
    reg_no =  models.CharField(max_length= 15)
    registered = models.BooleanField(default=False)
    program = models.ForeignKey('Program', on_delete=models.CASCADE)
    yos = models.IntegerField(default= 1)
    created_at =  models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.reg_no

    class Meta:
        db_table ='student'
        ordering =['first_name']



{
    "first_name" : "Michael",
    "last_name" : "Michael",
    "gender" : "MALE",
    "phone_number" : "255765656556",
    "reg_no" : "T22-03-10111",
    "registered" : False,
    "program" : 1,
    "yos" : 1,
}