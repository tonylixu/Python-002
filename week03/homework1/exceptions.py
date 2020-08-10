# -*- coding: utf-8 -*-
import shlex
import subprocess
import sys
import re


class PmapNotInstalledError(Exception):
    """Exception raised when nmap is not installed"""

    def __init__(self,
                 message="Nmap is either not installed or we couldn't locate nmap path"):
        self.message = message
        super().__init__(message)


class PmapXMLParserError(Exception):
    """Exception raised when we can't parse the output"""

    def __init__(self, message="Unable to parse xml output"):
        self.message = message
        super().__init__(message)