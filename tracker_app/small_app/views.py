@login_required
def profileDisplay(request):
    user_detail = UserDetail.objects.get(user_id=request.user.id)
    return render(request, 'profiledisplay.html', {'user_detail': user_detail})