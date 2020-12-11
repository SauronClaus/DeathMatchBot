weaponTierFile = open("weaponTiers.txt", "r")
weaponTierFull = weaponTierFile.read()
weaponTierArray = weaponTierFull.split('\n')
for weaponTier in weaponTierArray: 
    weaponTier1Name = weaponTier + ".txt"
    weaponFile1 = open(weaponTier1Name, "r")
    weaponSet1 = weaponFile1.read().split('\n')
    for weapon in weaponSet1:
        print("Weapon: " + weapon)
        newWeaponFile = open("Armory\\" + weaponTier + "\\" + weapon + ".txt", "w")