create table model(
model_id serial,
model_number text not null,
primary key (model_id)
);

create table manufacturer(
manufacturer_id serial,
manufacturer_name varchar(50) not null,
manufacturer_country varchar(50) not null,
primary key (manufacturer_id)
);

create table user_info(
user_id serial,
user_name varchar(100) not null,
phone_number text not null,
email_address text not null,
home_address text,
register_time Date not null,
refer_id Integer,
flag text,
primary key(user_id)
);

create table scooter(
scooter_id serial,
manufacturer_id Integer references manufacturer(manufacturer_id),
model_id Integer references model(model_id),
range Integer,
availability boolean not null default TRUE,
weight Integer,
top_speed Integer,
condition text,
primary key (scooter_id) 
);

create table orders(
order_id serial,
user_id Integer references user_info(user_id),
scooter_id Integer references scooter(scooter_id),
start_time Date not null,
end_time Date not null,
late boolean default FALSE,
money_paid Integer,
additional_charge Integer,
payment_info text,
primary key (order_id)
);

create table damage(
damage_id serial,
damage_type varchar(255) not null,
primary key (damage_id)
);

create table order_damage(
order_id Integer references orders(order_id),
damage_id Integer references damage(damage_id),
primary key (order_id, damage_id)
);