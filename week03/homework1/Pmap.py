# -*- coding: utf-8 -*-
# Import system modules
import os
import re
import xml
import shlex
import subprocess
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import ParseError
# Import local package modules
from utils import get_nmap_path, get_nmap_version
from exceptions import PmapNotInstalledError, PmapXMLParserError


class Pmap():
    """This pmap class allows users to use the command line nmap from within python
    by calling Pmap.Pmap()
    """
    def __init__(self):
        """Object initialization"""
        self.nmap_tool = get_nmap_path()
        self.xml_args = ' -oX - '
        self.ping_args = ' -sP -R '
        self.target = ''
        self.port_range = '1-1024'
        self.raw_output = ''

    def default_command(self):
        """The default nmap command, this is where you add default params
        Note self.default_args is set to '-oX -', which output as xml format
        """
        return self.nmap_tool + ' '

    def get_nmap_version(self):
        """Return nmap build version"""
        nmap_version = get_nmap_version(self.nmap_tool)
        return nmap_version

    def scan_ip(self, _ip):
        scan_command = self.default_command() + _ip
        scan_shlex = shlex.split(scan_command)
        return self.run_command(scan_shlex)

    def scan_ip_xml(self, _ip):
        scan_command = self.default_command() + self.xml_args + _ip
        scan_shlex = shlex.split(scan_command)
        output = self.run_command(scan_shlex)
        xml_root = self.get_xml_et(output)
        return xml_root

    def ping_ip(self, _ip):
        """Ping single IP with normal output"""
        _scan_command = self.default_command() + self.ping_args + _ip
        _scan_shlex = shlex.split(_scan_command)
        return self.run_command(_scan_shlex)

    def ping_ip_xml(self, _ip):
        """Ping single IP with XML output"""
        _scan_command = self.default_command() + self.ping_args + self.xml_args + _ip
        _scan_shlex = shlex.split(_scan_command)
        _output = self.run_command(_scan_shlex)
        _xml_root = self.get_xml_et(_output)
        return _xml_root

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
            raise PmapNotInstalledError()

    def get_xml_et(self, _output):
        """Return xml ET from string

        :param _output: Command output in string format
        :return XML element root
        """
        try:
            self.raw_output = _output
            return ET.fromstring(_output)
        except ParseError:
            raise PmapXMLParserError()
