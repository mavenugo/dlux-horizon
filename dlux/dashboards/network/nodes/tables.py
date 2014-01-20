# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Author: Endre Karlson <endre.karlson@hp.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from django.utils.translation import ugettext_lazy as _

from horizon import tables


class NodesTable(tables.DataTable):
    id = tables.Column('id', verbose_name='Identifier')
    type = tables.Column('type')
    mac_address = tables.Column(
        lambda i: i.properties['macAddress']['value'],
        verbose_name='Mac Address')

    class Meta:
        name = 'nodes'
        verbose_name = _('Nodes',)
