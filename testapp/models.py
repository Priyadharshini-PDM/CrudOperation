from django.db import models
import uuid

class company(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_email=models.EmailField(max_length=100)
    emp_role=models.CharField(max_length=25)
    emp_contact=models.CharField(max_length=30)
    emp_salary=models.IntegerField()

    id=models.UUIDField(default=uuid.uuid4,unique=True ,primary_key=True,editable=False)

def __str__(self) -> str:
    return str(self.emp_name)