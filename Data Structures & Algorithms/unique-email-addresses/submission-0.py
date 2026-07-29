class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        clean = set()
        for email in emails:
            user , domain = email.split("@")
            user = user.split("+")[0]
            user = user.replace(".","")
            clean.add(f"{user}@{domain}")


        #     cleaned = email.replace(".", "")
        #     value = cleaned.index("+")
        #     end = cleaned.index("@")
        #     print(cleaned[:value] + cleaned[end:])
        #     clean.add(cleaned[:value] + cleaned[end:])

        # print(clean)
        return len(clean)