from django.db import models


# Create your models here.
class Launch(models.Model):

    def __init__(self, mission_name, rocket_name, description, launch_date, image_url, upcoming, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mission_name = mission_name
        self.rocket_name = rocket_name
        self.description = description
        self.launch_date = launch_date
        self.image_url = image_url
        self.upcoming = upcoming
