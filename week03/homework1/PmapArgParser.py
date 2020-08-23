# -*- coding: utf-8 -*-
import re
import argparse
import multiprocessing as mp

TOTAL_CPU = mp.cpu_count()


class PmapArgParser(object):
    def __init__(self, _description=''):
        self.parser = argparse.ArgumentParser(_description)

    def parse_args(self):
        return self.parser.parse_args()

    def add_num_argument(self):
        self.parser.add_argument(
            '-n',
            type=PmapArgParser.check_n_argument,
            dest='num',
            default=1,
            help='Number of threads/processes')

    def add_mode_argument(self):
        self.parser.add_argument(
            '-m',
            choices=['thread', 'process'],
            dest='mode',
            default='thread',
            help='Mode: thread or process')

    def add_method_argument(self):
        self.parser.add_argument(
            '-f',
            choices=['ping', 'tcp'],
            dest='method',
            default='tcp',
            help='Ping or tcp test')

    def add_output_argument(self):
        self.parser.add_argument(
            '-w',
            type=str,
            dest='output',
            required=False,
            help='Output file name')

    def add_ip_argument(self):
        self.parser.add_argument(
            '-ip',
            type=PmapArgParser.check_ip_argument,
            dest='ip_range',
            required=True,
            help='Single IP or IP range in ipA-ipB format')

    def add_port_argument(self):
        self.parser.add_argument(
            '-p',
            type=PmapArgParser.check_port_argument,
            dest='port',
            required=False,
            help='Port number')

    @staticmethod
    def check_n_argument(_parallel_num):
        """Check if given parallel num is valid"""
        if not re.match(r'[1-9]+', _parallel_num):
            raise argparse.ArgumentTypeError(f'Please use only numbers!')
        if int(_parallel_num) > TOTAL_CPU:
            raise argparse.ArgumentTypeError(f'-n {_parallel_num} is larger than system CPU ({TOTAL_CPU})!')
        return int(_parallel_num)

    @staticmethod
    def check_ip_argument(_ips):
        """Check if given ip(s) is in valid format"""
        _ip_regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
        # Check if IP range format
        if '-' in _ips and _ips.count('-') == 1:
            _start_ip = _ips.split('-')[0]
            _end_ip = _ips.split('-')[1]
            if not re.search(_ip_regex, _start_ip) or not re.search(_ip_regex, _end_ip):
                raise argparse.ArgumentTypeError(f'Invalid IP address!')
        else:
            if not re.search(_ip_regex, _ips):
                raise argparse.ArgumentTypeError(f'Invalid IP address!')
        return _ips

    @staticmethod
    def check_port_argument(_port):
        """Check if given parallel num is valid"""
        if int(_port) <= 0 or int(_port) >= 65535:
            raise argparse.ArgumentTypeError(f'-p {_port} invalid port number! (1<= port <=65535)')
        return _port
