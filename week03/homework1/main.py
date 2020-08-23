# -*- coding: utf-8 -*-
import json
import argparse
import ipaddress
from concurrent.futures import ThreadPoolExecutor, as_completed
# Import local package modules
from Pmap import Pmap
from Pmapparser import PmapParser
from PmapArgParser import PmapArgParser


def parse_arguments() -> PmapParser:
    """Add command line arguments"""
    _arg_parser = PmapArgParser('Pmap argument parser')
    _arg_parser.add_num_argument()
    _arg_parser.add_mode_argument()
    _arg_parser.add_method_argument()
    _arg_parser.add_ip_argument()
    _arg_parser.add_port_argument()
    _arg_parser.add_output_argument()
    _args = {}
    try:
        _args = _arg_parser.parse_args()
    except argparse.ArgumentTypeError as e:
        sys.exit(f'[ERROR]: Failed to parse command line argument')
    return _args


def scan_ip(_ip):
    """Sacn port 1-1024 for given IP"""
    pmap = Pmap()
    # Use default nmap args
    xml_parser = PmapParser()
    result = xml_parser.parse_pmap_ip_scan(pmap.scan_ip_xml(_ip))
    return result if result else {_ip: 'down'}


def ping_ip(_ip):
    """Ping single ip"""
    pmap = Pmap()
    # Use default nmap args
    xml_parser = PmapParser()
    result = xml_parser.parse_pmap_ping(pmap.ping_ip_xml(_ip))
    return result if result else {_ip: 'down'}


def parse_ip_range(_ip_str):
    """Parse ip range str to start ip and end ip"""
    if '-' in ip_str:
        _start_ip, _end_ip = ip_str.split('-')[0], ip_str.split('-')[1]
    else:
        _start_ip = _end_ip = ip_str
    return _start_ip, _end_ip


if __name__ == '__main__':
    # Retrieve command line argument
    args = parse_arguments()
    num, mode, method, ip_str = args.num, args.mode, args.method, args.ip_range
    port = args.port if args.port else 0
    output_file = args.output if args.output else ''

    # Parse IP range
    start_ip, end_ip = parse_ip_range(ip_str)
    start_ip = int(ipaddress.IPv4Address(start_ip))
    end_ip = int(ipaddress.IPv4Address(end_ip))
    print(f'Running with argument -n {num}, -f {method}, -ip {ip_str}, -w {output_file}')

    # Execute ping or tcp command
    task_type, tasks, results = method, [], []
    with ThreadPoolExecutor(max_workers=num) as executor:
        if task_type == 'tcp':
            for int_ip in range(start_ip, end_ip + 1):
                tasks.append(executor.submit(scan_ip, str(ipaddress.IPv4Address(int_ip))))
        elif task_type == 'ping':
            for int_ip in range(start_ip, end_ip + 1):
                tasks.append(executor.submit(ping_ip, str(ipaddress.IPv4Address(int_ip))))

        for future in as_completed(tasks):
            if task_type == 'tcp' and future.result():
                if future.result(): results.append([future.result()])
            if task_type == 'ping' and future.result():
                if future.result(): results.append([future.result()])

        # Output to console anyway
        print(results)
        # Write into file
        if output_file:
            with open(output_file, 'w') as json_writer:
                json.dump(results, json_writer)
