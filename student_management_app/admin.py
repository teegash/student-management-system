from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from student_management_app.models import CustomUser

# Register your models here.
from django.contrib import admin
from .models import AdminHOD, Attendance, AttendanceReport, Courses, FeedBackStaff, FeedBackStudent, NotificationStaffs, NotificationStudent, LeaveReportStaff, LeaveReportStudent, Staffs, Students, Subjects

admin.register( AdminHOD, Attendance, AttendanceReport, Courses, FeedBackStaff, FeedBackStudent, NotificationStaffs, NotificationStudent, LeaveReportStaff, LeaveReportStudent, Staffs, Students, Subjects)(admin.ModelAdmin)

# Always remember to register your models here otherwise they wont migrate


class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser,UserModel)