# Import libraries
import dns.resolver

HOST = 'activity.lumu.io'

for qtype in ['A', 'AAAA', 'NS', 'MX', 'CNAME', 'SOA', 'TXT']:
    results = dns.resolver.resolve(HOST, qtype, raise_on_no_answer=False)
    for result in results:
        print( qtype.__str__(), 'Record : ', result.to_text())
