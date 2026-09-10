import smtplib

import os

from .chatbot import get_ai_response

from flask import Flask, render_template

from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import date

from public.models import userlogin

from public.models import userregistration

from public.models import department

from public.models import grievancecategory

from public.models import grievance

from public.models import infrastructureasset

from public.models import grievanceassignment

from public.models import grievanceupdate

from public.models import infrastructuremonitoring

from public.models import feedback

from public.models import notification

from public.models import document

# Create your views here.

def insertuserlogin(request):
    if request.method == 'POST':
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 =request.POST.get('t3')
        userlogin.objects.create(username=s1, password=s2, type=s3)
        return render(request,'userlogin.html')
    return render(request, 'userlogin.html')

def viewuserlogin(request):
    userdict=userlogin.objects.all()
    return render(request,"showuserlogin.html",{"userdict":userdict})

def insertregister(request):
    if request.method == 'POST':
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        s6 = request.POST.get('t6')

        # Check duplicate email
        if userregistration.objects.filter(email=s2).exists():
            messages.error(request, "Email is already registered.")
            return redirect('insertregister')

        # Check duplicate mobile
        if userregistration.objects.filter(contact=s4).exists():
            messages.error(request, "Mobile number is already registered.")
            return redirect('insertregister')
        userregistration.objects.create(name=s1,email=s2,password=s3,contact=s4,city=s5,address=s6)
        userlogin.objects.create(username=s2,password=s3, type="citizen")
        # Store email in session
        request.session['registered_email'] = s2
        messages.success(request, "Registration successful! Please login.")
        return redirect('logcheck')
    return render(request, 'userregistration.html')

def viewregister(request):
    regdict=userregistration.objects.all()
    return render(request,"showregister.html",{"regdict":regdict})

def delreg(request,pk):
    userregistration.objects.get(pk=pk).delete()
    regdict = userregistration.objects.all()
    return render(request, "showregister.html", {'regdict': regdict})

def insertdepartment(request):
    if request.method == 'POST':
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        department.objects.create(department_name=s1,description=s2,contact_email=s3,contact_phone=s4,head_officer=s5)
        return render(request,'department.html')
    return render(request, 'department.html')

def viewdepartment(request):
    deptdict=department.objects.all()
    return render(request,"showdepartment.html",{"deptdict":deptdict})

def deldept(request,pk):
    department.objects.get(pk=pk).delete()
    deptdict = department.objects.all()
    return render(request, "showdepartment.html", {'deptdict': deptdict})

def insertgrevcat(request):
    if request.method == 'POST':
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        grievancecategory.objects.create(category_name=s1,department=s2,description=s3,priority_level=s4)
        return render(request,'grievancecategory.html')
    return render(request, 'grievancecategory.html')

def viewgrevcat(request):
    gcatdict=grievancecategory.objects.all()
    return render(request,"showgrevcat.html",{"gcatdict":gcatdict})

def delgcat(request,pk):
    grievancecategory.objects.get(pk=pk).delete()
    gcatdict = grievancecategory.objects.all()
    return render(request, "showgrevcat.html", {"gcatdict": gcatdict})

def insertgrievance(request):
    categories = grievancecategory.objects.all()
    username = request.session.get('username', '')
    # Generate Grievance ID
    p = grievance.objects.last()
    if p:
        num = int(p.grievance_id.split("-")[1]) + 1
    else:
        num = 1
    grievance_id = f"GRV-{num:03d}"
    if request.method == 'POST':
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        s6 = request.POST.get('t6')
        s7 = request.POST.get('t7')
        s8 = request.FILES.get('t8')
        s9 = request.POST.get('t9')
        grievance.objects.create(grievance_id=grievance_id, citizen=s1, category=s2, title=s3, description=s4, location=s5, latitude=s6, longitude=s7, photo=s8, submission_date=s9, priority="Medium", status="Pending")
        notification.objects.create(user=s1, title="Grievance Submitted",
            message=f"Your grievance '{grievance_id}' has been submitted successfully.",
            notification_date=date.today(),
            priority="Medium"
        )
        return render(request,'grievance.html', {'categories': categories, 'username': username, 'grievance_id': grievance_id, 'msg': 'Grievance submitted successfully'})
    return render(request, 'grievance.html', {'categories': categories, 'username': username, 'grievance_id': grievance_id})

def viewgriev(request):
    grievdict=grievance.objects.all()
    return render(request,"showgriev.html",{"grievdict":grievdict})

