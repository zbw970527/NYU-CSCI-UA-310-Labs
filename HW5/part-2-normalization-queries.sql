--show the name of company where they have dissatisfactory record(satisfaction = False).

select company.company_name, company.company_id, complaint.satisfaction from complaint 
inner join company on company.company_id = complaint.company_id where complaint.satisfaction = False;

--show the first 5 most popular complaint type and their name.

select complaint_type.type_id, complaint_type.category, result.count from (select type_id, count(*) from complaint group by type_id) as result 
left join complaint_type on result.type_id = complaint_type.type_id order by result.count desc limit 5;


-- show all the industries (names and their id) and the count of complaints that they receive, form the most to the least

select industry.industry_name, industry.industry_id, result.count from 
(select industry_id, count(*) from complaint group by industry_id) as result 
inner join industry on result.industry_id = industry.industry_id order by result.count desc;