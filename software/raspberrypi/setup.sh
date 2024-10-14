python3 -m venv ./.venv
source ./.venv/bin/activate

# Note that requirements.txt currently contains all the necessary
# modules to train the models. We need to make a simpler version just 
# for running the model. it is nearly a GB at the moment.
pip3 install -r requirements.txt

