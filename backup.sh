#!/bin/sh
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
find . -name '.DS_Store' -type f -ls -delete
mkdir -p bp bp/simulater/yolov7 bp/simulater/data
mkdir -p bp/JetsonNano/setup bp/JetsonNano/info bp/JetsonNano/Controller/utils bp/JetsonNano/Controller/pwms/samples

cp *.py *.sh bp/
cp simulater/*.py simulater/*.txt bp/simulater/
cp simulater/yolov7/*.py bp/simulater/yolov7/
cp simulater/data/*.onnx bp/simulater/data/

cp JetsonNano/*.py JetsonNano/*.txt bp/JetsonNano/
cp JetsonNano/setup/* bp/JetsonNano/setup/
cp JetsonNano/info/*jpg bp/JetsonNano/info/
cp JetsonNano/Controller/*.py bp/JetsonNano/Controller/
cp JetsonNano/Controller/pwms/*.py bp/JetsonNano/Controller/pwms/
cp JetsonNano/Controller/pwms/samples/*.py bp/JetsonNano/Controller/pwms/samples/
cp JetsonNano/Controller/utils/*.py JetsonNano/Controller/utils/*.onnx JetsonNano/Controller/utils/*.yaml bp/JetsonNano/Controller/utils/
