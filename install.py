#!/usr/bin/env python3
import os
import subprocess
import venv


THIS_DIR = os.path.abspath(os.path.dirname(__file__))

virtualenv = venv.EnvBuilder(with_pip=True)
home_dir = os.path.expanduser('~')
venv_root = os.path.join(home_dir, '.virtualenvs', 'xonsh')
virtualenv.create(venv_root)

pip_path = os.path.join(venv_root, 'bin', 'pip')

subprocess.run([pip_path,
                'install',
                'pip',
                '--upgrade',
                ])

subprocess.run([pip_path,
                'install',
                'xonsh[ptk,linux]',
                ])

bin_dir = os.path.join(home_dir, 'bin')
os.makedirs(bin_dir, exist_ok=True)

# TODO: add ~/bin/ to $PATH only if it is not already in $PATH
xonsh_path = os.path.join(venv_root, 'bin', 'xonsh')
os.symlink(xonsh_path,  os.path.join(bin_dir, 'xonsh'))
os.symlink(os.path.join(THIS_DIR, '.xonshrc'),
            os.path.join(home_dir, '.xonshrc'))

xonsh_config_dir = os.path.join(home_dir, '.config', 'xonsh')
os.makedirs(xonsh_config_dir, exist_ok=True)
os.symlink(os.path.join(THIS_DIR, 'config.json'),
            os.path.join(xonsh_config_dir, 'config.json'))

# Upgrade Script
os.symlink(os.path.join(THIS_DIR, 'upgrade_xonsh'),
            os.path.join(home_dir, 'bin', 'upgrade_xonsh'))


# Add to list of shells
subprocess.run('echo `which xonsh` | sudo tee -a /etc/shells', shell=True)
