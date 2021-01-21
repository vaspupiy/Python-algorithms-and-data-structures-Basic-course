# https://drive.google.com/file/d/1udTCq6-gPpIhv477x7aTpk-aKRozgSj0/view?usp=sharing

# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

not_5 = ~ 5
print(f'Результат логической побитовой операции «Не» над числом 5: число  {not_5}  ({bin(not_5)})')

not_6 = ~ 6
print(f'Результат логической побитовой операции «Не» над числом 6: число  {not_6}  ({bin(not_6)})')

and_5_6 = 5 & 6
print(f'Результат логической побитовой операции «И» над числами 5 и 6: число  {and_5_6} '
      f'({bin(5)} & {bin(6)} = {bin(and_5_6)})')

or_5_6 = 5 | 6
print(f'Результат логической побитовой операции «ИЛИ» над числами 5 и 6: число  {or_5_6} '
      f'({bin(5)} | {bin(6)} = {bin(or_5_6)})')

xor_5_6 = 5 ^ 6
print(f'Результат логической побитовой операции «Исключающее ИЛИ» над числами 5 и 6: число  {xor_5_6} '
      f'({bin(5)} | {bin(6)} = {bin(xor_5_6)})')

shl_5 = 5 << 2
print(f'Результат побитового сдвига влево на два знака числа 5 : число {shl_5} ({bin(5)} << 2 = {bin(shl_5)})')

shl_5 = 5 >> 2
print(f'Результат побитового сдвига вправо на два знака числа 5: число {shl_5} ({bin(5)} >> 2 = {bin(shl_5)})')