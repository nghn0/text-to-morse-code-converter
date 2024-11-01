morse_codes = [
    ('.-', 'A'),
    ('-...', 'B'),
    ('-.-.', 'C'),
    ('-..', 'D'),
    ('.', 'E'),
    ('..-.', 'F'),
    ('--.', 'G'),
    ('....', 'H'),
    ('..', 'I'),
    ('.---', 'J'),
    ('-.-', 'K'),
    ('.-..', 'L'),
    ('--', 'M'),
    ('-.', 'N'),
    ('---', 'O'),
    ('.--.', 'P'),
    ('--.-', 'Q'),
    ('.-.', 'R'),
    ('...', 'S'),
    ('-', 'T'),
    ('..-', 'U'),
    ('...-', 'V'),
    ('.--', 'W'),
    ('-..-', 'X'),
    ('-.--', 'Y'),
    ('--..', 'Z'),
    ('-----', '0'),
    ('.----', '1'),
    ('..---', '2'),
    ('...--', '3'),
    ('....-', '4'),
    ('.....', '5'),
    ('-....', '6'),
    ('--...', '7'),
    ('---..', '8'),
    ('----.', '9'),
    ('/', ' ')
]


def check_letter(ch):
    is_there = False
    for codes in morse_codes:
        if ch in codes:
            is_there = True
    if not is_there:
        raise Exception(f"{ch} is not in between A-Z or 0-9")


def check_code(code):
    is_there = False
    for codes in morse_codes:
        if code in codes:
            is_there = True
    if not is_there:
        raise Exception(f"{code} is not a valid code between A-Z or 0-9")


text = input("Enter a text : ")
text = text.upper()
code = ''
for i in text:
    check_letter(i)
    for j in morse_codes:
        if i == j[1]:
            code = code + j[0] + " "

print(f"{text} in morse format: {code}")

m_code = input("Enter the morse code: ")
m_code = m_code.split()
to_text = ''
for i in m_code:
    check_code(i)
    for j in morse_codes:
        if i == j[0]:
            to_text = to_text + j[1]
print(to_text)
