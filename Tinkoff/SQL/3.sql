select top(10) name 
from Пилоты 
    left join Рейсы 
        on Пилоты.pilot_id = Рейсы.first_pilot_id 
    left join Самолёты 
        on Рейсы.plane_id = Самолёты.plane_id 
where  Самолёты.cargo_flg = 1
group by name 
order by count(Самолеты.capacity) desc