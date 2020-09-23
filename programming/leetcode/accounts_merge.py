# https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: [[str]]) -> [[str]]:
        res = []
        mapping = dict()
        for account in accounts:
            name = account[0]
            emails = set(account[1:])
            if name in mapping:
                if len(mapping[name] & emails) > 0:
                    mapping[name] |= emails
                else:
                    acc = list(emails)
                    acc.sort()
                    acc.insert(0, name)
                    res.append(acc)
            else:
                mapping[name] = emails
        
        for name, emails in mapping.items():
            arr = [name]
            sorted_emails = list(emails)
            sorted_emails.sort()
            arr.extend(sorted_emails)
            res.append(arr)
        
        return res
        

arr = [["Kevin","Kevin1@m.co","Kevin5@m.co","Kevin2@m.co"],["Bob","Bob3@m.co","Bob1@m.co","Bob2@m.co"],["Lily","Lily3@m.co","Lily2@m.co","Lily0@m.co"],["Gabe","Gabe2@m.co","Gabe0@m.co","Gabe2@m.co"],["Kevin","Kevin4@m.co","Kevin3@m.co","Kevin3@m.co"]]
out = [["Lily","Lily0@m.co","Lily2@m.co","Lily3@m.co"],["Gabe","Gabe0@m.co","Gabe2@m.co"],["Kevin","Kevin1@m.co","Kevin2@m.co","Kevin5@m.co"],["Kevin","Kevin3@m.co","Kevin4@m.co"],["Bob","Bob1@m.co","Bob2@m.co","Bob3@m.co"]]


[["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]

s = Solution()
assert s.accountsMerge(arr) == out
