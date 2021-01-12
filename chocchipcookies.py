from kitchen import Rosemary
from kitchen.utensils import Bowl, BakingTray, Oven, Plate
from kitchen.ingredients import Butter, BakingPowder, Sugar, Egg, ChocolateChips, Salt, Flour

#Preheat the oven 
oven = Oven.use()
Oven.preheat(oven, degrees=175)

#Make cookie dough
bowl = Bowl.use(name='cookie dough')
bowl.add(Butter.take('one part'))
bowl.add(Sugar.take('200g'))
bowl.mix()
for egg in Egg.take(2):
    egg.crack()
    bowl.add(egg)
bowl.mix()
bowl.add(Salt.take('a pinch'))
for flour in Flour.take('300g'):
    bowl.add(Flour.take('1/3'))
    bowl.mix()
for ChocolateChips in ChocolateChips.take('200g'):
    bowl.add(ChocolateChips.take('1/2'))
    bowl.mix()
bowl.add(BakingPowder('a teaspoon'))

#Form cookies 
bakingtray = BakingTray.use(name='cookie tray')
for i in range(8):
    cookie = bowl.take('1/8')
    bakingtray.add(cookie)

#Bake cookies
oven.add(bakingtray)
oven.bake(minutes=10)

tray_with_cookies = oven.take()
cookies = tray_with_cookies.take()
plate = Plate.use()
chocolate_chip_cookies=plate.add(cookies)

Rosemary.serve(plate)


