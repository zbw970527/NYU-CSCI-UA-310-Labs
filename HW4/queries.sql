-- write your queries underneath each number:
 
-- 1. the total number of rows in the database
select count(*) as exact_count from  complaint_data;

-- 2. show the first 15 rows, but only display 3 columns (your choice)
select industry, complaint_result, business_city from complaint_data limit 15;

-- 3. do the same as above, but chose a column to sort on, and sort in descending order
select industry, complaint_result, business_city from complaint_data order by industry desc limit 15;

-- 4. add a new column without a default value
alter table complaint_data add column new_col varchar(255);

-- 5. set the value of that new column
update complaint_data set new_col = 'set values!';

-- 6. show only the unique (non duplicates) of a column of your choice
select distinct industry from complaint_data;

-- 7.group rows together by a column value (your choice) and use an aggregate function to calculate something about that group 
select complaint_result, count(*) from complaint_data group by complaint_result;

-- 8. now, using the same grouping query or creating another one, find a way to filter the query results based on the values for the groups
select complaint_result, count(*) from complaint_data group by complaint_result having count(*) > 300;

-- 9. find numbers of satisfied complaint in NY area
select satisfaction, count(*) from complaint_data where business_state = 'NY' group by satisfaction;

-- 10. show first five states which receive most complaints. 
select business_state, count(*) from complaint_data group by business_state order by count(*) desc limit 5;

-- 11. find the least 10 complainted industry in NY state.
select industry, count(*) from complaint_data where business_state = 'NY' group by industry order by count(*) asc limit 10;

-- 12. what are the first 5 complaint result in industry "Home Improvement Contractor - 100"
select complaint_result, count(*) from complaint_data where industry = 'Home Improvement Contractor - 100' group by complaint_result order by count(*) desc limit 5;
