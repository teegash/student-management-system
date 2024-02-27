from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


# Middleware is a framework of hooksinto Django request/response processing.
# Its a light, low level plugin system for globally altering Django's input or output.
# It defines when a user request(Access URL Endpoint):
#     - the request will come to middleware first then further the request will be processed.
# This middleware will need to be installed in settings middleware



class LoginCheckMiddleWare(MiddlewareMixin):
    
    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "student_management_app.HodViews":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                if modulename == "student_management_app.StaffViews":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("staff_home"))
            elif user.user_type == "3":
                if modulename == "student_management_app.StudentViews":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("student_home"))
            else:
                return HttpResponseRedirect(reverse("show_login"))
            
        else:
            if request.path == reverse("show_login") or request.path == reverse("do_login"):
                pass
            else:
                return HttpResponseRedirect(reverse("show_login"))