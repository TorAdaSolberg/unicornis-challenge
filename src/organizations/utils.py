from .models import Organization

def UserOrgs(request):
    current_user = request.user
    q_user_orgs= Organization.objects.filter(members=current_user).values()
    user_orgs = []
    for organizations in q_user_orgs:
        user_orgs.append(organizations)
    print(user_orgs)
    return user_orgs
