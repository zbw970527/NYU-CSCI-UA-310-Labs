-- 1.Show the scooter id, company name, when the company was founded,
-- scooter model, weight, max speed, acquired_date, and retired fields for the first 10 scooters in the inventory.
select scooter_id, name, founded, model, weight, max_speed, acquire_date, retired from scooter inner join scooter_type on scooter.scooter_type_id = scooter_type.scooter_type_id inner join company on scooter_type.company_id = company.company_id order by scooter_id limit 10;
-- 2.Show the total number of retired scooters as well as the total number of non-retired scooters.
select retired, count(*) from scooter group by retired;
-- 3.List the number of scooters acquired every month (every year/month combination). Show only the year/months counts that exceed 2.
select to_char(acquire_date, 'YYYY-MM') as month, count(*) from scooter group by month having count(*) > 2 order by month;
-- 4.Count how many scooter types there are for each company by showing the company id and the number of scooter types associated with that company id
select company_id, count(*) from (select distinct company_id, model from scooter_type) as temp group by company_id order by company_id;
