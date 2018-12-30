# Log
https://raw.githubusercontent.com/Olliv3r/Log/master/LOG.png
# Login de inicialização do linux

+ Instalacao do script
 * apt update
 * apt install git python
 * git clone https://github.com/Olliv3r/Log
 * cd Log
 * cat log.py > $PREFIX/bin/log
 * printf "log" >> ~/.bashrc
 * chmod +x $PREFIX/bin/log


 
+ Usuário e senha padrão
* root
* toor

+ para trocar o usuario
* sed -i "s/root/usuario/g" $PREFIX/bin/log.py
+ para trocar a senha
* sed -i "s/toor/senha/g" $PREFIX/bin/log.py

+ exemplo:

*	sed -i "s/root/olive/g" $PREFIX/bin/log.py
*	sed -i "s/toor/evilo/g" $PREFIX/bin/log py

+ Copyring oliveObom
