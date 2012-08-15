# Copyright 2012 OpenStack LLC.
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

from sqlalchemy import Integer, Column, MetaData, Table

from nova.openstack.common import log as logging

LOG = logging.getLogger(__name__)


def upgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine

    instance_types = Table('instance_types', meta, autoload=True)
    disk_qos = Column('disk_qos', Integer())

    instance_types.create_column(disk_qos)
    instance_types.update().values(disk_qos=0).execute()


def downgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine

    instance_types = Table('instance_types', meta, autoload=True)
    disk_qos = Column('disk_qos', Integer())

    instance_types.drop_column(disk_qos)
