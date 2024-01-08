favorite_languagens = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
}

# Quebra de linha de código no print
print("Sarah's favorite languages is " +
      f"{favorite_languagens['sarah'].title()}\n")

for name, language in favorite_languagens.items():
    print(f"{name.title()}'s favorite language is {language.title()}.\n")

for name in favorite_languagens.keys():
    print(f"{name.title()}.\n")
    
# Podemos omitir o método keys
for name in favorite_languagens:
    print(f"{name.title()}.\n")
    

friends = ['phil', 'sarah']
for name in favorite_languagens.keys():
    print(f"{name.title()}.")
    if name in friends:
        print(f" Hi {name.title()}, I see your favorite language is {favorite_languagens[name].title()}")

if 'erin' not in favorite_languagens.keys():
    print("Erin, please take our poll!")
    
for name in sorted(favorite_languagens.keys()):
    print(f"{name.title()}, thank you for taking the poll!")

# Recuperando os dados sem repetição
for language in set(favorite_languagens.values()):
    print(language)
