from django.db import models

class RealTimeImage(models.Model):
    image = models.ImageField(upload_to='images/')
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"


from django.db import models

# Model to store interest submissions
class Interested(models.Model):
    SESSION_CHOICES = [
        ('Early Morning', 'Early Morning'),
        ('Day', 'Day'),
        ('Night', 'Night'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    age = models.IntegerField()  # New field for age
    starting_date = models.DateField()  # New field for starting date
    address = models.CharField(max_length=255, blank=True)  # Optional field for address
    session = models.CharField(max_length=20, choices=SESSION_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.session}"


from django.db import models

from django.db import models

class Trainers(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    experience = models.IntegerField(help_text="Years of experience")
    reg_no = models.CharField(max_length=50)
    about = models.TextField()
    photo = models.ImageField(upload_to='trainers/')  # New field for the trainer's photo

    def __str__(self):
        return self.name


class Review(models.Model):
    trainer = models.ForeignKey(Trainers, on_delete=models.CASCADE, related_name="reviews")
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField(default=5)

    def __str__(self):
        return f"Review for {self.trainer.name} by {self.user_name}"