def delgriev(request,pk):
    grievance.objects.get(pk=pk).delete()
    grievdict = grievance.objects.all()
    return render(request, "showgriev.html", {"grievdict": grievdict})

def insertinfrasset(request):
    if request.method == 'POST':
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        s6 = request.POST.get('t6')
        s7 = request.POST.get('t7')
        s8 = request.FILES.get('t8')
        infrastructureasset.objects.create(asset_name=s1,asset_type=s2,location=s3,department=s4,installation_date=s5,last_maintenance_date=s6,condition_status=s7,photo=s8)
        return render(request,'frasset.html',{'msg':'Infrastructure asset registered successfully'})
    return render(request, 'frasset.html')

def viewinasset(request):
    inasdict=infrastructureasset.objects.all()
    return render(request,"showinasset.html",{"inasdict":inasdict})

def delinasset(request,pk):
    infrastructureasset.objects.get(pk=pk).delete()
    inasdict = infrastructureasset.objects.all()
    return render(request, "showinasset.html", {"inasdict": inasdict})

def insertgrievassign(request):
    grievances = grievance.objects.all()
    if request.method == 'POST':
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        s6 = request.POST.get('t6')
        grievanceassignment.objects.create(grievance=s1,assigned_officer=s2,department=s3,assigned_date=s4,expected_resolution_date=s5,status=s6)
        # Find the citizen who submitted this grievance
        g = grievance.objects.get(grievance_id=s1)
        citizen_email = g.citizen
        # Automatic notification
        notification.objects.create(
            user=citizen_email,
            title="Grievance Assigned",
            message=f"Your grievance {s1} has been assigned to {s3} department.",
            notification_date=date.today(),
            priority="High"
        )
        return render(request, 'grievassign.html', {'grievances': grievances, 'msg': 'Grievance assigned successfully'})
    return render(request,'grievassign.html',{'grievances': grievances})

def viewgassign(request):
    gassdict=grievanceassignment.objects.all()
    return render(request,"showgassign.html",{"gassdict":gassdict})

def delgassign(request,pk):
    grievanceassignment.objects.get(pk=pk).delete()
    gassdict = grievanceassignment.objects.all()
    return render(request, "showgassign.html", {"gassdict": gassdict})

def insertgrievupdate(request):
    grievances = grievance.objects.all()
    if request.method == 'POST':
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.FILES.get('t5')
        s6 = request.POST.get('t6')
        grievanceupdate.objects.create(grievance=s1,officer=s2,update_date=s3,description=s4,photo=s5,status=s6)
        # Find citizen automatically
        g = grievance.objects.get(grievance_id=s1)
        g.status = s6
        g.save()
        citizen_email = g.citizen
        # Automatic notification
        if s6 == "Completed" or s6 == "Resolved":
            notification.objects.create(
                user=citizen_email,
                title="Grievance Resolved",
                message=f"Your grievance {s1} has been resolved successfully.",
                notification_date=date.today(),
                priority="High"
            )
        else:
            notification.objects.create(
                user=citizen_email,
                title="Grievance Updated",
                message=f"A new update has been added to your grievance {s1}.",
                notification_date=date.today(),
                priority="Medium"
            )
        return render(request, 'grievanceupdate.html', {'grievances': grievances, 'msg': 'Grievance updated successfully'})
    return render(request, 'grievanceupdate.html', {'grievances': grievances})

def viewgupdate(request):
    username = request.session.get('username', '')
    usertype = request.session.get('usertype', '')
    if usertype == 'citizen':
        # Get this citizen's grievances
        my_grievances = grievance.objects.filter(citizen=username)
        # Get their grievance IDs
        grievance_ids = my_grievances.values_list('grievance_id', flat=True)
        # Show only updates for their grievances
        gupdatedict = grievanceupdate.objects.filter(grievance__in=grievance_ids)
    else:
        # Admin can see all updates
        gupdatedict = grievanceupdate.objects.all()
    return render(request, "showgupdate.html", {"gupdatedict": gupdatedict})

def delgupdate(request,pk):
    grievanceupdate.objects.get(pk=pk).delete()
    gupdatedict = grievanceupdate.objects.all()
    return render(request, "showgupdate.html", {"gupdatedict": gupdatedict})

