export ORACLE_HOME=/opt/oracle/instantclient_11_2
sudo ldconfig
export LD_LIBRARY_PATH="$ORACLE_HOME"
sudo ldconfig
export PATH="$ORACLE_HOME:$PATH"
sudo ldconfig

