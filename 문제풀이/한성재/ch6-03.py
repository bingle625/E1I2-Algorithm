# 로그파일 재정렬

# try 예시된 input 처리에는 적합하나, 식별자가 달라질 경우를 대비하지 못함.
def reorderLogFiles(logs: list):
    """
    :type logs: List[str]
    :rtype: List[str]
    """
    new_log = []

    for log in logs:
        if log.startswith("let"):
            new_log.append(log)

    new_log.sort(key=lambda log: log[4:])

    for log in logs:
        if log.startswith("dig"):
            new_log.append(log)

    return new_log


logs2 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
         "let2 own kit dig", "let3 art ban"]

logs2 = reorderLogFiles(logs2)

print(logs2)
