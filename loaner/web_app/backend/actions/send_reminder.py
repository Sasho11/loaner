# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Action to send an e-mail reminder."""

import logging

from loaner.web_app.backend.actions import base_action
from loaner.web_app.backend.lib import send_email
from loaner.web_app.backend.models import event_models


class Error(Exception):
  """General Error class for this module."""


class SendReminderError(Error):
  """Error raised when we cannot send the requested e-mail."""


class SendReminder(base_action.BaseAction):
  """Action class to send an e-mail to a device assignee."""

  ACTION_NAME = 'send_reminder'
  FRIENDLY_NAME = 'Send reminder'

  def run(self, **kwargs):
    """Send an e-mail to the device assignee and remove reminder."""
    device = kwargs.get('device')
    if not device:
      raise SendReminderError(
          'Cannot send mail. Task did not receive a device; only kwargs: '
          '{}'.format(str(kwargs)))
    if not hasattr(device, 'next_reminder') or not device.next_reminder:
      raise SendReminderError(
          'Cannot send mail without next_reminder on device with serial '
          '{}.'.format(device.serial_number))
    reminder_event = event_models.ReminderEvent.get(device.next_reminder.level)
    if not reminder_event:
      raise SendReminderError(
          'Cannot send mail. There is no ReminderEvent entity for level '
          '{}.'.format(device.next_reminder.level))
    logging.info(
        'Sending reminder at level %d to device %s.',
        device.next_reminder.level, device.identifier)
    send_email.send_user_email(device, reminder_event.template)
    device.set_last_reminder(device.next_reminder.level)
    device.next_reminder = None
    device.put()
