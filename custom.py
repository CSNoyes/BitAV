"""This is for easy customization of new currencies."""
import tools
import hashlib


def hash_(x):
    return hashlib.sha256(x).hexdigest()
sigDB = 'sigDB.db'
curDB = 'curDB.db'
listen_port = 8900
gui_port = 8700
version = "BitAV 0.1"
block_reward = 10 ** 5
premine = 5 * 10 ** 6
fee = 10 ** 3
num_cores = 2
# Lower limits on what the "time" tag in a block can say.
mmm = 100
# Take the median of this many of the blocks.
# How far back in history do we look when we use statistics to guess at
# the current blocktime and difficulty.
history_length = 400
# This constant is selected such that the 50 most recent blocks count for 1/2 the
# total weight.
inflection = 0.985
download_many = 500  # Max number of blocks to request from a peer at the same time.
max_download = 50000
brainwallet = 'brainDefault' # passphrase / wallet generation seed
privkey = tools.detSha(brainwallet)
pubkey = tools.privtopub(privkey)
peers = [['localhost', 8901],
         ['localhost', 8902],
         ['localhost', 8903],
         ['localhost', 8904],
         ['localhost', 8905]]
hashes_per_check = 10 ** 5

def blocktime(length):
    if length * block_reward < premine:
        return 30  # seconds
    else:
        return 60