def insertinframonitor(request):
    assets = infrastructureasset.objects.all()
    if request.method == 'POST':
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        s6 = request.FILES.get('t6')
        s7 = request.POST.get('t7')
        infrastructuremonitoring.objects.create(asset=s1,monitored_by=s2,inspection_date=s3,condition_report=s4,defects_found=s5,photo=s6,action_taken=s7)
        return render(request,'inframonitoring.html', {'assets': assets,
            'msg': 'Monitoring report submitted successfully'})
    return render(request, 'inframonitoring.html', {'assets': assets})

def viewinmonitor(request):
    inmondict=infrastructuremonitoring.objects.all()
    return render(request,"showinmonitor.html",{"inmondict":inmondict})

def delinmonitor(request,pk):
    infrastructuremonitoring.objects.get(pk=pk).delete()
    inmondict = infrastructuremonitoring.objects.all()
    return render(request, "showinmonitor.html", {"inmondict": inmondict})

def insertfeedback(request):
    username = request.session.get('username', '')
    # Get resolved grievance IDs from officer updates
    resolved_updates = grievanceupdate.objects.filter(status='Resolved')
    resolved_ids = resolved_updates.values_list('grievance', flat=True)
    # Get only this citizen's resolved grievances
    grievances = grievance.objects.filter(citizen=username, grievance_id__in=resolved_ids)
    if request.method == 'POST':
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        existing = feedback.objects.filter(citizen=s1, grievance=s2).exists()
        if existing:
            return render(request, 'feedback.html', {'username': username, 'grievances': grievances,
                'msg': 'You have already submitted feedback for this grievance.'})
        feedback.objects.create(citizen=s1,grievance=s2,rating=s3,comments=s4,feedback_date=date.today())
        return render(request,'feedback.html', {'username': username, 'grievances': grievances,
            'msg': 'Feedback submitted successfully'})
    return render(request, 'feedback.html', {'username': username, 'grievances': grievances})

def viewfeed(request):
    feeddict=feedback.objects.all()
    return render(request,"showfeed.html",{"feeddict":feeddict})

def delfeed(request,pk):
    feedback.objects.get(pk=pk).delete()
    feeddict = feedback.objects.all()
    return render(request, "showfeed.html", {"feeddict": feeddict})

def insertnotify(request):
    if request.method == 'POST':
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        notification.objects.create(user=s1,title=s2,message=s3,notification_date=s4,priority=s5)
        return render(request,'notification.html')
    return render(request, 'notification.html')

def viewnotify(request):
    username = request.session.get('username', '')
    notifdict = notification.objects.filter(user=username).order_by('-id')
    return render(request, 'shownotify.html', {'notifdict': notifdict})

def delnotify(request,pk):
    notification.objects.get(pk=pk).delete()
    notifdict = notification.objects.all()
    return render(request, "shownotify.html", {"notifdict": notifdict})

def insertdocument(request):
    username = request.session.get('username', '')
    grievances = grievance.objects.filter(citizen=username)
    if request.method == 'POST':
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.FILES.get('t5')
        # File validation
        allowed_extensions = ['.pdf', '.jpg', '.jpeg', '.png']
        extension = os.path.splitext(s5.name)[1].lower()
        if extension not in allowed_extensions:
            return render(request, 'document.html', {'username': username,'grievances': grievances,
                'msg': 'Invalid file format. Please upload PDF, JPG, JPEG or PNG.'})
        if s5.size > 5 * 1024 * 1024:
            return render(request, 'document.html', {'username': username, 'grievances': grievances,
                'msg': 'File size must be less than 5 MB.'})
        document.objects.create(user=s1, grievance=s2, document_type=s3, description=s4, document_file=s5)
        return render(request, 'document.html', {'username': username, 'grievances': grievances,
                'msg': 'Document submitted successfully'})
    return render(request, 'document.html', {'username': username, 'grievances': grievances})

def viewdocument(request):
    docdict=document.objects.all()
    return render(request,"showdocument.html",{"docdict":docdict})

def deldoc(request,pk):
    document.objects.get(pk=pk).delete()
    docdict = document.objects.all()
    return render(request, "showdocument.html", {"docdict": docdict})

