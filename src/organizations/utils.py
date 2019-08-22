from .models import Organization


def UserOrgs(request):
    """ helper method used to extract a given users related organizations.

    It querys for a given users memberships in organizations, and extracts it as
    a list of dicts for easy parsing in templates. There really must be a better
    way of doing this like writing a custom template tag or such, but i wont make
    it a priority.

    args:
        request:
            Django WSGI request, just to get the current_user
            note: Also handy if one wants to add the list of user Organizations
            into the session at a later point
    """
    current_user = request.user
    #print(type(request)) #debugprint
    q_user_orgs= Organization.objects.filter(members=current_user).values()
    user_orgs = []
    for organizations in q_user_orgs:
        user_orgs.append(organizations)
    #print(user_orgs) #debugprint
    return user_orgs
