#Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input("Digite o 1º número: "));
num2 = int(input("Digite o 2º número: "));
num3 = int(input("Digite o 3º número: "));

if(num1 > num2 and num1 > num3):
    print(num1);
elif(num2 > num3 and num2 > num1):
    print(num2);
elif(num3 > num1 and num3 > num2):
    print(num3);

#Ordenando o numero do meio
if(num1 > num3 and num1 < num2):
    print(num1);
elif(num2 > num1 and num2 < num3):
    print(num2);
elif(num3 > num1 and num3 > num2):
    print(num3);
elif(num2 < num1 and num2 > num3):
    print(num2);

if(num1 < num2 and num1 < num3):
    print(num1);
elif(num2 < num1 and num2 < num3):
    print(num2);
elif(num3 < num1 and num3 < num2):
    print(num3);

