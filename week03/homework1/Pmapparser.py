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
    def __init__(self, xml_et=''):
        self.xml_et = xml_et
        self.xml_root = None

    def parse_pmap_ip_scan(self, _xml_root):
        """Parse single IP scan result"""
        try:
            _output, _host = {}, ''
            if not _xml_root: return _output
            self.xml_root = _xml_root
            _host = self.xml_root.find("host")
            # If host is not up
            if not _host: return _output
            # Get host status
            if _host.find("status") is not None:
                _output['state'] = _host.find("status").attrib['state']
            # Get host IP address
            if _host.find("address") is not None:
                _output['address'] = _host.find("address").attrib['addr']
            # Get open ports
            _output['ports'] = []
            _ports = _host.find("ports")
            for _port in _ports:
                if _port.tag == 'port':
                    _temp = {}
                    _temp['protocol'] = _port.attrib['protocol']
                    _temp['port'] = _port.attrib['portid']
                    _output['ports'].append(_temp)
            return _output
        except Exception as e:
            print(f'[ERROR] {e}')

    def parse_pmap_ping(self, _xml_root):
        """Parse single ping scan result"""
        try:
            _output, _host = {}, ''
            if not _xml_root: return _output
            self.xml_root = _xml_root
            _host = self.xml_root.find("host")
            # If host is not up
            if not _host: return _output
            # Get host status
            if _host.find('status') is not None:
                _output['state'] = _host.find('status').attrib['state']
            # Get host IP address
            if _host.find("address") is not None:
                _output['address'] = _host.find('address').attrib['addr']
            _run_stats = self.xml_root.find('runstats')
            if _run_stats.find('finished') is not None:
                _output['elapsed'] = _run_stats.find('finished').attrib['elapsed']
            return _output
        except Exception as e:
            print(f'[ERROR] {e}')