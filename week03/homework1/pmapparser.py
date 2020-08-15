# -*- coding: utf-8 -*-
import io
import os
import re
import sys
import shlex
import subprocess
from xml.etree import ElementTree as ET


class PmapParser(object):
    """pmap output XML parser"""
    def __init__(self, xml_et):
        self.xml_et = xml_et
        self.xml_root = None

    def parse_pmap_ip_scan(self, xml_root):
        """Parse single IP scan result"""
        attrib = {}
        try:
            if not xml_root:
                return ''
            self.xml_root = xml_root
            host = xml_root.find("host")

            if host.find("address") is not None:
                attrib[host.find("address").attrib] = host.find("address").attrib.get(attr)
            return attrib
        except Exception as e:
            print(f'No IP address find')
