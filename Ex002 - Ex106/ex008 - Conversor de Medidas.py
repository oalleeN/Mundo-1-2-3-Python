''' Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''
m = float(input('Digite a distância: '))
km = m*0.001
hm = m*0.01
dam = m*0.1        # verificar um valor em metros para hm, hm, dam, dm, cm e mm!
dm = m*10
cm = m*100
mm = m*1000

print(f' O valor convertido para quilômetro é: {km:.0f}km \n O valor convertido para hectômetro é: {hm:.0f}hm')
print(f' O valor convertido para decametro é: {dam:.0f}dam')
print(f' O valor convertido para decimetro é: {dm:.0f}dm \n O valor convertido para centímetro é: {cm:.0f}cm')
print(f' O valor covertido para milímetro é: {mm:.0f}mm')

# segunda opção e mais prática!

m = float(input('Digite a distância: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000

print(f' O valor convertido para quilômetro é: {km:.0f}km \n O valor convertido para hectômetro é: {hm:.0f}hm')
print(f' O valor convertido para decametro é: {dam:.0f}dam')
print(f' O valor convertido para decimetro é: {dm:.0f}dm \n O valor convertido para centímetro é: {cm:.0f}cm')
print(f' O valor covertido para milímetro é: {mm:.0f}mm')
