
from django.shortcuts import render
from meeting_room_booking.models import Employee,Rooms,Bookings,Facilities,Feedback,Cancellations
from django.http import HttpResponse,HttpRequest,HttpResponseNotFound,HttpResponseRedirect
import json
from django.core import serializers
from datetime import datetime
# Create your views here.



def home(request):
    print('in home')

    return render(request,'meeting_room_booking/login.html', {})



def toAbout(request):
    print('in home')

    return render(request,'meeting_room_booking/about.html', {})



def toFAQ(request):
    print('in home')

    return render(request,'meeting_room_booking/faq.html', {})



def toContact(request):
    print('in home')

    return render(request,'meeting_room_booking/contact.html', {})



def tofeedback(request):
    print('in home')

    return render(request,'meeting_room_booking/feedback.html', {})


def toHome(request):

    uname = request.session['username']
    #return render(request,'meeting_room_booking/')



    return render(request,'meeting_room_booking/home.html',{'user':uname})

def toBook(request):

    #uname = request.GET['username']
    return render(request,'meeting_room_booking/booking.html',{})

def tosignup(request):

    #uname = request.GET['username']
    return render(request,'meeting_room_booking/signup.html',{})



#@csrf_exempt
def login(request):


    print('in login')
    username = request.GET['username']
    paswd = request.GET['pass']
    print(username)
    print(paswd)

    emp = Employee.objects.filter(username=username)
    print(emp[0].password)
    if (paswd == emp[0].password):
        #auth successfull
        print('correct')
        request.session['username'] = username
        request.session.modified = True
        return render(request,'meeting_room_booking/home.html',{'user':request.session['username']})

def signup(request):

    #collect all parameters and save to database

    name = request.GET.get('name')
    print(name)
    uname = request.GET.get('username','')
    password = request.GET.get('pass','')
    email = request.GET.get('mail','')
    des = request.GET.get('des','')
    dept = request.GET.get('dept','')
    addr = request.GET.get('addr','')
    pnumber = request.GET.get('pno','')
    emp = Employee.objects.filter(email=email)
    if(len(emp) == 0):
        # email doesn't exist, check for username

        emp1 = Employee.objects.filter(username=uname)

        if(len(emp1)==0):

            #username doesn't exist as well, add user
            emp_to_be_added = Employee.objects.create(name=name, username=uname, email=email, designation=des,
                                                      password=password, dept=dept, address=addr, phonenumber=pnumber)
            emp_to_be_added.save()
            return HttpResponse('USER ADDED')
        else:
            return HttpResponseNotFound('User already exists')



    else:

        return HttpResponseNotFound('Email address already exists')

