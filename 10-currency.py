# Write code below 💖
pesos=(int(input("What do you have left in pesos: ")))
soles=(int(input("What do you have left in soles: ")))
reais=(int(input("What do you have left in reais: ")))
exchpesos=pesos*0.00025
exchsoles=soles*0.27
exchreais=reais*0.18
usd=exchpesos+exchsoles+exchreais
print(usd)
