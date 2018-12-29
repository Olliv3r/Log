# Log
Login de inicialização doinux

# Instalacao do script

1 apt update

2 apt install git python

3 git clone https://github.com/Olliv3r/Log

4 cd Log

5 cat log.py > $PREFIX/bin/log

6 printf "log" >> ~/.bashrc

7 chmod +x $PREFIX/bin/log


1 usuario padrao é
* root
2 A senha padrao e
* toor

1 para trocar o usuario
* sed -i "s/root/usuario/g" > $PREFIX/bin/log.py
2 para trocar a senha
* sed -i "s/toor/senha/g" > $PREFIX/bin/log.py

* exemplo:

*	sed -i "s/root/olive/g" > $PREFIX/bin/log.py
*	sed -i "s/toor/evilo/g" > $PREFIX/bin/log py
*

Copyring oliveObom
