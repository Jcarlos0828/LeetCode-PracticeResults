'''
EASY 929. Unique Email Addresses
'''
class Solution:
    def numUniqueEmails(self, emails: '''List[str]''') -> int:
        set_emails = set()
        for i in emails:
            localDomainName = i.split('@')
            getLocalName = localDomainName[0].split('+',1)
            getLocalName = getLocalName[0].split('.')
            getLocalName = ''.join(getLocalName)
            getLocalName = '@'.join((getLocalName,localDomainName[1]))
            print(getLocalName)
            set_emails.add(getLocalName)
        return len(set_emails)