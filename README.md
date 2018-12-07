# Log
Login de inicialização doinux

# Instalacao do script

apt update

apt install git python

git clone https://github.com/Tioolive/Log

cd Log

cat log.py > $PREFIX/bin/log

printf "log" >> $PREFIX/etc/bash.bashrc

chmod +x $PREFIX/bin/log

# O usuario padrao e
root
# A senha padrao e
toor

# para trocar o usuario
sed -i "s/root/usuario/g" > $PREFIX/bin/log.py
# para trocar a senha
sed -i "s/toor/senha/g" > $PREFIX/bin/log.py

exemplo:

	sed -i "s/root/olive/g" > $PREFIX/bin/log.py
	sed -i "s/toor/evilo/g" > $PREFIX/bin/log py





Copyring oliveObom
