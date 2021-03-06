import re

# Matching Regex Objects
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 555-123-4567.')
print('Phone number found: ' + mo.group())

# Adding parentheses will create groups in the regex
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 555-123-4567.')
print('Phone number found: ' + mo.group())

# Let's take a look what is in the groups
mo.group(1)
#* '555'
mo.group(2)
#* '123-4567'
mo.group(0)
#* '555-123-4567'
mo.group()
#* 555-123-4567
mo.groups()
#* ('555', '123-4567')

# It's useful to somehow separate the values
areaCode, mainNumber = mo.groups()
print(areaCode)
#* 555
print(mainNumber)
#* 123-4567

# Matching Multiple Groups with the Pipe
someRegex = re.compile (r'John Smith|Jane Doe')
mo1 = someRegex.search('John Smith and Jane Doe')
mo1.group()
#* 'John Smith'
mo2 = someRegex.search('Jane Doe and John Smith')
mo2.group()
#* 'Jane Doe'

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
#* 'Batmobile'
mo.group(1)
#* 'mobile'

# Optional Matching with the Question Mark
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
#* 'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
#* 'Batwoman'

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 777-123-4567')
mo1.group()
#* '777-123-4567'

mo2 = phoneRegex.search('My number is 123-4567')
mo2.group()
#* '123-4567'

# Matching Zero or More with the Star
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
#* 'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
#* 'Batwoman'

mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()
#* 'Batwowowowoman'

# Matching One or More with the Plus
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()
#* 'Batwoman'

mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()
#* 'Batwowowowoman'

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None
#* True

# Matching Specific Repetitions with Braces
naRegex = re.compile(r'(Na){3}')
mo1 = naRegex.search('NaNaNa')
mo1.group()
#* 'NaNaNa'

mo2 = naRegex.search('Na')
mo2 == None
#* True

# Greedy and Non-greedy Matching
#! Python’s regular expressions are greedy by default, which means that 
#! in ambiguous situations they will match the longest string possible.
greedyNaRegex = re.compile(r'(Na){3,5}')
mo1 = greedyNaRegex.search('NaNaNaNaNa')
mo1.group()
#* 'NaNaNaNaNa'

nongreedyNaRegex = re.compile(r'(Na){3,5}?')
mo2 = nongreedyNaRegex.search('NaNaNaNaNa')
mo2.group()
#* 'NaNaNa'

# findall() method
# w/o groups
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') 
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
#* ['415-555-9999', '212-555-0000']

# w/ groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') 
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
#* [('415', '555', '9999'), ('212', '555', '0000')]

# Character Classes

# In the earlier phone number regex example, you learned that \d could stand for any numeric digit. 
# That is, \d is shorthand for the regular expression (0|1|2|3|4|5|6|7|8|9). 
# There are many such shorthand character classes, as shown below:

# Shorthand Codes for Common Character Classes

#! Shorthand | Represents
#! character |
#! class     |
#! -------------------------------------------------------------------------------------------------
#! \d        | Any numeric digit from 0 to 9.
#! \D        | Any character that is not a numeric digit from 0 to 9.
#! \w        | Any letter, numeric digit, or the underscore character. (As matching “word” characters.)
#! \W        | Any character that is not a letter, numeric digit, or the underscore character.
#! \s        | Any space, tab, or newline character. (As matching “space” characters.)
#! \S        | Any character that is not a space, tab, or newline.

# The regular expression \d+\s\w+ will match 
# text that has one or more numeric digits (\d+), 
# followed by a whitespace character (\s), 
# followed by one or more letter/digit/underscore characters (\w+). 
# The findall() method returns all matching strings of the regex pattern in a list.

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
#* ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']

# Making Your Own Character Classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
consonantRegex = re.compile(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]')

vowelRegex.findall('The quick brown FOX JUMPS OVER the lazy dog')
#* ['e', 'u', 'i', 'o', 'O', 'U', 'O', 'E', 'e', 'a', 'o']
consonantRegex.findall('The quick brown FOX JUMPS OVER the lazy dog')
#* ['T', 'h', 'q', 'c', 'k', 'b', 'r', 'w', 'n', 'F', 'X', 'J', 'M', 'P', 'S', 'V', 'R', 't', 'h', 'l', 'z', 'y', 'd', 'g']

# You can also include ranges of letters or numbers by using a hyphen.
alphaNumericRegex = re.compile(r'[a-zA-Z0-9]')
alphaNumericRegex.findall('No "punctuation marks" in the results. 11')
#* ['N', 'o', 'p', 'u', 'n', 'c', 't', 'u', 'a', 't', 'i', 'o', 'n', 'm', 'a', 'r', 'k', 's', 'i', 'n', 't', 'h', 'e', 'r', 'e', 's', 'u', 'l', 't', 's', '1', '1']

# Note that inside the square brackets, the normal regular expression symbols are not interpreted as such. 
# This means you do not need to escape the ., *, ?, or () characters with a preceding backslash. 
# For example, the character class [0-5.] will match digits 0 to 5 and a period. You do not need to write it as [0-5\.].

