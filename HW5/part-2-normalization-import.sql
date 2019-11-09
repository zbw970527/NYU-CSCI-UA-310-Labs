-- I created a scratch table to get original csv

create table scratch(
company_name varchar(255),
industry_name varchar(255),
category varchar(255),
case_start_date text,
case_resolve_date text,
result_type text,
satisfaction boolean,
company_state varchar(20)
);

-- import from industry.csv to table industry

copy industry from 'd:/nyu/data/industry.csv' delimiter ',';

-- import from complaint_type.csv to table complaint_type

copy complaint_type from 'd:/nyu/data/complaint_type.csv' delimiter ',';

-- import from table scratch to table company

insert into company (company_name, company_state) select distinct company_name, company_state from scratch;

-- import data from scratch and other tables into complaint

insert into complaint (company_id, industry_id, type_id, case_start_date, case_resolve_date, satisfaction) 
select company.company_id, industry.industry_id, complaint_type.type_id, scratch.case_start_date, scratch.case_resolve_date, scratch.satisfaction from scratch 
left join company on company.company_name = scratch.company_name and company.company_state = scratch.company_state 
left join complaint_type on complaint_type.category = scratch.category 
left join industry on industry.industry_name = scratch.industry_name;


