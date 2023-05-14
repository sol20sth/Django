from accounts.form import UserChangeForm, UserCreationForm


def user_forms(request):
    if request.user.is_authenticated:
        u_change_form = UserChangeForm(instance=request.user)
    else:
        u_change_form = ""
    
    return {
        "u_create_form" : UserCreationForm,
        "u_change_form" : UserChangeForm
    }