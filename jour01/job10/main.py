montant_initial_investissement= 1000
taux_rendement_annuel= 0.1

gain= montant_initial_investissement * taux_rendement_annuel 
print (gain)

montant_initial_investissement += gain

print (f'montant total: {montant_initial_investissement}€')


insvestissement_capital= 5000

augmentation_taux_annuel= 0.02

montant_initial_investissement += insvestissement_capital
print ( f'montant tolal capital: {montant_initial_investissement} €' )

taux_rendement_annuel += augmentation_taux_annuel

gain= montant_initial_investissement * taux_rendement_annuel
print (f'montant gain final :{gain}€')

montant_initial_investissement += gain 
print (f' montant total :{montant_initial_investissement}€' )

retrait= 0.9

montant_initial_investissement *= retrait

print (f'montant avec retrait capital : {montant_initial_investissement} €')

baisse_taux_annuel = 0.01

taux_rendement_annuel -= baisse_taux_annuel

gain= montant_initial_investissement * taux_rendement_annuel
montant_initial_investissement += gain
print (f'montant gain final: {gain} € montant final capital : {montant_initial_investissement} €')