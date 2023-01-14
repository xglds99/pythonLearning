film = {"天下无贼": 40, "战狼": 80}
film_ticket = {}
film_total_price = {}
film_avg_price = {}
for key in film:
    print(key)
    if key in film_ticket:
        film_ticket[key] += 1
    else:
        film_ticket[key] = 1
    if key in film_total_price:
        film_total_price[key] += film[key]
    else:
        film_total_price[key] = film[key]


for film_num in film_ticket:
    film_avg_price[film_num] = film_total_price[film_num] / film_ticket[film_num]

print(film_avg_price)