--List all people (names are adequate) that have flags in any order
select * from user where flag IS NOT NULL;

--List all available scooters in any order
select * from scooter where availability = TRUE;

--List all scooters (scooter model and manufacturer, along with person's name¡­ and when they're due back) that are being borrowed in order of when they're due back ordered by when whey were due increasing (that is, earlier ones appear first, and more recent ones appear later)
select scooter.scooter_id, manufacturer.manufacturer_name, model.model_number, user_info.user_name, orders.end_time from scooter inner join manufacturer on manufacturer.manufacturer_id = scooter.manufacturer_id inner join model on model.model_id = scooter.model_id inner join orders on orders.scooter_id = scooter.scooter_id inner join user_info on orders.user_id = user_info.user_id where scooter.availability = FALSE order by end_time;

--List all scooters (scooter model and manufacturer, along with person's name) that are being borrowed and that are late in any order
select scooter.scooter_id, manufacturer.manufacturer_name, model.model_number, user_info.user_name, orders.end_time from scooter inner join manufacturer on manufacturer.manufacturer_id = scooter.manufacturer_id inner join model on model.model_id = scooter.model_id inner join orders on orders.scooter_id = scooter.scooter_id inner join user_info on orders.user_id = user_info.user_id where scooter.availability = FALSE and scooter.late = TRUE;

--List the top 5 people (names and number of referrals) that have the most referrals sorted by most referrals descending
select user_info.name, user_info.user_id, result.count from (select refer_id, count(*) from user_info where refer_id is not null group by refer_id) as result left join user_info on result.refer_id = user_info.user_id order by result.count desc;
                                                                                                                                                                                                                                                                                                                                                                                                           
--Given a unique identifier for a person, show all of the times that person has borrowed a scooter in chronological order (from the first time they borrowed a scooter to the most recent)
select * from orders where user_id = (some specified value) order by start_time;

--Given a unique identifier for a particular instance of a person borrowing a scooter, show all of the damage / late related fees
select order_id, additional_charge from orders where order_id = (some specified value);

--List all of the manufacturers of scooters in your database, even if you don't currently have any of their scooters in your inventory
select * from manufacturer;
