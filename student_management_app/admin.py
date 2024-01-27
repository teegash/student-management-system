from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AdminHOD, Attendance, AttendanceReport, Courses, FeedBackStaff, FeedBackStudent, NotificationStaffs, NotificationStudent, LeaveReportStaff, LeaveReportStudent, Staffs, Students, Subjects

admin.register(AdminHOD, Attendance, AttendanceReport, Courses, FeedBackStaff, FeedBackStudent, NotificationStaffs, NotificationStudent, LeaveReportStaff, LeaveReportStudent, Staffs, Students, Subjects)(admin.ModelAdmin)

# Always remember to register your models here otherwise they wont migrate