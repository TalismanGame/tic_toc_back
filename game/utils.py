from random import randrange

alphabet = 'abcdefghijklmnopqrstuvwxyz'
def GenerateInviteCode():
    code = ''
    for i in range(9):
        randomKey = randrange(len(alphabet))
        code += alphabet[randomKey]
    return code