import re

META_CHAR = "   . ^ $ * + ? { } [ ] \ | ( )    "

SPECIAL_CHAR_DICT = {
    '\d': 'Match any decimal digit',
    '\D': 'Match any non-digit char, equivalent to [^0-9]',
    '\s': 'Match any whitespace',
    '\S': 'Match any non-whitespace char',
    '\w': 'Match any alphanumeric char, `_` is included',
    '\W': 'Match any non-alphanumeric char, `_` is excluded',
    }

""" You can use special char in character class, like [\s.,]
will match any whitespace, dot or comma."""


### Repetition Mechanism

"""
Repetitions such as * are greedy; when repeating a RE,
the matching engine will try to repeat it as many times as possible.
If later portions of the pattern don’t match,
the matching engine will then back up and try again with few repetitions.

A step-by-step example will make this more obvious.
Let’s consider the expression a[bcd]*b.
This matches the letter 'a', zero or more letters from the class [bcd],
and finally ends with a 'b'.
Now imagine matching this RE against the string abcbd.

Step        Matched Explanation
1   a       The a in the RE matches.
2   abcbd   The engine matches [bcd]*, going as far as it can, which is to the end of the string.
3   Failure The engine tries to match b, but the current position is at the end of the string, so it fails.
4   abcb    Back up, so that [bcd]* matches one less character.
5   Failure Try b again, but the current position is at the last character, which is a 'd'.
6   abc Back up again, so that [bcd]* is only matching bc.
6   abcb    Try b again. This time the character at the current position is 'b', so it succeeds.

The end of the RE has now been reached, and it has matched abcb.
This demonstrates how the matching engine goes as far as it can at first,
and if no match is found it will then progressively back up and retry the rest of the RE again and again.
It will back up until it has tried zero matches for [bcd]*,
and if that subsequently fails,
the engine will conclude that the string doesn’t match the RE at all.
"""

REPETITION_CHAR_DICT = {
    '?': "Match 0 or 1 time",
    '*': "Match 0 or ANY times",
    '+': "Match 1 or ANY times",
    '{m,n}': "Match at least m times, at most n times",
    }

# In {m,n} if m is omitted, it means the low limit is 0.
# if n is omitted, it means the up limit is 2 billion.


##### RE Module

import re
p = re.complie('ab*')  # p is short for pattern
p2 = re.complie('ab*', re.IGNORECASE)  # make an ignore case pattern


### Backslash Plague

r"""
The Backslash Plague
As stated earlier, regular expressions use the backslash character ('\') to indicate special forms or
to allow special characters to be used without invoking their special meaning.
This conflicts with Python’s usage of the same character for the same purpose in string literals.

Let’s say you want to write a RE that matches the string \section, which might be found in a LaTeX file.
To figure out what to write in the program code, start with the desired string to be matched.
Next, you must escape any backslashes and other metacharacters by preceding them with a backslash,
resulting in the string \\section. The resulting string that must be passed to re.compile() must be \\section.
However, to express this as a Python string literal, both backslashes must be escaped again.

Characters  Stage
\section    Text string to be matched
\\section   Escaped backslash for re.compile()
"\\\\section"   Escaped backslashes for a string literal

In short, to match a literal backslash, one has to write '\\\\' as the RE string,
because the regular expression must be \\, and each backslash must be expressed as \\ inside a regular Python string literal.
In REs that feature backslashes repeatedly,
this leads to lots of repeated backslashes and makes the resulting strings difficult to understand.

The solution is to use Python’s raw string notation for regular expressions;
backslashes are not handled in any special way in a string literal prefixed with 'r',
so r"\n" is a two-character string containing '\' and 'n', while "\n" is a one-character string containing a newline.
Regular expressions will often be written in Python code using this raw string notation.

Regular String  Raw string
"ab*"           r"ab*"
"\\\\section"   r"\\section"
"\\w+\\s+\\1"   r"\w+\s+\1"

"""

