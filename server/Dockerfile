from ubuntu:16.10

# system specific settings
run echo 'export TERM=screen-256color' >> ~/.bashrc
run echo 'export PAGER=less' >> ~/.bashrc
run echo 'export EDITOR=vim' >> ~/.bashrc
run echo 'bind -r "\C-s"' >> ~/.bashrc
run echo 'stty -ixon' >> ~/.bashrc
run echo 'export LC_ALL=C.UTF-8' >> ~/.bashrc
run echo 'export LANG=C.UTF-8' >> ~/.bashrc

# user specific settings
copy .gitconfig /root/.gitconfig
copy .vimrc /root/.vimrc
run apt-get update
run apt-get install -y ranger
run apt-get install -y tree
run apt-get install -y cloc
run apt-get install -y git
run apt-get install -y vim
run mkdir -p /root/.vim/pack/plugins/start
run git clone https://github.com/mitsuhiko/vim-python-combined /root/.vim/pack/plugins/start/vim-python-combined
run git clone https://github.com/tomasr/molokai /root/.vim/pack/plugins/start/molokai
run git clone https://github.com/ctrlpvim/ctrlp.vim /root/.vim/pack/plugins/start/ctrlp.vim
run git clone https://github.com/airblade/vim-gitgutter /root/.vim/pack/plugins/start/vim-gitgutter
run git clone https://github.com/justinmk/vim-sneak /root/.vim/pack/plugins/start/vim-sneak
run git clone https://github.com/tpope/vim-surround /root/.vim/pack/plugins/start/vim-surround
run git clone https://github.com/nvie/vim-flake8 /root/.vim/pack/plugins/start/vim-flake8
run git clone https://github.com/mattn/emmet-vim.git /root/.vim/pack/plugins/start/emmet-vim

# app specific settings
run apt-get install -y ipython3
run apt-get install -y python3-pip
run pip3 install flake8
run pip3 install Flask
run pip3 install gunicorn
run pip3 install requests

expose 8000
