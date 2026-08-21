class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = []

        for e in emails:
            username, domain = (e.split("@"))
            username = username.replace(".", "")
            if "+" in username:
                username = (username.split("+"))[0]

            if username + domain not in uniques:
                uniques.append(username + domain)

        print(uniques)


        return len(uniques)


        