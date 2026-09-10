from django.db import models

# Create your models here.
from django.db import models

# 0. User Registration
class userregistration(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    contact = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 1. User Login
class userlogin(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

# 2. Department Table
class department(models.Model):
    department_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=20)
    head_officer = models.CharField(max_length=50)

# 3. Grievance Category Table
class grievancecategory(models.Model):
    category_name = models.CharField(max_length=50)
    department = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    priority_level = models.CharField(max_length=20)

# 4. Grievance Table
class grievance(models.Model):
    grievance_id = models.CharField(max_length=10, unique=True)
    citizen = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=200)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    photo = models.FileField(upload_to='documents/', null=True, blank=True)
    submission_date = models.CharField(max_length=25)
    priority = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

# 5. Infrastructure Asset Table
class infrastructureasset(models.Model):
    asset_name = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    department = models.CharField(max_length=40)
    installation_date = models.CharField(max_length=25)
    last_maintenance_date = models.CharField(max_length=25)
    condition_status = models.CharField(max_length=20)
    photo = models.FileField(upload_to='documents/', null=True, blank=True)

# 6. Grievance Assignment Table
class grievanceassignment(models.Model):
    grievance = models.CharField(max_length=40)
    assigned_officer = models.CharField(max_length=40)
    department = models.CharField(max_length=40)
    assigned_date = models.CharField(max_length=25)
    expected_resolution_date = models.CharField(max_length=25)
    status = models.CharField(max_length=20)

# 7. Grievance Update Table
class grievanceupdate(models.Model):
    grievance = models.CharField(max_length=40)
    officer = models.CharField(max_length=40)
    update_date = models.CharField(max_length=25)
    description = models.CharField(max_length=300)
    photo = models.FileField(upload_to='documents/', null=True, blank=True)
    status = models.CharField(max_length=20)

# 8. Infrastructure Monitoring Table
class infrastructuremonitoring(models.Model):
    asset = models.CharField(max_length=40)
    monitored_by = models.CharField(max_length=40)
    inspection_date = models.CharField(max_length=25)
    condition_report = models.CharField(max_length=300)
    defects_found = models.CharField(max_length=200)
    photo = models.FileField(upload_to='documents/', null=True, blank=True)
    action_taken = models.CharField(max_length=200)

# 9. Feedback Table
class feedback(models.Model):
    citizen = models.CharField(max_length=40)
    grievance = models.CharField(max_length=40)
    rating = models.CharField(max_length=10)
    comments = models.CharField(max_length=200)
    feedback_date = models.CharField(max_length=25)

# 10. Notification Table
class notification(models.Model):
    user = models.CharField(max_length=40)
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=300)
    notification_date = models.CharField(max_length=25)
    priority = models.CharField(max_length=10)

# 11. Document Table
class document(models.Model):
    user = models.CharField(max_length=40)
    grievance = models.CharField(max_length=40)
    document_type = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    document_file = models.FileField(upload_to='documents/', null=True, blank=True)
