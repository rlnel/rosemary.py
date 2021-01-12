from kitchen import Rosemary
from kitchen.ingredients import Flour, Egg, Salt, Butter, Milk 
from kitchen.utensils import Bowl, Pan, Plate

#Whisk eggs
bowl=Bowl.use(name='batter')
for egg in Egg.take(2):
    egg.crack()
    bowl.add(egg)
bowl.mix()
bowl.add(Salt.take('dash'))

#Add milk
for milk in Milk.take('500ml'): 
    bowl.add(Milk.take('1/2'))
    bowl.mix()

#Add flour 
for flour in Flour.take('250g'):
    bowl.add(Flour.take('1/5'))
    bowl.mix()

pan = Pan.use(name='pancakes')
pan.add(Butter.take('slice'))
plate = Plate.use()
for i in range(8):
    pan.add(bowl.take('1/8')) 
    pan.cook(minutes=1)
    pan.flip()
    pan.cook(minutes=1)

    pancake = pan.take()
    plate.add(pancake)

Rosemary.serve(plate)

