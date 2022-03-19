select name from Пилоты WHERE
(count * from Рейсы where Пилоты.pilot_id = Рейсы.second_pilot_id 
 and destination = 'Шереметьево' and flight_dt BETWEEN '2021-08-01' and '2021-08-31') = 3