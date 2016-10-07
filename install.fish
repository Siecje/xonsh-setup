#!/usr/bin/fish

python3 -m venv ~/.virtualenvs/xonsh
source ~/.virtualenvs/xonsh/bin/activate.fish
pip install xonsh[ptk,linux]
mkdir -p ~/bin/
# TODO: add ~/bin/ to $PATH only if it is not already in $PATH
ln -s ~/.virtualenvs/xonsh/bin/xonsh ~/bin/xonsh
ln -s (pwd)/.xonshrc ~/.xonshrc
mkdir -p ~/.config/xonsh/
ln -s (pwd)/config.json ~/.config/xonsh/config.json

# Upgrade Script
ln -s (pwd)/upgrade_xonsh ~/bin/

# Add to list of shells

#sudo echo '~/.virtualenvs/xonsh/bin/xonsh' >> /etc/shells
echo `which xonsh` | sudo tee -a /etc/shells
