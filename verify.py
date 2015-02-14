import urllib, urllib2
from virus_total_apis import PublicApi as vtAPI
import consensus
apiKey = '72567edcd2b6af6da376b765f73b867fa7fe8606b9fab0e5319f4504eb6fce55'

def sigCheck(malSig, type):

    def getReport(sig):
        vt = vtAPI(apiKey)
        report = vt.get_file_report(sig)
        return report

    if type == 'add':
        report = getReport(malSig)
        if 'response_code' not in report['results']:
            return False
        if report['results']['response_code'] == 0:
            return True
        elif report['results']['response_code'] == 1:
            ratio = float(report['results']['positives']) / float(report['results']['total'])
            if (ratio) <= 0.1:
                # this is the error case
                return False
            else:
                return True

    if type == 'drop':
        report = getReport(malSig)
        if 'response_code' not in report['results']:
            return False
        if report['results']['response_code'] == 0:
            return False
        elif report['results']['response_code'] == 1:
            if (int(report['results']['positives']) / int(report['results']['total'])) >= 0.5:
                return True
            else:
                # error case, in order to drop sig must be known good
                return False