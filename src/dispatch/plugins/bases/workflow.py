"""
.. module: dispatch.plugins.bases.workflow
    :platform: Unix
    :copyright: (c) 2019 by Netflix Inc., see AUTHORS for more
    :license: Apache, see LICENSE for more details.
.. moduleauthor:: Kevin Glisson <kglisson@netflix.com>
"""
from dispatch.plugins.base import Plugin
from dispatch.models import PluginOptionModel


class WorkflowPlugin(Plugin):
    type = "workflow"
    _schema = PluginOptionModel
    

    
    def create(self, items, **kwargs):
        return "Conversation Created"
    def add(self, items, **kwargs):
        return "User Added"
    def send(self, items, **kwargs):
        return "Message sent"



