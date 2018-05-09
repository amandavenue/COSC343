grep -q -F 'export PATH=/opt/anaconda/bin:$PATH' ~/.bashrc || echo 'export PATH=/opt/anaconda/bin:$PATH' >> ~/.bashrc
grep -q -F 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/anaconda/lib' ~/.bashrc || echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/anaconda/lib' >> ~/.bashrc
echo "Updated the PATH for anaconda environment."
mkdir -p ~/.matplotlib
touch ~/.matplotlib/matplotlibrc
grep -q -F 'backend: TkAgg' ~/.matplotlib/matplotlibrc || echo 'backend: TkAgg' >> ~/.matplotlib/matplotlibrc
echo "Configured matplotlib for TkAgg backend."
echo "The environment is ready for COSC343."
source ~/.bashrc


