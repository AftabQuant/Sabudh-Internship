-- Customers Table 
create table customers (
customer_id int primary key,
first_name varchar(50) not null,
last_name varchar(50) not null,
email varchar(100) unique not null,
phone varchar(20),
address varchar(200),
city varchar(50),
state varchar(50),
zip_code varchar(20),
registration_date datetime default current_timestamp, loyalty_points int default 0
);

-- Product Category Table
create table productCategories (
category_id int primary key,
category_name varchar(50) not null,
description text,
parent_category_id int,
foreign key (parent_category_id) references productCategories(category_id)
);


