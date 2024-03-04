import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from student_management_app.models import SessionYearModel, Students, Subjects


def staff_home(request):
    return render(request,"staff_template/staff_home_template.html")

def staff_take_attendance(request):
    subjects=Subjects.objects.filter(staff_id=request.user.id)
    session_years=SessionYearModel.object.all()
    return render(request,"staff_template/staff_take_attendance.html",{"subjects":subjects,"session_years":session_years})

@csrf_exempt
def get_students(request):
    subject_id=request.POST.get("subject")
    session_year=request.POST.get("session_year")
    
    subject=Subjects.objects.get(id=subject_id)
    session_model=SessionYearModel.object.get(id=session_year)
    students=Students.objects.filter(course_id=subject.course_id,session_year_id=session_model)
    list_data=[]
    
    for student in students:
        data_small={"id":student.admin.id,"name":student.admin.first_name+" "+student.admin.last_name}
        list_data.append(data_small)
        
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)
    
@csrf_exempt
def save_attendance_data(request):
    student_ids=request.POST.getlist("student_ids[]")
    print(student_ids)
    return HttpResponse("OK")
    # subject_id=request.POST.get("subject_id")
    # attendance_date=request.POST.get("attendance_date")
    # session_year_id=request.POST.get("session_year_id")
    
    # subject_model=Subjects.objects.get(id=subject_id)
    # session_model=SessionYearModel.object.get(id=session_year_id)
    # json_student=json.loads(student_ids)
    # print(subject_model)
    # print(session_model)
    # print(attendance_date)
    # print(json_student)
    
    # for student_id in json_student:
    #     student=Students.objects.get(admin=student_id)
    #     attendance=StudentsAttendance(student_id=student,subject_id=subject_model,attendance_date=attendance_date,session_year_id=session_model)
    #     attendance.save()
    
    # return HttpResponse("OK")

