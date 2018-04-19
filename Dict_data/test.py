import re

regex = re.compile(r'\b[a-z]*[āáǎàōóǒòêēéěèīíǐìūúǔùǖǘǚǜüńňǹɑɡ]+[a-z]*\b')
text = "Thǐs ís à pìnyin abóut shá"
m = regex.findall(text)
print(m)