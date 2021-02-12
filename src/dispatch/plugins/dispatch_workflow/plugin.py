"""
.. module: dispatch.plugins.dispatch_workflow.plugin
    :platform: Unix
    :copyright: (c) 2019 by Netflix Inc., see AUTHORS for more
    :license: Apache, see LICENSE for more details.
"""
from jinja2 import Template
from typing import Any

from dispatch.decorators import apply, counter, timer
from dispatch.plugins import dispatch_workflow as workflow_plugin
from dispatch.plugins.bases import WorkflowPlugin

from .config import (
    CAMUNDA_API_URL,
)


class WorkflowPlugin(WorkflowPlugin):
    title = "Workflow Plugin - Workflow Management"
    slug = "workflow"
    description = "Creates WorkflowPlugin"
    

    author = "Nokia-IESP"
    author_url = "https://nokiaiesp-dev.dyn.nesc.nokia.net/iesp/"

    _schema = None

    def create(self, items, **kwargs):   
        return "Conversation Created"
    def add(self, items, **kwargs):
        return "User Added"
    def send(self, items, **kwargs):
        return "Message sent"
    