### Match the pattern

""" When you made a pattern with re.compile(r'pattern_string'), you can use its method to do some regex operation """

COMMON_PATTERN_METHODS = {
    'match()': 'Determine if the RE matches at the beginning of a string.',
    'search()': 'Scan a string, looking for any position the pattern matches.',
    'findall()': 'Find all matched substr, return them as a list of str.',
    'finditer()': 'Find all matched substr, return them as an iterator of re-match object'
    }

"""
Or you can use `re`-module's functions for such pattern setting.
re.method(r'pattern_string', material, flag) is equivalent to pattern.method(material, flag)
"""

COMMON_MATCH_OBJECT_METHODS = {
    'group()': 'Return the string(group 0) matched by the RE',
    'groups()': 'Return all the sub_groups(except 0) matched by the RE',
    'start()': 'Return the starting position of the match',
    'end()': 'Return the ending position of the match',
    'span()': 'Return a tuple of (start, end) position'
    }


### Compilation Flags

"""
Compilation flags let you modify some aspects of how regular expressions work.
Flags are available in the re module under two names, a long name such as IGNORECASE and a short, one-letter form such as I.
(If you’re familiar with Perl’s pattern modifiers, the one-letter forms use the same letters; the short form of re.VERBOSE is re.X, for example.)
Multiple flags can be specified by bitwise OR-ing them; re.I | re.M sets both the I and M flags, for example.
"""
FLAG_USAGE_DICT = {
    ("DOTALL", "S"): "Make . match any character, including newlines",
    ("IGNORECASE", "I"): "Do case-insensitive matches",
    ("LOCALE", "L"): "Do a locale-aware match",
    ("MULTILINE", "M"): "Multi-line matching, affecting ^ and $",
    ("VERBOSE", "X"): "Enable verbose REs, which can be organized more cleanly and understandably.",
    ("UNICODE", "U"): "Makes several escapes like \w, \b, \s and \d dependent on the Unicode character database.",
    }

# Locale-mode:  \w can match Spanish chars like ñ if you set Spanish in your system locale-language file.
#
# Multiline-mode: As the material you passed to a pattern is always a string,
# thus ^ $ will treat the entire string as a whole line, and matches only the begging and end of it.
# But a whole book you passed to python re pattern is a string, too.
# We don't want ^ $ to match only the beginning and the end of the book.
# So if you enable multiline mode, ^ $ will also treat the substring between 2 newline character as a line, and match them.
#
# Dotall mode: this will make the dot `.` match newline character, too.
#
# Ignorecase mode: perform case-insensitive matching, be aware this flag won't effect special characters like French,
# unless you set Locale flag together with Ignorecase flag.
#
# Unicode mode: make \w, \W, \b, \B, \d, \D, \s and \S dependent on the Unicode character properties database.
#
# Verbose Mode(X): this will allow you to write Regex in a more readable way,
# in this mode, white spaces are ignored unless they are in character class or precede by backslash
# you can also put a comment inside lines precede with #, following is an example

charref = re.compile(
    r"""
    &[#]                # Start of a numeric entity reference
    (
        0[0-7]+         # Octal form
      | [0-9]+          # Decimal form
      | x[0-9a-fA-F]+   # Hexadecimal form
    )
    ;                   # Trailing semicolon
    """, re.VERBOSE)

### More Metacharacters
ZERO_WIDTH_ASSERTIONS = {
    '^': 'Beginning of line',
    '$': 'End of line',
    '|': 'Alternation expression',
    # Same as vim, a sequence of alphanumeric or '_' chars is considering a word
    r'\b': 'Word boundary, matches beginning or end of a word',
    '\B': 'Matching non-word-boundary position',
    '\A': 'Beginning of the string',  # string refers to python string, not a word.
    '\Z': 'End of the string',
    }


