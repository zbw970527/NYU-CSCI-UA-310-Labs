create table industry(
industry_id serial,
industry_name varchar(255) not null,
primary key(industry_id)
);

create table complaint_type(
type_id serial,
category varchar(255) not null,
primary key (type_id)
);

create table company(
company_id serial,
company_name varchar(255) not null,
company_state varchar(20),
primary key (company_id)
);

create table complaint(
complaint_id serial,
company_id Integer references company(company_id),
industry_id Integer references industry(industry_id),
type_id Integer references complaint_type(type_id),
case_start_date text,
case_resolve_date text,
satisfaction boolean,
primary key (complaint_id)
);

