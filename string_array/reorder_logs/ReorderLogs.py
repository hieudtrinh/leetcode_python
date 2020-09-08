from typing import List


class ReorderLogs:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digits = []
        letters = []
        # divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)


        letters.sort(key = lambda x: x.split()[0])            #when suffix is tie, sort by identifier
        letters.sort(key = lambda x: x.split()[1:])           #sort by suffix
        result = letters + digits                                        #put digit logs after letter logs
        return result


    def reorderLogFiles2(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero", "let0 art can"]
reoderlogs = ReorderLogs()
logs1 = reoderlogs.reorderLogFiles(logs)
logs2 = reoderlogs.reorderLogFiles2(logs)
print(logs1)
print(logs2)