### Group
"""
You can use ( ) to encapsulate an expression as a group.
And retrieve the matching group latter use the match_object.group() funciton.
Group 0 is always present; it’s the whole RE.
To determine the group number, just count the opening parenthesis number from left to right.
By the way, you can pass multiple group number to match_object.group() method.
It will return what you ask for in a tuple.
The match_object.groups() method will return all sub_groups in a tuple.
Belowing is an example:
"""
"""
>>> p = re.compile('(a(b)c)d')
>>> m = p.match('abcd')
>>> m.group(0)
'abcd'
>>> m.group(1)
'abc'
>>> m.group(2)
'b'
>>> m.group(2, 1, 2)
('b', 'abc', 'b')
>>> m.groups()
('abc', 'b')
"""

# Named Groups & Special groups
#
# As the RE content could be quite complex, and numbered group can't mathc the need.
# We can use Perl-style and Python-style regex extension expressions.



# Non-capturing group
"""
Sometimes you’ll want to use a group to collect a part of a regular expression,
but aren’t interested in retrieving the group’s contents.
You can make this fact explicit by using a non-capturing group: (?:...),
where you can replace the ... with any other regular expression.

e.g.
>>> m = re.match("([abc])+", "abc")
>>> m.groups()
('c',)
>>> m = re.match("(?:[abc])+", "abc")
>>> m.groups()
()
>>> m.group()
'abc'
"""

# Lookahead Assertions
"""
Another zero-width assertion is the lookahead assertion.
Lookahead assertions are available in both positive and negative form.
(?=...)
    Positive lookahead assertion, This succeeds if the RE of ... successfully matches at the current location,
    and fails otherwise.
(?!...)
    This is the opposite of the positive assertion. It succeed when the ... pattern doesn't match at current location.

If we want find all files except those end with `bat` extension, we can do:
>>> re.findall(r'^.*[.](?!bat$).*$', 'engine.py\nfit.bat\nreadme.md', re.M)

The negative lookahead here means:
if the expression bat doesn’t match at this point, try the rest of the pattern;
if bat$ does match, the whole pattern will fail.

"""


# Named group
"""
The syntax for a named group is `(?P<name>...)`.
Named group is still given a number, so you can retrieve them both by number and name.
The syntax for named group backreference is (?P=name)
Belowing is an example:
>>> p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
>>> p.search('Paris in the the spring').group()
'the the'
"""


### Modifying Strings
""" Regular expression also allow you to modify strings """

RE_STRING_METHOD = {
    'split()': 'Split the string into a list, splitting it wherever the RE matches',    'sub()': 'Find all substrings where the RE matches, and replace them with a different string',
    'subn()': 'Does the same as sub(), but returns the new string and the number of replacements.',
    }

# Split Examples
p = re.compile(r'[aeiou]')
p.split('apple, banana, coco nuts')
# result: ['', 'ppl', ', b', 'n', 'n', ', c', 'c', ' n', 'ts']

# You can limit the split times by passing a maximum split number to the method
p.split('apple, banana, coco nuts', 3)
# result: ['', 'ppl', ', b', 'nana, coco nuts']

# If you want to add the delimiter into the result list, wrap your pattern with `()`
p2 = re.compile(r'([aeiou])')
p2.split('apple, banana, coco nuts')
# result: ['', 'a', 'ppl', 'e', ', b', 'a', 'n', 'a', 'n', 'a', ', c', 'o', 'c', 'o', ' n', 'u', 'ts']


# Substitution Examples
sub_p = re.compile(r'Jack|Jones')
sub_p.sub('Lier', "I don't like Jack & Jones")
# result: "I don't like Lier & Lier"

# you can add a count parameter to it to limit the substitution times, default value 0 means change all matchs.
sub_p.sub('Lier', "I don't like Jack & Jones", 1)
# result: "I don't like Lier & Jones"

# subn() did the same with sub, but will return a tuple containing a total number of replacement.
sub_p.subn('Lier', "I don't like Jack & Jones")
# result ("I don't like Lier & Lier", 2)

