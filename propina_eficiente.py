#Imagina que sales a cenar con tus amigos. 
# Al final de la noche, llega la cuenta y quieren calcular cuánta propina dejar 
# dependiendo de qué tan bueno fue el servicio, y cuánto debe pagar cada persona en total.

ticket_total = float(input ("How much the dinner costs?: "))
people = float(input("How many people assists to the dinner?: "))
satisfaction = input("Was the experience good, regular or bad?: ")

if satisfaction == "good":
    propina = 15*ticket_total/100
elif satisfaction == "regular":
    propina = 10*ticket_total/100
elif satisfaction == "bad":
    propina = 5*ticket_total/100
    
people_price = (propina + ticket_total)/people
print(f"Everyone have to pay {people_price}€")
    