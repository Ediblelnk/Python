import re

sentence = 'The quick brown fox jumps over the lazy dog.'
excerpt1 = 'I took a deep breath and listened to the old brag of my heart. I am, I am, I am.'
excerpt2 = 'The most beautiful things in the world can be seen and touched; they are felt with the heart.'
repeated = 'The ants, dug, dug, dug, until they died for their queen.'
all_caps = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'
all_lower = 'this is all lowercase.'
all_nums = '10710948574'
mixed = '1495871asdf304985htyjew7afjqorif409jq43j'

"""
re.math searches for the pattern (arg 1) in the beginning of the string (arg 2), returns boolean
"""
if re.match(r'T', sentence):
    print('1 match')

"""
re.search for the pattern in the entire string, returns boolean
"""
if re.search(r'a', excerpt1):
    print('2 match')

"""
re.findall return a list of all non-overlapping matches in the string
"""
if re.findall(r'dug', repeated):
    print('3 match:', re.findall(r'dug', repeated))

"""
re.search returns an object with several methods that give details about it
"""
match_ = re.search(r'THE', all_caps)
if match_:
    print('4 match:', end=' ')
    print(match_.group(), match_.start(), match_.end(), match_.span(), sep=', ')
"""
group - returns the string matched
start - returns the start position of the first match
end - returns the end position of the first match
span - returns 'start' and 'end' as a tuple
"""

"""
re.sub(pattern, repl, string, count=0)
replaces all occurences of the pattern in string with repl, substituting all occurences,
unless count provided. returns the modified string
"""
u_excerpt1 = re.sub(r'I', 'You', excerpt1)
print(f'5 match: excerpt1, but with "I" replaced with "You" - \n\t{u_excerpt1}')

"""
. metacharacter - matches any character OTHER THAN a new line (\n)
"""
g = r'gr.y'
if re.match(g, 'grey'):
    print('6 match')
if re.match(g, 'gray'):
    print('7 match')
if re.match(g, 'blue'):
    print('8 match')

"""
^ metacharacter - match the start of a string
$ metacharacter - match the end of a string
"""
g = r'^gr.y$'
if re.match(g, 'grey'):
    print('9 match')
if re.match(g, 'greymatter'):
    print('10 match')

"""
[] - indicates the creation of a *character class*
provides a way to match only one of a specific set of characters

[a-z] matches any lowercase alphabetic character
[G-P] matches any UPPERCASE character from G to P
[0-9] matches any digit

^ within a character class inverts it, meaning it matches any character OTHER than the ones included in the class

"""
vowels = r'[aeiou]'
consonants = r'[^aeiou]'
if re.search(vowels, 'grey'):
    print('11 match')
if re.search(vowels, 'rhythm myths'):
    print('12 match')
if re.search(consonants, 'beans!'):
    print('13 match')

Aa0 = r'[A-Z][a-z][0-9]'
if re.search(Aa0, 'beans'):
    print('14 match')
if re.search(Aa0, 'Tg9'):
    print('15 match')

"""
* metacharacter - ZERO or more repetitions of the previous thing
+ metacharacter - ONE  or more repetitions of the previous thing
? metacharacter - ZERO or ONE  repetitions of the previous thing
{x,y} metacharacter - between x and y repetitions of the previous thing (inclusive)
x|y metacharacter - matches EITHER x or y

1*      matches '', '1', '11', '111', etc
1+      matches '1', '11', '111', etc
1?      matches '', '1' ONLY
1{2,4}  matches '11', '111', '1111'
1|2     matches '1' or '2'
"""

"""
() - indicates a group, which can be arguments to metacharacters

[match_object].group() - group(0) and group() returns the whole match
         - group(n) returns the nth group from the left
[match_object].groups() - returns all groups up from 1
"""
egg = r'egg(spam)*'
if re.match(egg, 'egg'):
    print('16 match')
if re.match(egg, "eggspamspamspamegg"):
    match_ = re.match(egg, "eggspamspamspamegg")
    print('17 match:', match_.group(), match_.group(1), match_.groups())
if re.match(egg, 'spam'):
    print('18 match')

"""
named groups:
(?P<name>...) - name is the name of the group, and ... is the content. can be accessed by group(name) in a match object

non-capturing groups:
(?:...) - ... is the content. not accessible by the group() method

"""
egg = r'(?P<growingchicken>egg)(?:spam)'
if re.match(egg, 'egg'):
    print('19 match')
if re.match(egg, "eggspamspamspamegg"):
    match_ = re.match(egg, "eggspamspamspamegg")
    print('20 match:', match_.group(), match_.groups())
if re.match(egg, 'spam'):
    print('21 match')

"""
special sequences
\d - digits
\s - whitespace
\w - word characters
\D - all EXCEPT digits
\S - all EXCEPT whitespace
\W - all EXCEPT word characters
\A - beginning of a string
\Z - end of a string
\b - empty string between \w and \W characters
\B - matches the empty string anywhere else
"""