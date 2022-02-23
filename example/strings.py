'spam eggs' #single quotes
"spam eggs" # double quotes

#escape sequences
'\n' #newline
'\\' #backslash
'\'' #single quote
'\"' #double quote
'\r' #return / enter
'\t' #tab
'\v' #vertical tab
'\b' #backspace
'\f' #ASCII Form feed / Page break
#\ooo #Octal Value oo
#\xhh #Hex Value hh

u'string' #Unicode modifier, converts to unicode, more characters, more memory
b'string' #Byte modifier, converts to ASCII, less characters, less memory
r'string' #Raw modifier, string expressed as is, <ignores escape characters>
f'string' #Format modifier, express variables within a string

string = """this string is 
crossing multiple lines"""

#Strings can be concatenated with + and repeated with *
print('ba' + 'na' * 2) #= 'banana'

#Strings next to each other are automatically concatenated
print('to''get''her') #= 'together'
#this is useful for organization
glue = ('glue WILL'
	' stick to itself')

#Strings can be indexed
print(glue[3]) #prints 4th character
print(glue[-1]) #prints last character

#Strings can be sliced
glue[0:4] #0 incl to 4 exclu
glue[4:] #from 4 inclu to end
glue[:9] #from begining to 9 exclu

#Notable Methods
glue.capitalize() #puts first letter into titlecase
glue.endswith('to', 0, len(glue)-7) #boolean, true if it does, false if not
glue.startswith('') #boolean, true if it does, false if not
glue.find('') #returns index of first occurance, -1 if not found
glue.strip('') #returns copy of string with argument character removed at start or end
glue.removeprefix('') #removes argument if it is a prefix, also suffix variant
print(glue.replace(' ', '_', 2)) #third argument is optional, used for number of replacements
print(glue.split(' ')) #returns list of string, separated by argument
print(glue.swapcase()) #return copy with uppercase to lowercase and vice versa
print(glue.title()) #returns a titlecased version of string