# Empty matches are replaced only when they’re not adjacent to a previous match.
sub_p2 = re.compile('x*')
p.sub('-', 'abxd')
# result: '-a-b-d-'
# Here each boundary was substitiute with the symbol `-`, except those round x,
# because they are considered one single match of `x*`

# In sub() method, you can use `\1` or `g<1>` to referred to numbered group.
# And `g<name>` to refer to named group.
# The three samples listed below are equivalent.

p = re.compile('section{ (?P<name> [^}]* ) }', re.VERBOSE)
p.sub(r'subsection{\1}','section{First}')
# result 'subsection{First}'
p.sub(r'subsection{\g<1>}','section{First}')
# result 'subsection{First}'
>>> p.sub(r'subsection{\g<name>}','section{First}')
# result 'subsection{First}'

# The replacement can be a function !
# If you use function to replace mathes, the function will be called, with the match object as parameter,
# the return value will be on the previous position of matches.

def square_match(match):
    """ return number ** number of matched number """
    value = int(match.group())
    return value ** value

re.sub('\d*', square_match, '1+2=3')
# result: '1+4=27'

### Common Problems

# Use String Methods
# if your task is simple enough, which string method is capable enough, use them instead of re
# string.split(), string.replace() and string.translate() are faster than their `re` relatives


# Greeady versus Non-Greedy

# Non greedy qualifier will find the minimum match for the pattern
NON_GREEDY_QUALIFIERS = ['??', '+?', '*?', '{m,n}?']

"""
When repeating a regular expression, as in a*,
the resulting action is to consume as much of the pattern as possible.
This fact often bites you when you’re trying to match a pair of balanced delimiters,
such as the angle brackets surrounding an HTML tag.
The naive pattern for matching a single HTML tag doesn’t work because of the greedy nature of .*.

>>>
>>> s = '<html><head><title>Title</title>'
>>> len(s)
32
>>> print re.match('<.*>', s).span()
(0, 32)
>>> print re.match('<.*>', s).group()
<html><head><title>Title</title>

The RE matches the '<' in <html>, and the .* consumes the rest of the string.
There’s still more left in the RE, though, and the > can’t match at the end of the string,
so the regular expression engine has to backtrack character by character until it finds a match for the >.
The final match extends from the '<' in <html> to the '>' in </title>, which isn’t what you want.

In this case, the solution is to use the non-greedy qualifiers *?, +?, ??, or {m,n}?,
which match as little text as possible. In the above example, the '>' is tried immediately after the first '<' matches, and when it fails, the engine advances a character at a time, retrying the '>' at every step. This produces just the right result:

>>>
>>> print re.match('<.*?>', s).group()
<html>

(Note that parsing HTML or XML with regular expressions is painful.
Quick-and-dirty patterns will handle common cases,
but HTML and XML have special cases that will break the obvious regular expression;
by the time you’ve written a regular expression that handles all of the possible cases,
the patterns will be very complicated. Use an HTML or XML parser module for such tasks.)

"""

# Using re.VERBOSE

"""
Regular expressions are a very compact notation, but they’re not terribly readable.
REs of moderate complexity can become lengthy collections of backslashes, parentheses, and metacharacters,
making them difficult to read and understand.
For such REs, specifying the re.VERBOSE flag when compiling the regular expression can be helpful,
because it allows you to format the regular expression more clearly.

pat = re.compile(r"""
 \s*                 # Skip leading whitespace
 (?P<header>[^:]+)   # Header name
 \s* :               # Whitespace, and a colon
 (?P<value>.*?)      # The header's value -- *? used to
                     # lose the following trailing whitespace
 \s*$                # Trailing whitespace to end-of-line
""", re.VERBOSE)

This is far more readable than:

pat = re.compile(r"\s*(?P<header>[^:]+)\s*:(?P<value>.*?)\s*$")

"""
