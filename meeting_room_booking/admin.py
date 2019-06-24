from django.contrib import admin

# Register your models here.

from meeting_room_booking.models import Employee,Rooms,Bookings,Facilities,Feedback,Cancellations

admin.site.register(Employee)
admin.site.register(Rooms)
admin.site.register(Bookings)
admin.site.register(Facilities)
admin.site.register(Feedback)
admin.site.register(Cancellations)
