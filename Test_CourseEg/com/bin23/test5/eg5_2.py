import re

gaveStr = "site sea suede sweet see kase sse ssee loses teacher tea take tell eat"

print(re.findall(r'\b[st][a-z]*[er]\b', gaveStr))