# By placing a caret character (^) just after the character class’s opening bracket, you can make a negative character class. 
# A negative character class will match all the characters that are not in the character class. 
notAlphaNumericRegex = re.compile(r'[^a-zA-Z0-9]')
notAlphaNumericRegex.findall('No "punctuation marks" in the results. 11')
#* [' ', '"', ' ', '"', ' ', ' ', ' ', '.', ' ']

# The Caret and Dollar Sign Characters

#  You can also use the caret symbol (^) at the start of a regex to indicate that a match must occur 
# at the beginning of the searched text. Likewise, you can put a dollar sign ($) at the end of the 
# regex to indicate the string must end with this regex pattern. 
#  And you can use the ^ and $ together to indicate that the entire string must match the regex—that 
# is, it’s not enough for a match to be made on some subset of the string.

beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello, world!')
#* <re.Match object; span=(0, 5), match='Hello'>

beginsWithHello.search('He said hello.') == None
#* True

# The r'\d$' regular expression string matches strings that end with a numeric character from 0 to 9.
endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
#* <re.Match object; span=(16, 17), match='2'>

endsWithNumber.search('Your number is forty two.') == None
#* True

# The r'^\d+$' regular expression string matches strings that both begin and end with one or more numeric characters.
wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
#* <re.Match object; span=(0, 10), match='1234567890'>

wholeStringIsNum.search('12345xyz67890') == None
#* True
wholeStringIsNum.search('12  34567890') == None
#* True

#! Carrots cost dollars (Caret^ symbol comes first, Dollar$ comes as the end)

# The Wildcard Character

# The . (or dot) character in a regular expression is called a wildcard 
# and will match any character except for a newline.
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
#* ['cat', 'hat', 'sat', 'lat', 'mat']

# Remember that the dot character will match just one character, which is why the match for 
# the text flat in the previous example matched only lat. 
# To match an actual dot, escape the dot with a backslash: \.
atRegex = re.compile(r'.at\.')
atRegex.findall('The cat in the hat sat on the flat mat.')
#* ['mat.']

atRegex = re.compile(r'..at')
atRegex.findall('The cat in the hat sat on the flat mat.')
#* [' cat', ' hat', ' sat', 'flat', ' mat']

atRegex = re.compile(r'\w{1,2}at')
atRegex.findall('The cat in the hat sat on the flat mat.')
#* ['cat', 'hat', 'sat', 'flat', 'mat']

# Matching Everything with Dot-Star

#  Remember that the dot character means "any single character except the newline,"
# and the star character means "zero or more of the preceding character."
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: John Last Name: Doe')
mo.group(1)
#* 'John'
mo.group(2)
#* 'Doe'

#  The dot-star uses greedy mode: It will always try to match as much text as possible. 
# To match any and all text in a non-greedy fashion, use the dot, star, and question mark (.*?).
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group()
#* '<To serve man>'

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()
#* '<To serve man> for dinner.>'

# Matching Newlines with the Dot Character

#  The dot-star will match everything except a newline. 
noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
#* 'Serve the public trust.'

# By passing re.DOTALL as the second argument to re.compile(), you can make the dot character match 
# all characters, including the newline character.
newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
#* 'Serve the public trust.\nProtect the innocent.\nUphold the law.'


#! The ? matches zero or one of the preceding group.
#! The * matches zero or more of the preceding group.
#! The + matches one or more of the preceding group.
#! The {n} matches exactly n of the preceding group.
#! The {n,} matches n or more of the preceding group.
#! The {,m} matches 0 to m of the preceding group.
#! The {n,m} matches at least n and at most m of the preceding group.
#! {n,m}? or *? or +? performs a non-greedy match of the preceding group.
#! ^spam means the string must begin with spam.
#! spam$ means the string must end with spam.
#! The . matches any character, except newline characters.
#! \d, \w, and \s match a digit, word, or space character, respectively.
#! \D, \W, and \S match anything except a digit, word, or space character, respectively.
#! [abc] matches any character between the brackets (such as a, b, or c).
#! [^abc] matches any character that isn’t between the brackets.

# Case-Insensitive Matching

# To make your regex case-insensitive, you can pass re.IGNORECASE 
# or re.I as a second argument to re.compile().
robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()
#* 'RoboCop'

robocop.search('ROBOCOP protects the innocent.').group()
#* 'ROBOCOP'

robocop.search('John, why does your book talk about robocop?').group()
#* 'robocop'

# Substituting Strings

namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
#* 'CENSORED gave the secret documents to CENSORED.'

agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
#* 'A**** told C**** that E**** knew B**** was a double agent.'

# Managing Complex Regexes

# instead of a hard-to-read regular expression like this:
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

#you can spread the regular expression over multiple lines with comments like this:
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    (\d{3})                       # first 3 digits
    (\s|-|\.)                     # separator
    (\d{4})                       # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

mo = phoneRegex.search('My number is 555.123-4567 ext. 456.')
mo.groups()
#* ('555.123-4567 ext. 456', '555', '.', '123', '-', '4567', ' ext. 456', 'ext.')

# Combining flags (re.IGNORECASE, re.DOTALL, re.VERBOSE etc)

# the re.compile() function takes only a single value as its second argument.
# but you can use pipes:
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
someRegexValue.search('Foo bar').group()
#* 'Foo'
