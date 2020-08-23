# -*- coding: utf-8 -*-
import sys
import shlex
import subprocess


def get_nmap_path() -> str:
    """Returns namp path"""
    _cmd = "which nmap"
    _args = shlex.split(_cmd)
    _sub_proc = subprocess.Popen(_args, stdout=subprocess.PIPE)

    try:
        _outputs, _errors = _sub_proc.communicate(timeout=10)
    except Exception as e:
        print(f'[ERROR]: {e}')
        _sub_proc.kill()
    else:
        return _outputs.decode('utf8').strip()


def get_nmap_version(_nmap_path: str) -> str:
    """Returns nmap version"""
    _cmd = _nmap_path + ' --version'

    _args = shlex.split(_cmd)
    _sub_proc = subprocess.Popen(_args, stdout=subprocess.PIPE)

    try:
        _outputs, _errors = _sub_proc.communicate(timeout=10)
    except Exception as e:
        print(f'[ERROR]: {e}')
        _sub_proc.kill()
    else:
        return _outputs.decode('utf8').strip()


if __name__ == '__main__':
    nmap_path = get_nmap_path()
    nmap_version = get_nmap_version(nmap_path)
    print(f'{nmap_path}, {nmap_version}')