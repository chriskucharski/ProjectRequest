# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Attachments(models.Model):
    #id = models.IntegerField(primary_key=True)
    container_id = models.IntegerField()
    container_type = models.CharField(max_length=90)
    filename = models.CharField(max_length=765)
    disk_filename = models.CharField(max_length=765)
    filesize = models.IntegerField()
    content_type = models.CharField(max_length=765, blank=True)
    digest = models.CharField(max_length=120)
    downloads = models.IntegerField()
    author_id = models.IntegerField()
    created_on = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'attachments'

class AuthSources(models.Model):
    #id = models.IntegerField()
    type = models.CharField(max_length=90)
    name = models.CharField(max_length=180)
    host = models.CharField(max_length=180, blank=True)
    port = models.IntegerField(null=True, blank=True)
    account = models.CharField(max_length=765, blank=True)
    account_password = models.CharField(max_length=180, blank=True)
    base_dn = models.CharField(max_length=765, blank=True)
    attr_login = models.CharField(max_length=90, blank=True)
    attr_firstname = models.CharField(max_length=90, blank=True)
    attr_lastname = models.CharField(max_length=90, blank=True)
    attr_mail = models.CharField(max_length=90, blank=True)
    onthefly_register = models.IntegerField()
    tls = models.IntegerField()
    class Meta:
        db_table = u'auth_sources'

class Boards(models.Model):
    #id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=765, blank=True)
    position = models.IntegerField(null=True, blank=True)
    topics_count = models.IntegerField()
    messages_count = models.IntegerField()
    last_message_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'boards'

class Changes(models.Model):
    #id = models.IntegerField(primary_key=True)
    changeset_id = models.IntegerField()
    action = models.CharField(max_length=3)
    path = models.TextField()
    from_path = models.TextField(blank=True)
    from_revision = models.CharField(max_length=765, blank=True)
    revision = models.CharField(max_length=765, blank=True)
    branch = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'changes'

class ChangesetParents(models.Model):
    changeset_id = models.IntegerField()
    parent_id = models.IntegerField()
    class Meta:
        db_table = u'changeset_parents'

