# -*- coding: utf-8 -*-
# Import system modules
import os
import re
import xml
import shlex
import argparse
import subprocess
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import ParseError
# Import local package modules
from utils import get_nmap_path, get_nmap_version
from exceptions import PmapNotInstalledError, PmapXMLParserError
from pmapparser import PmapParser


class Pmap(object):
    """This pmap class allows users to use the command line nmap from within python
    by calling Pmap.Pmap()
    """
    def __init__(self):
        """Object initialization"""
        self.nmap_tool = get_nmap_path()
        self.default_args = ' -oX - '
        self.target = ''
        self.port_range = '1-1024'
        self.raw_output = ''

    def default_command(self):
        """The default nmap command, this is where you add default params
        Note self.default_args is set to '-oX -', which output as xml format
        """
        return self.nmap_tool + self.default_args

    def get_nmap_version(self):
        """Return nmap build version"""
        nmap_version = get_nmap_version(self.nmap_tool)
        return nmap_version

    def scan_ip(self, ip):
        scan_command = self.default_command() + ip
        scan_shlex = shlex.split(scan_command)
        output = self.run_command(scan_shlex)
        xml_root = self.get_xml_et(output)
        return xml_root

    def run_command(self, cmd):
        """Run the given nmap command"""
        if os.path.exists(self.nmap_tool):
            sub_proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            try:
                output, errors = sub_proc.communicate()
            except Exception as e:
                sub_proc.kill()
            else:
                return output.decode('utf8').strip()
        else:
            raise NmapNotInstalledError()

    def get_xml_et(self, output):
        """Return xml ET"""
        try:
            self.raw_output = output
            return ET.fromstring(output)
        except ParseError:
            raise NmapXMLParserError()


if __name__ == '__main__':
    pmap = Pmap()
    output = pmap.scan_ip('3.12.31.55')
    print(output)
    # parser = PmapParser(output)
    # print(parser.parse_pmap_ip_scan(output))
