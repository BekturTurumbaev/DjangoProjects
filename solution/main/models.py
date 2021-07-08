from django.db import models


# ---------------------------------------------------------------------------------------------------

class HomeViewSubjects1(models.Model):
    header = models.CharField(max_length=100)
    description = models.TextField()
    description2 = models.TextField()
    button = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.header

# ---------------------------------------------------------------------------------------------------

class AboutViewSubjects1(models.Model):
    number = models.IntegerField()
    header = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.header

class AboutViewSubjects2(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.text

class AboutViewSubjects3(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    duty = models.CharField(max_length=100)
    description = models.TextField()
    avatar = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

class AboutViewSubjects4(models.Model):
    image = models.CharField(max_length=100)
    header = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.header

class AboutViewSubjects5(models.Model):
    logo = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.logo

# ---------------------------------------------------------------------------------------------------

class NewsViewSubjects1(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.text

class NewsViewSubjects2(models.Model):
    logo = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.logo

class NewsViewSubjects3(models.Model):
    image = models.CharField(max_length=100)
    header = models.CharField(max_length=200)
    descriprion = models.TextField()
    button = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.header

# ---------------------------------------------------------------------------------------------------

class ServicesViewSubjects1(models.Model):
    header = models.CharField(max_length=100)
    descriprion = models.TextField()
    button = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.header

class ServicesViewSubjects2(models.Model):
    image = models.CharField(max_length=100)
    header = models.CharField(max_length=100)
    descriprion = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.header

class ServicesViewSubjects3(models.Model):
    image = models.CharField(max_length=100)
    header = models.CharField(max_length=100)
    descriprion = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.header

# ---------------------------------------------------------------------------------------------------