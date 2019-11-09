-- write your sql code here

CREATE DATABASE homework04;

-- test drop table:
CREATE TABLE HUAQ(
 name varchar(255),
 age real
);

DROP TABLE HUAQ;

CREATE TABLE complaint_data(
  industry varchar(255),
  complaint_type varchar(255),
  mediation_start_Date varchar(255),
  mediation_close_Date varchar(255),
  complaint_result varchar(255),
  satisfaction boolean,
  business_city varchar(255),
  business_state varchar(255)
  );

ALTER TABLE complaint_data ADD COLUMN id SERIAL PRIMARY KEY;