#@csrf_exempt
def check_avail(request):


    #print('here')
    agen = request.GET['agen']
    date = request.GET['date']
    from_time = request.GET['timefrom']
    to_time = request.GET['timeto']
    capacity = request.GET['capacity']
    #get list of facilities as well

    isWifi = request.GET['wifi']
    isVid = request.GET['vid']
    isProjector = request.GET['proj']
    isBoard = request.GET['board']
    isAudio = request.GET['audio']
    isAC = request.GET['ac']
    #isVid = request.GET['vid']


    print(type(from_time))
    print(date)



    #print(capacity)

    #all rooms
    all_rooms = list(Rooms.objects.all())
    #print(all_rooms)
    #print(len(all_rooms))
    #now filter according to capacity
    for i,c in enumerate(all_rooms):

        #print(all_rooms[i].capacity)
        if (int(all_rooms[i].capacity) < int(capacity)):
            print('in here')
            del all_rooms[i]


    #print(len(all_rooms))

    #print('here again')


    roomids = []
    for i in all_rooms:
        roomids.append(i.roomID)

    #filter according to date and time


    #contains all booked objects
    booked_rooms =list( Bookings.objects.all())
    print(len(booked_rooms))
    if(len(booked_rooms)!=0):

        print('bookings present')
        for i,c in enumerate(all_rooms):
            for j,d in enumerate(booked_rooms):
                print('i'+str(all_rooms[i].pk))
                print('j'+str(booked_rooms[j].pk))
                if all_rooms[i].pk == booked_rooms[j].pk:
                    print('id matched')
                    x = booked_rooms[j].date
                    print(x)
                    d = datetime.strptime(date, "%Y-%m-%d").date()
                    print(d)
                    if (x == d): #if date is same then check time range
                        print('date is same')
                        #if range is overlapping, remove from the list
                        if (datetime.strptime(from_time,"%H:%M").time()<=booked_rooms[j].to_time) and (datetime.strptime(to_time,"%H:%M").time()>=booked_rooms[j].from_time):
                            del all_rooms[i]



    all_fac = list(Facilities.objects.all())

    #print(len(all_fac))


    #now filter according to facilities


    print('wifi '+str(isWifi))


    print('according to facilities')
    print(len(all_rooms))

    for i,c in enumerate(all_rooms):
        id = all_rooms[i].roomID
        print('id '+str(id))
        obj1 = list(Facilities.objects.filter(roomID=id))
        #print(all_rooms[i].roomID)
        ob = obj1[0]
        #print('um wtf')
        print(ob.pk)
        print(ob.isWifi)
        #compare requirements

        if (int(isWifi)==1) and (ob.isWifi==0):
            if(len(all_rooms)>0):
                print('deleted')
                del all_rooms[i]
            else:
                break


        if (int(isAC) == 1) and (ob.isAC==0):
            if (len(all_rooms)>0):
                print('deleted')
                del all_rooms[i]
            else:
                break


        if (int(isAudio)==1) and (ob.isAudio==0):
            if (len(all_rooms)>0):
                print('deleted')
                del all_rooms[i]
            else:
                break


        if (int(isBoard)==1) and (ob.isBoard==0):
            if (len(all_rooms)>0):
                print('deleted')
                del all_rooms[i]
            else:
                break

        if (int(isProjector)==1) and (ob.isProjector==0):
            if (len(all_rooms )>0):
                print('deleted')
                del all_rooms[i]
            else:
                break



        if (int(isVid)==1) and (ob.isVid==0):
            if (len(all_rooms)>0):
                print('deleted')
                del all_rooms[i]
            else:
                break


    #print('here it is')
    if(len(all_rooms)!=0):

        #print('in here now')
        #all_rooms_as_json = serializers.serialize('json', all_rooms)
        print(all_rooms)
        object_dict = {x.pk: x for x in all_rooms}
        print(object_dict)

        request.session['date'] = date
        request.session['fromtime'] = from_time
        request.session['totime'] = to_time
        request.session['agenda']= agen
        return render(request,'meeting_room_booking/availability.html',{'d':object_dict})

    else:

        #tanvi, redirect this to an error page which will display that rooms aren't available. Keep the sidebar so that user can go back to home
        return('No such rooms available')



def confirm(request):

    #in the radio button put name as id
    id = request.GET['id']
    date = request.session['date']
    from_time = request.session['fromtime']
    to_time = request.session['totime']
    agen = request.session['agenda']
    user = request.session['username']
    print('user '+user)

    #using above details to create an object and add to table
    ob = list(Employee.objects.filter(username=user))
    room_ob = list(Rooms.objects.filter(roomID=id))
    book = Bookings.objects.create(username=ob[0],agenda=agen,to_time = to_time,from_time=from_time,date=date,roomID=room_ob[0])

    book.save()

    #redirect to home
    return render(request,'meeting_room_booking/home.html',{})




def myBook(request):



    #this view will return a list of all bookings ever done by the user
    books = list(Bookings.objects.filter(username = request.session['username']))
    object_dict = {x.pk: x for x in books}


    # refer to test.html to understand how to display this in html
    return render(request,'meeting_room_booking/history.html',{'d':object_dict})



def cancelbook(request):

    #this view will delete from the bookings table

    #ask the user for booking ID

    print('in cancel')
    id = request.GET['id']
    reason = request.GET['reason']


    obj = Bookings.objects.filter(bookID=id)

    if(len(obj)==0):
        #bookind ID doesn't exist, redirect to some error page
        pass
        #remove pass when actual code is added


    else:

        print('here')

        ob = Cancellations.objects.create(bookID=obj[0],reason=reason)
        ob.save()
        obj.delete()
        return render(request,'meeting_room_booking/home.html')
        #redirect to home page or a page that displays deletion done, idk












#@csrf_exempt
def test(request):
    print(request.method)


    print(
        'hi'
    )
    id = request.GET['lid']
    print(id)
    return HttpResponse('DONE')

def feedback(request):

    print('here')
    name = request.GET['name']
    comments = request.GET['comms']
    sat = request.GET['sat']
    email = request.GET['email']

    print(name)

    to_add = Feedback.objects.create(satisfaction=sat,email=email,comments=comments,name=name)
    to_add.save()
    return render(request,'meeting_room_booking/home.html',{})


    #redirect back to home here
    return render(request,'meeting_room_booking/home.html',{})


def toCancel(request):

    #will redirect to cancellation page

    return render(request,'meeting_room_booking/cancel.html',{})

def toFeed(request):

    #will redirect to feedback page

    return render(request,'meeting_room_booking/feedback.html',{})


def toHistory(request):

    #will redirect to history

    return render(request, 'meeting_room_booking/history.html', {})







