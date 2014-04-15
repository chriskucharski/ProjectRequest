from django.shortcuts import *
from django.conf import settings
from django.db import transaction
import getpass

def ldapquery(username):
    import ldap
        
    l = ldap.open(settings.AD_DNS_NAME)
    l.protocol_version = ldap.VERSION3
    l.set_option(ldap.OPT_REFERRALS, 0)
    output =l.simple_bind(settings.AD_APP_USER, settings.AD_APP_PASS)
    print "Connection output: %s"  %(output)
    result = l.search_ext_s(settings.AD_SEARCH_DN,ldap.SCOPE_SUBTREE, 
           "sAMAccountName=%s" % username,settings.AD_SEARCH_FIELDS)[0][1]
    l.unbind()
    
    if result.has_key('cn'):
        commonname = result['cn'][0]
        print "Common name: %s" %(commonname)
    else:
        commonname = None
        print "No common name"
    
    if result.has_key('department'):
        department = result['department'][0]
        print "Department: %s" %(department)
    else:
        department = None
        print "No department"
        
    return {'commonname':commonname, 'department':department}

@transaction.commit_on_success
def showIndex(request):
    from ProjectRequest.projectrequest import forms
    from models import Users
    from models import Issues
    from models import Trackers
    from models import Projects
    from models import IssueStatuses
    from models import IssueCategories
    from models import Enumerations
    from models import CustomValues
    from models import CustomFields
    import datetime
    
    if request.method == 'POST': # If the form has been submitted...
        form = forms.ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            requester = form.cleaned_data['requester']
            department = form.cleaned_data['department']
            subject = form.cleaned_data['subject']
            business_sponsor = form.cleaned_data['business_sponsor']
            requested_delivery_date = form.cleaned_data['requested_delivery_date']
            system = form.cleaned_data['system']
            description = "%s \n\n" \
                        "Business Sponsor: %s \n" \
                        "Department: %s \n" \
                        "Requested Delivery Date: %s \n" \
                        "System: %s" % (form.cleaned_data['description'], \
                                        business_sponsor, \
                                        department, \
                                        requested_delivery_date, \
                                        system)
            print "Description: ", description
            
            authors = Users.objects.get(login='IT_SalesCommsSystemsRequests') #'IT_SalesCommsSystemsRequests'
            projects = Projects.objects.get(name='Discretionary Requests') #'Client Systems Technology Projects'
            trackers = Trackers.objects.get(name='IT Project') #'IT Project'
            statuses = IssueStatuses.objects.get(name='New') #'New'
            categories = IssueCategories.objects.get(name='New Request') #'New Request'
            priorities = Enumerations.objects.get(type='IssuePriority', name='3 - Normal')
            print "Author Id:", authors.id
            print "Project Id:", projects.id
            print "Tracker Id:", trackers.id
            print "Status Id:", statuses.id
            print "Category Id:", categories.id
            print "Priority Id:", priorities.id
            
            issue = Issues.objects.create(tracker_id = trackers.id
                                  , project_id = projects.id
                                  , subject = subject
                                  , description = description
                                  , status_id = statuses.id
                                  , assigned_to_id = authors.id
                                  , priority_id = priorities.id
                                  , author_id = authors.id
                                  , lock_version = 0
                                  , done_ratio = 0
                                  , created_on = datetime.datetime.now()
                                  , updated_on = datetime.datetime.now()
                                  , lft = 1
                                  , rgt = 2)
            print "Issue Id:", issue.id
            
            custom_fields = CustomFields.objects.get(name='Requested By')
            custom_requester = CustomValues.objects.create(customized_type = 'Issue'
                                                           , customized_id = issue.id
                                                           , custom_field_id = custom_fields.id
                                                           , value = requester)
            print "Custom field Id:", custom_requester.id
            return HttpResponseRedirect('thanks/') # Redirect after POST
    else:
        #userinfo = ldapquery(getpass.getuser())
        #userinfo = ldapquery('ckucharski')
        #form = forms.ContactForm(initial={'requester': userinfo['commonname'], 'department': userinfo['department']}) # An unbound form
        form = forms.ContactForm(initial={'requester':'Chris Kucharski', 'department':'Technology'})
        context = RequestContext(request, {'form':form})
    return render_to_response('projectrequest/index.html', context)

def showThanks(request):
    return render_to_response('projectrequest/thanks.html')
