"""This file explains how we tell if a transaction is valid or not, it explains
how we update the system when new transactions are added to the blockchain."""
import blockchain
import custom
import copy
import tools
import verify


def addr(tx):
    return tools.make_address(tx['pubkeys'], len(tx['signatures']))


def sigVerify(tx, txs, DB):

    def sigs_match(sigs, pubs, msg):
        x = all(tools.verify(msg, sig, pub) for sig in sigs for pub in pubs)
        return x

    tx_copy = copy.deepcopy(tx)
    tx_copy.pop('signatures')
    if len(tx['pubkeys']) == 0:
        return False
    if len(tx['signatures']) > len(tx['pubkeys']):
        return False
    msg = tools.detSha(tx_copy)
    if not sigs_match(copy.deepcopy(tx['signatures']),
                      copy.deepcopy(tx['pubkeys']), msg):
        return False
    try:
        if not verify.sigCheck(tx['malSig'], tx['type']):
            return False
    except:
        return False
    return True

def mint_verify(tx, txs, DB):
    return 0 == len(filter(lambda t: t['type'] == 'mint', txs))

tx_check = {'add': sigVerify, 'drop': sigVerify, 'mint': mint_verify}

def adjust(key, pubkey, amount, DB, sign=1):
    acc = blockchain.db_get(pubkey, DB)
    if not DB['add_block']: sign=-1
    acc[key] += amount*sign
    blockchain.db_put(pubkey, acc, DB)


def mint(tx, DB):
    address = addr(tx)
    adjust('amount', address, custom.block_reward, DB)
    adjust('count', address, 1, DB)


def void(tx, DB):
    pass

update = {'mint': mint, 'add': void, 'drop': void}
#-----------------------------------------
