Сборка проекта:

pip3 install virtualenv

python3 -m venv env

. ./env/bin/activate

pip3 install -r lib.txt

sudo apt install graphviz

Файл с исходным арифметическим выражением и файл, в котором будет находиться абстрактное синтаксическое дерево передаются в качестве параметров:

python3 parser.py <имя_исходного_файла>.txt <имя_выходного_файла>.png
