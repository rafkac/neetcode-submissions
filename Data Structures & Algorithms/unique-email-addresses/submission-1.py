class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = set()

        for e in emails:
            username, domain = (e.split("@"))
            username = username.replace(".", "")
            username = (username.split("+"))[0]
            
            uniques.add(username + domain)

        return len(uniques)


        