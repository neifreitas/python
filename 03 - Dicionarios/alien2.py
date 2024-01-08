alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x-position: {alien_0['x_position']}")

# Move o alienígena para a direita
# Determina a distância que o alienígena deve se deslocar de acordo com sua velocidade atual

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Este deve ser uma alienígena rápido
    x_increment = 3

# A nova posição é a posição antiga somada ao incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f'First x_position: {alien_0['x_position']} and speed: {alien_0["speed"]}')

alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Este deve ser uma alienígena rápido
    x_increment = 3

# A nova posição é a posição antiga somada ao incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f'Second x_position: {alien_0['x_position']} and speed: {alien_0["speed"]}')