class Changesets(models.Model):
    #id = models.IntegerField(primary_key=True)
    repository_id = models.IntegerField()
    #revision = models.CharField(unique=True, max_length=765)
    revision = models.CharField(unique=True, max_length=255)
    committer = models.CharField(max_length=765, blank=True)
    committed_on = models.DateTimeField()
    comments = models.TextField(blank=True)
    commit_date = models.DateField(null=True, blank=True)
    scmid = models.CharField(max_length=765, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'changesets'

class ChangesetsIssues(models.Model):
    changeset_id = models.IntegerField(unique=True)
    issue_id = models.IntegerField(unique=True)
    class Meta:
        db_table = u'changesets_issues'

class ChartDoneRatios(models.Model):
    #id = models.IntegerField(primary_key=True)
    day = models.IntegerField()
    week = models.IntegerField()
    month = models.IntegerField()
    project_id = models.IntegerField()
    issue_id = models.IntegerField()
    done_ratio = models.IntegerField()
    class Meta:
        db_table = u'chart_done_ratios'

class ChartIssueStatuses(models.Model):
    #id = models.IntegerField(primary_key=True)
    day = models.IntegerField()
    week = models.IntegerField()
    month = models.IntegerField()
    project_id = models.IntegerField()
    issue_id = models.IntegerField()
    status_id = models.IntegerField()
    class Meta:
        db_table = u'chart_issue_statuses'

class ChartSavedConditions(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    project_id = models.IntegerField(null=True, blank=True)
    conditions = models.CharField(max_length=765)
    chart = models.CharField(max_length=765)
    class Meta:
        db_table = u'chart_saved_conditions'

class ChartTimeEntries(models.Model):
    #id = models.IntegerField(primary_key=True)
    day = models.IntegerField()
    week = models.IntegerField()
    month = models.IntegerField()
    logged_hours = models.FloatField()
    entries = models.IntegerField()
    user_id = models.IntegerField()
    issue_id = models.IntegerField(null=True, blank=True)
    activity_id = models.IntegerField(null=True, blank=True)
    project_id = models.IntegerField()
    class Meta:
        db_table = u'chart_time_entries'

class Comments(models.Model):
    #id = models.IntegerField(primary_key=True)
    commented_type = models.CharField(max_length=90)
    commented_id = models.IntegerField()
    author_id = models.IntegerField()
    comments = models.TextField(blank=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    class Meta:
        db_table = u'comments'

class CustomFields(models.Model):
    #id = models.IntegerField()
    type = models.CharField(max_length=90)
    name = models.CharField(max_length=90)
    field_format = models.CharField(max_length=90)
    possible_values = models.TextField(blank=True)
    regexp = models.CharField(max_length=765, blank=True)
    min_length = models.IntegerField()
    max_length = models.IntegerField()
    is_required = models.IntegerField()
    is_for_all = models.IntegerField()
    is_filter = models.IntegerField()
    position = models.IntegerField(null=True, blank=True)
    searchable = models.IntegerField(null=True, blank=True)
    default_value = models.TextField(blank=True)
    editable = models.IntegerField(null=True, blank=True)
    visible = models.IntegerField()
    class Meta:
        db_table = u'custom_fields'

class CustomFieldsProjects(models.Model):
    custom_field_id = models.IntegerField()
    project_id = models.IntegerField()
    class Meta:
        db_table = u'custom_fields_projects'

class CustomFieldsTrackers(models.Model):
    custom_field_id = models.IntegerField()
    tracker_id = models.IntegerField()
    class Meta:
        db_table = u'custom_fields_trackers'

class CustomValues(models.Model):
    #id = models.IntegerField(primary_key=True)
    customized_type = models.CharField(max_length=90)
    customized_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    value = models.TextField(blank=True)
    class Meta:
        db_table = u'custom_values'

class Documents(models.Model):
    #id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    category_id = models.IntegerField()
    title = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'documents'

class EnabledModules(models.Model):
    #id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=765)
    class Meta:
        db_table = u'enabled_modules'

class Enumerations(models.Model):
    #id = models.IntegerField()
    name = models.CharField(max_length=90)
    position = models.IntegerField(null=True, blank=True)
    is_default = models.IntegerField()
    type = models.CharField(max_length=765, blank=True)
    active = models.IntegerField()
    project_id = models.IntegerField(null=True, blank=True)
    parent_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'enumerations'

class GroupsUsers(models.Model):
    group_id = models.IntegerField(unique=True)
    user_id = models.IntegerField(unique=True)
    class Meta:
        db_table = u'groups_users'

class IssueCategories(models.Model):
    #id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    name = models.CharField(max_length=90)
    assigned_to_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'issue_categories'

class IssueRelations(models.Model):
    #id = models.IntegerField(primary_key=True)
    issue_from_id = models.IntegerField()
    issue_to_id = models.IntegerField()
    relation_type = models.CharField(max_length=765)
    delay = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'issue_relations'

class IssueStatuses(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=90)
    is_closed = models.IntegerField()
    is_default = models.IntegerField()
    position = models.IntegerField(null=True, blank=True)
    default_done_ratio = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'issue_statuses'

class Issues(models.Model):
    #id = models.IntegerField(primary_key=True)
    tracker_id = models.IntegerField()
    project_id = models.IntegerField()
    subject = models.CharField(max_length=765)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    category_id = models.IntegerField(null=True, blank=True)
    status_id = models.IntegerField()
    assigned_to_id = models.IntegerField(null=True, blank=True)
    priority_id = models.IntegerField()
    fixed_version_id = models.IntegerField(null=True, blank=True)
    author_id = models.IntegerField()
    lock_version = models.IntegerField()
    created_on = models.DateTimeField(null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    done_ratio = models.IntegerField()
    estimated_hours = models.FloatField(null=True, blank=True)
    parent_id = models.IntegerField(null=True, blank=True)
    root_id = models.IntegerField(null=True, blank=True)
    lft = models.IntegerField(null=True, blank=True)
    rgt = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'issues'

class JournalDetails(models.Model):
    #id = models.IntegerField(primary_key=True)
    journal_id = models.IntegerField()
    property = models.CharField(max_length=90)
    prop_key = models.CharField(max_length=90)
    old_value = models.CharField(max_length=765, blank=True)
    value = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'journal_details'

class Journals(models.Model):
    #id = models.IntegerField(primary_key=True)
    journalized_id = models.IntegerField()
    journalized_type = models.CharField(max_length=90)
    user_id = models.IntegerField()
    notes = models.TextField(blank=True)
    created_on = models.DateTimeField()
    class Meta:
        db_table = u'journals'

class MemberRoles(models.Model):
    #id = models.IntegerField(primary_key=True)
    member_id = models.IntegerField()
    role_id = models.IntegerField()
    inherited_from = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'member_roles'

class Members(models.Model):
    #id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    project_id = models.IntegerField()
    created_on = models.DateTimeField(null=True, blank=True)
    mail_notification = models.IntegerField()
    class Meta:
        db_table = u'members'

class Messages(models.Model):
    #id = models.IntegerField(primary_key=True)
    board_id = models.IntegerField()
    parent_id = models.IntegerField(null=True, blank=True)
    subject = models.CharField(max_length=765)
    content = models.TextField(blank=True)
    author_id = models.IntegerField(null=True, blank=True)
    replies_count = models.IntegerField()
    last_reply_id = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    locked = models.IntegerField(null=True, blank=True)
    sticky = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'messages'

class News(models.Model):
    #id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=180)
    summary = models.CharField(max_length=765, blank=True)
    description = models.TextField(blank=True)
    author_id = models.IntegerField()
    created_on = models.DateTimeField(null=True, blank=True)
    comments_count = models.IntegerField()
    class Meta:
        db_table = u'news'

class OpenIdAuthenticationAssociations(models.Model):
    #id = models.IntegerField(primary_key=True)
    issued = models.IntegerField(null=True, blank=True)
    lifetime = models.IntegerField(null=True, blank=True)
    handle = models.CharField(max_length=765, blank=True)
    assoc_type = models.CharField(max_length=765, blank=True)
    server_url = models.TextField(blank=True)
    secret = models.TextField(blank=True)
    class Meta:
        db_table = u'open_id_authentication_associations'

class OpenIdAuthenticationNonces(models.Model):
    #id = models.IntegerField(primary_key=True)
    timestamp = models.IntegerField()
    server_url = models.CharField(max_length=765, blank=True)
    salt = models.CharField(max_length=765)
    class Meta:
        db_table = u'open_id_authentication_nonces'

class Projects(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.TextField(blank=True)
    homepage = models.CharField(max_length=765, blank=True)
    is_public = models.IntegerField()
    parent_id = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    identifier = models.CharField(max_length=765, blank=True)
    status = models.IntegerField()
    lft = models.IntegerField(null=True, blank=True)
    rgt = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'projects'

class ProjectsTrackers(models.Model):
    project_id = models.IntegerField()
    tracker_id = models.IntegerField(unique=True)
    class Meta:
        db_table = u'projects_trackers'

class Queries(models.Model):
    #id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=765)
    filters = models.TextField(blank=True)
    user_id = models.IntegerField()
    is_public = models.IntegerField()
    column_names = models.TextField(blank=True)
    sort_criteria = models.TextField(blank=True)
    group_by = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'queries'

class Repositories(models.Model):
    #id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    url = models.CharField(max_length=765)
    login = models.CharField(max_length=180, blank=True)
    password = models.CharField(max_length=180, blank=True)
    root_url = models.CharField(max_length=765, blank=True)
    type = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'repositories'

class Roles(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=90)
    position = models.IntegerField(null=True, blank=True)
    assignable = models.IntegerField(null=True, blank=True)
    builtin = models.IntegerField()
    permissions = models.TextField(blank=True)
    class Meta:
        db_table = u'roles'

class SchemaMigrations(models.Model):
    #version = models.CharField(unique=True, max_length=765)
    version = models.CharField(unique=True, max_length=255)
    class Meta:
        db_table = u'schema_migrations'

class Settings(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    value = models.TextField(blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'settings'

class TimeEntries(models.Model):
    #id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    user_id = models.IntegerField()
    issue_id = models.IntegerField(null=True, blank=True)
    hours = models.FloatField()
    comments = models.CharField(max_length=765, blank=True)
    activity_id = models.IntegerField()
    spent_on = models.DateField()
    tyear = models.IntegerField()
    tmonth = models.IntegerField()
    tweek = models.IntegerField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    class Meta:
        db_table = u'time_entries'

class Tokens(models.Model):
    #id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    action = models.CharField(max_length=90)
    value = models.CharField(max_length=120)
    created_on = models.DateTimeField()
    class Meta:
        db_table = u'tokens'

class Trackers(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=90)
    is_in_chlog = models.IntegerField()
    position = models.IntegerField(null=True, blank=True)
    is_in_roadmap = models.IntegerField()
    class Meta:
        db_table = u'trackers'

class UserPreferences(models.Model):
    #id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    others = models.TextField(blank=True)
    hide_mail = models.IntegerField(null=True, blank=True)
    time_zone = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'user_preferences'

class Users(models.Model):
    #id = models.IntegerField()
    login = models.CharField(max_length=90)
    hashed_password = models.CharField(max_length=120)
    firstname = models.CharField(max_length=90)
    lastname = models.CharField(max_length=90)
    mail = models.CharField(max_length=180)
    admin = models.IntegerField()
    status = models.IntegerField()
    last_login_on = models.DateTimeField(null=True, blank=True)
    language = models.CharField(max_length=15, blank=True)
    auth_source_id = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    type = models.CharField(max_length=765, blank=True)
    identity_url = models.CharField(max_length=765, blank=True)
    mail_notification = models.CharField(max_length=765)
    class Meta:
        db_table = u'users'

class Versions(models.Model):
    #id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=765, blank=True)
    effective_date = models.DateField(null=True, blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    wiki_page_title = models.CharField(max_length=765, blank=True)
    status = models.CharField(max_length=765, blank=True)
    sharing = models.CharField(max_length=765)
    class Meta:
        db_table = u'versions'

class Watchers(models.Model):
    #id = models.IntegerField(primary_key=True)
    watchable_type = models.CharField(max_length=765)
    watchable_id = models.IntegerField()
    user_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'watchers'

class WikiContentVersions(models.Model):
    #id = models.IntegerField(primary_key=True)
    wiki_content_id = models.IntegerField()
    page_id = models.IntegerField()
    author_id = models.IntegerField(null=True, blank=True)
    data = models.TextField(blank=True)
    compression = models.CharField(max_length=18, blank=True)
    comments = models.CharField(max_length=765, blank=True)
    updated_on = models.DateTimeField()
    version = models.IntegerField()
    class Meta:
        db_table = u'wiki_content_versions'

class WikiContents(models.Model):
    #id = models.IntegerField(primary_key=True)
    page_id = models.IntegerField()
    author_id = models.IntegerField(null=True, blank=True)
    text = models.TextField(blank=True)
    comments = models.CharField(max_length=765, blank=True)
    updated_on = models.DateTimeField()
    version = models.IntegerField()
    class Meta:
        db_table = u'wiki_contents'

class WikiPages(models.Model):
    #id = models.IntegerField(primary_key=True)
    wiki_id = models.IntegerField()
    title = models.CharField(max_length=765)
    created_on = models.DateTimeField()
    protected = models.IntegerField()
    parent_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'wiki_pages'

class WikiRedirects(models.Model):
    #id = models.IntegerField(primary_key=True)
    wiki_id = models.IntegerField()
    title = models.CharField(max_length=765, blank=True)
    redirects_to = models.CharField(max_length=765, blank=True)
    created_on = models.DateTimeField()
    class Meta:
        db_table = u'wiki_redirects'

class Wikis(models.Model):
    #id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    start_page = models.CharField(max_length=765)
    status = models.IntegerField()
    class Meta:
        db_table = u'wikis'

class Workflows(models.Model):
    #id = models.IntegerField(primary_key=True)
    tracker_id = models.IntegerField()
    old_status_id = models.IntegerField()
    new_status_id = models.IntegerField()
    role_id = models.IntegerField()
    class Meta:
        db_table = u'workflows'

