from django.db import models
from django.core.validators import RegexValidator


class Candidate(models.Model):

    serialnumber = models.AutoField(primary_key=True)
    candidate_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True, unique=True)
    mobile_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message= "Phone number must be entered in the format:  '+999999999'. Up to 12 digits allowed.")
    mobile_number = models.CharField(validators=[mobile_regex], max_length=12, blank=True)
    current_location = models.CharField(max_length=200, blank=True, null=True)
    nearest_city = models.CharField(max_length=200, blank=True, null=True)
    ug_course = models.CharField(max_length=200, blank=True, null=True)
    ug_institute_name = models.CharField(max_length=300, blank=True, null=True)
    ug_tier_one = models.BooleanField(default=False)
    ug_passing_year = models.IntegerField(blank=True, null=True)
    pg_course = models.CharField(max_length=100, blank=True, null=True)
    pg_institute_name = models.CharField(max_length=300, blank=True, null=True)
    pg_tier_one = models.BooleanField(default=False)
    pg_passing_year = models.IntegerField(blank=True, null=True)
    preferred_location = models.CharField(max_length=200, blank=True, null=True)
    resume = models.BooleanField(default=False)
    work_experience = models.FloatField(blank=True, null=True)
    analytics_experience = models.FloatField(blank=True, null=True)
    current_employer = models.CharField(max_length=200, blank=True, null=True)
    ctc = models.FloatField(blank=True, null=True)
    current_designation = models.CharField(max_length=100, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    any_other_course = models.CharField(max_length=200, blank=True, null=True)

