from source_data import MENU
from source_data import resources

# ==Základní fce==
espreso_cena = MENU['espresso']['cost']
late_cena = MENU['latte']['cost']
capucino_cena = MENU['cappuccino']['cost']

# == fce ==
def report(data):
    for položka in data:
        print(f'{položka}: {data[položka]}')
def mince():
    print('Prosím vložte mince 1, 2, 5, 10, 20, 50')
    peníze = 0
    peníze += int(input('1kč:'))*1
    peníze += int(input('2kč:'))*2
    peníze += int(input('5kč:'))*5
    peníze += int(input('10kč:'))*10
    peníze += int(input('20kč:'))*20
    peníze += int(input('50kč:'))*50
    print(f'Vložils {peníze} kč')
    return peníze
    

# ==Kód automatu==
user_choice = input('What would you like?' + '\n' + 'espresso/latte/cappuccino: ')

if user_choice == 'report':
    report(resources)

if user_choice == 'espresso':
    print(f' Zbylo ti {mince()-espreso_cena}')
elif user_choice == 'latte':
    print(f' Zbylo ti {mince()-late_cena}')
elif user_choice == 'cappuccino':
    print(f' Zbylo ti {mince()-capucino_cena}')