def logcheck(request):
    email = request.session.pop('registered_email', '')
    if request.method == "POST":
        username = request.POST.get('t1')
        password = request.POST.get('t2')
        count = userlogin.objects.filter(username=username).count()
        if count >= 1:
            udata = userlogin.objects.filter(username=username).first()
            request.session['username'] = username
            upass = udata.password
            utype = udata.type.lower()
            request.session['usertype'] = utype

            if upass == password:
                if utype == 'citizen':
                    return render(request, 'public_home.html')
                if utype == 'officer':
                    return render(request, 'officer_home.html')
                if utype == 'admin':
                    return render(request, 'govt_home.html')
            else:
                return render(request, 'userlogin.html', {
                    'msg': 'Invalid password',
                    'email': email
                })
        else:
            return render(request, 'userlogin.html', {
                'msg': 'Invalid username',
                'email': email
            })

    return render(request, 'userlogin.html', {
        'email': email
    })

def changepassword(request):
    uname=request.session['username']
    if request.method == 'POST':
        currentpass = request.POST.get('t1', '')
        newpass = request.POST.get('t2', '')
        confirmpass = request.POST.get('t3', '')

        ucheck = userlogin.objects.filter(username=uname).values()
        for a in ucheck:
            u = a['username']
            p = a['password']
            if u == uname and currentpass == p:
                if newpass == confirmpass:
                    userlogin.objects.filter(username=uname).update(password=newpass)
                    return render(request,'changepassword.html',{'msg': 'Password has been changed successfully'})
                else:
                    return render(request, 'changepassword.html',{'msg': 'New password and confirm password do not match'})
            else:
                return render(request, 'changepassword.html',{'msg': 'Current password is incorrect'})
    return render(request, 'changepassword.html')


def forgotpassword(request):
    if request.method=="POST":
        uname = request.POST.get('t1', '')
        user = userlogin.objects.filter(username=uname).count()
        if user >= 1:
            userlog = userlogin.objects.filter(username=uname).values()
            for u in userlog:
                upass= u['password']
                content = upass
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login(
                    os.environ.get('EMAIL_HOST_USER'),
                    os.environ.get('EMAIL_HOST_PASSWORD')
                )
                mail.sendmail(
                    os.environ.get('EMAIL_HOST_USER'),
                    uname,
                    content
                )
                mail.close()
                messages.success(request, "Your password has been sent to your email.")
                return redirect('logcheck')
        else:
            return render(request,'forgotpassword.html', {'msg': 'Enter a valid username'})
    return render(request,'forgotpassword.html')

def showindex(request):
    return render(request,'index.html')

def public_home(request):
    return render(request,'public_home.html')

def officer_home(request):
    return render(request,'officer_home.html')

def govt_home(request):
    return render(request,'govt_home.html')

def r_depart(request):
    return render(request, 'roads_department.html')

def water_depart(request):
    return render(request, 'water_department.html')

def elect_depart(request):
    return render(request, 'elect_department.html')

def san_depart(request):
    return render(request, 'sani_department.html')

def chatbot(request):

    username = request.session.get("username")
    usertype = request.session.get("usertype")

    if not username:
        return redirect("logcheck")

    if usertype != "citizen":
        return redirect("logcheck")

    if request.method == "POST":

        user_message = request.POST.get("message")

        chat_history = request.session.get(
            "chat_history_" + username,
            []
        )

        bot_response = get_ai_response(
            username,
            user_message,
            chat_history
        )

        chat_history.append({
            "role": "user",
            "content": user_message
        })

        chat_history.append({
            "role": "assistant",
            "content": bot_response
        })

        request.session["chat_history_" + username] = chat_history

        return render(request, "chatbot.html", {
            "user_message": user_message,
            "bot_response": bot_response,
            "chat_history": chat_history
        })

    return render(request, "chatbot.html", {
        "chat_history": request.session.get(
            "chat_history_" + username,
            []
        )
    })


def chatbot_message(request):

    if request.method == "POST":

        username = request.session.get("username")
        usertype = request.session.get("usertype")

        if not username or usertype != "citizen":
            return JsonResponse({
                "error": "Please login as a citizen to use the chatbot."
            })

        user_message = request.POST.get("message")

        chat_history = request.session.get(
            "chat_history_" + username,
            []
        )

        bot_response = get_ai_response(
            username,
            user_message,
            chat_history
        )

        chat_history.append({
            "role": "user",
            "content": user_message
        })

        chat_history.append({
            "role": "assistant",
            "content": bot_response
        })

        request.session["chat_history_" + username] = chat_history

        return JsonResponse({
            "response": bot_response
        })

    return JsonResponse({
        "error": "Invalid request"
    })


def clear_chat(request):

    username = request.session.get("username")

    if username:
        request.session.pop(
            "chat_history_" + username,
            None
        )

    return redirect("chatbot")