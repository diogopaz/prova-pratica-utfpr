"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "prova_pratica"

_ = MessageFactory("prova_pratica")

logger = logging.getLogger("prova_pratica")
