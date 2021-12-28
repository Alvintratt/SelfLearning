
#Comments
#[Multi line comments
# (# skapades auto in. blankrum)]

#Variabel if elif else test [Resultat:
# GÅR UPPIFRÅN GÅR NER OCH SLUT NÄR DEN HAR FÅTT ETT POSITIV IF/ELIF/ELSE KOMMANDO. ALLTSÅ ATT OM A = 2 OCH B = 3 STÅR DET BARA "A < B" OCH INTE "A < B  A < C"]

a = 2
b = 3
c = 2

if a < b:
    print('A < B')
elif a > b:
    print('A > B')
elif a < c:
    print('A < C')
elif a > c:
    print('A > C')
elif b < c:
    print('B < C')
elif b > c:
    print('b > c')
else:
    print('A == B')

#Function (osäker, länge sedan)

function = 'myFunction' #Råkade göra function till en variabel istället för en function. Google. https://youtu.be/-Bkupx9gX0o?list=PL98qAXLA6afuh50qD2MdAj3ofYjZR_Phn

#function1
#Före print()/Övrigt tab före = body
#Om kör def myFunction():   print('Test1')  print('Test2') = Ingenting i terminal
def myFunction():
    print('Test1')
    print('Test2')
#Ska fungera: [Resultat
# FUNGERAR. PRINT = A < B(FÖRE VARIABEL)    Test1   Test2] Slut bedömning: def kommandot definerar en function. Alltså den förklarar vad functionen ska göra. Men den fungerar inte om man bara kör den sådär. Man behöver aktivera den genom att skirav utan body på en annan rad: *function namn*()
myFunction()

#function2
def myFunction2():
    print('Test3')
    print('Test4')

#Matte function

def add_numbers(n1, n2):
    sum = n1 + n2
    return sum

result = add_numbers(5.4, 6.7)
#Dubbel function test (2 functions på samma rad) [Resultat:
# ERROR: STATEMENTS MUST BE SEPERATED BY NEWLINES OR SEMICOLONS. (ERROR FIXAD) Slut bedömning: blanksteg används för nya kommandon, och om jag har rätt så kan man skriva kommandon efter function kommandot, men inte en annan function med ett enkelt blanksteg efter.]
myFunction 
myFunction2
add_numbers

#GitHub release
'''
Detta är den första ändringen i denna kod innan den blev pushad till GitHub i SelfLearning.py med message commit1.
CTRL + S gör inget.
Skapar commit2
Push.
Success.
Commit3
'''

#Tabnine
#Har just lagt till Tabnine