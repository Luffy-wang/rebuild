class login_required():
    def check_permission(seff):
        return self.request.user.is_authenticated()