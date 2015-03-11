import copy
import tools
import blockchain
import custom
import http


def add(malSig, pubkey, privkey, DB):
    tx = {'type': 'add',
          'malSig': malSig,
          'pubkeys': [pubkey],
          }
    easy_add_transaction(tx, privkey, DB)


def drop(malSig, pubkey, privkey, DB):
    tx = {'type': 'drop',
          'malSig': malSig,
          'pubkeys': [pubkey],}
    easy_add_transaction(tx, privkey, DB)


def easy_add_transaction(tx_orig, privkey, DB):
    tx = copy.deepcopy(tx_orig)
    pubkey = tools.privtopub(privkey)
    address = tools.make_address([pubkey], 1)
    try:
        tx['count'] = blockchain.count(address, DB)
    except:
        tx['count'] = 1
    tx['signatures'] = [tools.sign(tools.detSha(tx), privkey)]
    print('CREATED TX: ' + str(tx))
    blockchain.add_tx(tx, DB)


submit_form = '''
<form name="first" action="{}" method="{}">
<input type="submit" value="{}">{}
</form> {}
'''
empty_page = '<html><body>{}</body></html>'


def easyForm(link, button_says, more_html='', form_type='post'):
    a = submit_form.format(link, '{}', button_says, more_html, "{}")
    if form_type == 'get':
        return a.format('get', '{}')
    else:
        return a.format('post', '{}')


linkHome = easyForm('/', 'HOME', '', 'get')


def page1(DB, brainwallet=custom.brainwallet):
    out = empty_page
    txt = '<input type="text" name="BrainWallet" value="{}">'
    out = out.format(easyForm('/home', 'Enter BasicCoin wallet passphrase: ', txt.format(brainwallet)))
    return out.format('')


def home(DB, dic):
    if 'BrainWallet' in dic:
        dic['privkey'] = tools.detSha(dic['BrainWallet'])
    elif 'privkey' not in dic:
        return "<p>You didn't type in your brain wallet.</p>"
    privkey = dic['privkey']
    pubkey = tools.privtopub(dic['privkey'])
    address = tools.make_address([pubkey], 1)
    if 'doAdd' in dic:
        add(dic['malSig'], pubkey, privkey, DB)
    if 'doDrop' in dic:
        drop(dic['malSig'], pubkey, privkey, DB)
    out = empty_page
    out = out.format('<p>your address: ' + str(address) + '</p>{}')
    out = out.format('<p>current block: ' + str(DB['length']) + '</p>{}')
    balance = blockchain.db_get(address, DB)['amount']
    for tx in DB['txs']:
        if tx['type'] == 'spend' and tx['to'] == address:
            balance += tx['amount'] - custom.fee
        if tx['type'] == 'spend' and tx['pubkeys'][0] == pubkey:
            balance -= tx['amount']
    out = out.format('<p>current balance is: ' + str(balance / 100000.0) + '</p>{}')
    if balance > 0:
        out = out.format(easyForm(
            '/home', 'add signatures', '''
        <input type="hidden" name="doAdd" value="add">
        <input type="text" name="malSig" value="malware signature">
        <input type="hidden" name="privkey" value="{}">'''.format(privkey)))

        out = out.format(easyForm('/home', 'remove signatures', '''
        <input type="hidden" name="doDrop" value="drop">
        <input type="text" name="malSig" value="malware signature">
        <input type="hidden" name="privkey" value="{}">'''.format(privkey)))

    txt = '''    <input type="hidden" name="privkey" value="{}">'''
    s = easyForm('/home', 'Refresh', txt.format(privkey))
    return out.format(s)


def hex2htmlPicture(string, size):
    txt = '<img height="{}" src="data:image/png;base64,{}">{}'
    return txt.format(str(size), string, '{}')


def main(port, brain_wallet, db):
    global DB
    DB = db
    http.server(DB, port, page1, home)
