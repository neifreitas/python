alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 25
alien_1['x_position'] = 10
alien_1['y_position'] = 50

print(alien_1)

alien_1['color'] = 'yellow'

print(alien_1)

del alien_0['points']
print(alien_0)