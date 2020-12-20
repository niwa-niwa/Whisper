import re
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
# from django.contrib.auth.validators import ASCIIUsernameValidator


@deconstructible
class CustomUsernameValidator(object):
    message = _('Invalid username')

    def __call__(self, value):
        # if not re.match(r'[^!"#$%&\'()\*\+\.,\/:;<=>?@\[\\\]^`{|}~]+', value):
        if not re.match(r'^[a-zA-Z0-9\_\-]+$', value):
            print('エラーです')
            raise ValidationError(self.message, code='invalid_username')


custom_usename_validator = [CustomUsernameValidator()]