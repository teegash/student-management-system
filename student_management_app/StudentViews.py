import datetime
from django.http import HttpResponse
from django.shortcuts import render

from student_management_app.models import Attendance, AttendanceReport, Courses, CustomUser, Students, Subjects




def student_home(request):
    return render(request,"student_template/student_home_template.html")


def student_view_attendance(request):
    student=Students.objects.get(admin=request.user.id)
    course=student.course_id
    subjects=Subjects.objects.filter(course_id=course)
    return render(request,"student_template/student_view_attendance.html",{"subjects":subjects})


def student_view_attendance_post(request):
    subject_id=request.POST.get("subject")
    start_date=request.POST.get("start_date")
    end_date=request.POST.get("end_date")
    
    start_date_parse=datetime.datetime.strptime(start_date,"%Y-%m-%d").date()
    end_date_parse=datetime.datetime.strptime(end_date,"%Y-%m-%d").date()
    subject_obj=Subjects.objects.get(id=subject_id)
    user_object=CustomUser.objects.get(id=request.user.id)
    stud_obj=Students.objects.get(admin=user_object)
    
    attendance=Attendance.objects.filter(attendance_date__range=(start_date_parse,end_date_parse),subject_id=subject_obj)
    attendance_reports=AttendanceReport.objects.filter(attendance_id__in=attendance,student_id=stud_obj)
    
    for attendance_report in attendance_reports:
        print("Date : "+str(attendance_report.attendance_id.attendance_date)," Status : "+str(attendance_report.status))
    
    return HttpResponse("OK")


