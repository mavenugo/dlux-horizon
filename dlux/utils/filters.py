# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 NEC Corporation All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import uuid


def get_int_or_uuid(value):
    """Check if a value is valid as UUID or an integer.

    This method is mainly used to convert floating IP id to the
    appropriate type. For floating IP id, integer is used in Nova's
    original implementation, but UUID is used in Neutron based one.
    """
    try:
        uuid.UUID(value)
        return value
    except (ValueError, AttributeError):
        return int(value)


def keys_as_id(obj, keys=['id'], joiner='%'):
    if isinstance(obj, dict):
        data = [obj[k] for k in keys]
    else:
        data = [getattr(obj, k) for k in keys]
    return joiner.join(data)
