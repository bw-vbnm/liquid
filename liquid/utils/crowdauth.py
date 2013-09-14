import crowd
import settings
from intranet.models import Member


class ActiveDirectoryGroupMembershipSSLBackend:
   supports_object_permissions = False
   supports_anonymous_user = False
   supports_inactive_user = False
   def authenticate(self,username=None,password=None):
      try:
         user = crowd.backends.CrowdBackends.authenticate(username, password)
         password = user.password
         username = user.username
         return self.get_or_create_user(username,password)
      
      except ImportError:
         pass

   def get_or_create_user(self, username, password):
      try:
         user = Member.objects.get(username=username)
      except Member.DoesNotExist:
         return None
      return user

   def get_user(self, user_id):
      try:
         return Member.objects.get(pk=user_id)
      except Member.DoesNotExist:
         return None
