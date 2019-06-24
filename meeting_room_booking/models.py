from django.db import models

# Create your models here.

class Employee(models.Model):
    
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,primary_key=True)
    email = models.CharField(max_length=50,unique=True)
    designation = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phonenumber = models.IntegerField()

    class Meta:
        db_table = "employee"



class Rooms(models.Model):

    dept = models.CharField(max_length=50)
    roomID = models.IntegerField(primary_key=True)
    floor = models.IntegerField()
    #avail = models.BooleanField(default=True)
    capacity = models.IntegerField(default=10)
    name = models.CharField(max_length=20)


    class Meta:
        db_table = "rooms"


class Facilities(models.Model):

    roomID = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    isWifi = models.IntegerField()
    isVid = models.IntegerField()
    isProjector = models.IntegerField()
    isBoard = models.IntegerField()
    isAudio = models.IntegerField()
    isAC = models.IntegerField()

    class Meta:
        db_table = "facilities"


class Bookings(models.Model):
    bookID = models.AutoField(primary_key=True)
    username = models.ForeignKey(Employee,on_delete=models.CASCADE,default="aseem")
    agenda = models.TextField()
    date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    roomID = models.ForeignKey(Rooms, on_delete=models.CASCADE,default=0)

    class Meta:
        db_table = "bookings"




class Feedback(models.Model):

    satisfaction = models.CharField(max_length=20)
    comments = models.TextField(default='null')
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    class Meta:
        db_table = "feedback"


class Cancellations(models.Model):

    bookID = models.ForeignKey(Bookings,on_delete=models.CASCADE)
    reason = models.TextField(default='null')


    class Meta:
            db_table = "cancellations"










