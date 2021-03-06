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

"""Global config defaults the app can override in the Config datastore model."""


DEFAULTS = {
    # bootstrap_[started|completed]: bool, Both False by default, changed to
    # True in datastore once the bootstrap process is started or completed
    # respectively.
    'bootstrap_started': False,
    'bootstrap_completed': False,

    # allow_guest_mode: bool, Whether an organization allows loaners to enable
    # guest mode.
    'allow_guest_mode': True,

    # loan_duration: int, Number of days to assign a loan by default.
    'loan_duration': 3,

    # minimum_loan_duration: int, Minimum days for which a loaner can be loaned.
    'minimum_loan_duration': 1,

    # maximum_loan_duration: int, Maximum days for which a loaner can be loaned.
    'maximum_loan_duration': 14,

    # loan_duration_email: bool, Whether email should be sent.
    'loan_duration_email': True,

    # reminder_email_throtting: bool, Whether to skip emails when a user sees a
    # Chrome app reminder.
    'reminder_email_throtting': True,

    # reminder_delay: int, Hours after which the app will send a reminder e-mail
    # for a Device it identifies as worthy of a reminder.
    'reminder_delay': 1,

    # shelf_audit: bool, Whether shelf audit should be enabled.
    'shelf_audit': True,

    # shelf_audit_email: bool, Whether email should be sent for audits.
    'shelf_audit_email': False,

    # shelf_audit_email_to: list, Users who should get the email.
    'shelf_audit_email_to': [''],

    # shelf_audit_interval: int, The number of hours to allow a shelf to remain
    # unaudited, overridable via a shelf's audit_interval_override property.
    'shelf_audit_interval': 24,

    # responsible_for_audit: list, A group that is responsible for performing an
    # audit on a shelf.
    'responsible_for_audit': ['technicians@example.com'],

    # support_contact: str, The support contact.
    'support_contact': 'File a ticket!',

    # org_unit_prefix: str, The Organizational Unit that will act as the
    # root for the Grab n Go child Org Units.
    'org_unit_prefix': '',

    # audit_interval: int, The shelf audit threshold in hours.
    'audit_interval': 24,

    # sync_roles_query_size: int, The number of users for which to query and
    # sync roles.
    'sync_roles_user_query_size': 1000,

    # anonymous_surveys: bool, Whether or not surveys are recorded anonymously.
    'anonymous_surveys': True,

    # require_surveys: bool, Whether or not the surveys are required.
    'require_surveys': False,

    # use_asset_tags: bool, True if you want to display device asset tags as
    # user-facing identifiers, False if you want to display serial numbers.
    'use_asset_tags': False,

    # img_banner_*: str, The banner images for reminder e-mails.
    'img_banner_primary': '',

    # img_button_*: str, The button images for reminder e-mails.
    'img_button_manage': '',

    # timeout_guest_mode: bool, Whether or not a deferred task should be created
    # to timeout guest mode.
    'timeout_guest_mode': True,

    # guest_mode_timeout_in_hours: int, The number of hours to allow guest mode
    # to be in use.
    'guest_mode_timeout_in_hours': 12,

    # unenroll_ou: str, The OU to move devices into as they leave the GnG
    # program, it defaults to the root ou of the organization.
    'unenroll_ou': '/',

    # return_grace_period: int, The grace period between marking a device as
    # pending return and the next heartbeat in minutes.
    'return_grace_period': 15,
}
