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

-- Products Table
create table products(
product_id int primary key,
product_name varchar(100) not null,
description text,
category_id int,
price decimal(10, 2) not null,
stock_quantity int default 0,
manufacturer varchar(100),
release_date date,
is_active boolean default true,
foreign key (category_id) references productCategories(category_id)
); 

-- Orders table
create table orders (
order_id int primary key,
customer_id int,
order_date datetime default current_timestamp,
total_amount decimal(12, 2) not null,
shipping_address varchar(200),
shipping_city varchar(50),
shipping_state varchar(50),
shipping_zip_code varchar(20),
status varchar(50) default 'Pending',
payment_method varchar(50),
foreign key (customer_id) references customers(customer_id)
);

-- Order Items table 
create table orderItems (
order_item_id int primary key,
order_id int,
product_id int,
quantity int not null,
unit_price decimal(10, 2) not null,
discount decimal(10, 2) default 0.00,
foreign key (order_id) references orders(order_id),
foreign key (product_id) references products(product_id)
);

-- Employees table
create table employees (
employee_id int primary key,
first_name varchar(50) not null,
last_name varchar(50) NOT null,
email varchar(100) unique not null,
phone varchar(20),
hire_date date not null,
job_title varchar(100),
department varchar(100),
manager_id int,
salary decimal(10, 2),
foreign key (manager_id) references employees(employee_id)
);

-- Reviews table
create table reviews (
review_id int primary key,
product_id int,
customer_id int,
rating int check (rating between 1 and 5),
comment text,
review_date datetime default current_timestamp,
foreign key (product_id) references products(product_id),
foreign key (customer_id) references customers(customer_id)
);

-- Promotions table
create table promotions (
promotion_id int primary key,
promotion_name varchar(100) not null,
description text,
discount_percentage decimal(5, 2),
start_date date not null,
end_date date not null,
is_active boolean default true
);

-- Product Promotions mapping 
create table productPromotions (
product_id int,
promotion_id int,
primary key (product_id, promotion_id),
foreign key (product_id) references products(product_id),
foreign key (promotion_id) references promotions(promotion_id)
);

-- Insert data into Customers table
insert into customers (customer_id, first_name, last_name, email, phone,
address, city, state, zip_code, registration_date, loyalty_points)
values
(1, 'John', 'Smith', 'john.smith@email.com', '555-123-4567', '123 Main St', 'Austin', 'TX', '78701',
'2023-01-15', 250),(2, 'Emma', 'Johnson', 'emma.j@email.com', '555-234-5678', '456 Elm St', 'Seattle', 'WA', '98101',
'2023-02-20', 175),
(3, 'Michael', 'Williams', 'michael.w@email.com', '555-345-6789', '789 Oak Ave', 'Chicago', 'IL', '60601',
'2023-03-10', 320),
(4, 'Sophia', 'Brown', 'sophia.b@email.com', '555-456-7890', '101 Pine Rd', 'New York', 'NY', '10001',
'2023-04-05', 100),
(5, 'Robert', 'Jones', 'robert.j@email.com', '555-567-8901', '202 Maple Dr', 'Los Angeles', 'CA', '90001',
'2023-04-12', 280),
(6, 'Olivia', 'Garcia', 'olivia.g@email.com', '555-678-9012', '303 Birch Ln', 'Miami', 'FL', '33101',
'2023-05-18', 150),
(7, 'William', 'Miller', 'william.m@email.com', '555-789-0123', '404 Cedar Ct', 'Denver', 'CO', '80201',
'2023-06-22', 90),
(8, 'Ava', 'Davis', 'ava.d@email.com', '555-890-1234', '505 Walnut Pl', 'Portland', 'OR', '97201',
'2023-07-14', 210),
(9, 'James', 'Rodriguez', 'james.r@email.com', '555-901-2345', '606 Spruce Way', 'Boston', 'MA',
'02101', '2023-08-08', 170),
(10, 'Isabella', 'Martinez', 'isabella.m@email.com', '555-012-3456', '707 Fir Blvd', 'Phoenix', 'AZ',
'85001', '2023-09-19', 300),
(11, 'David', 'Anderson', 'david.a@email.com', '555-321-7654', '808 Cypress St', 'San Francisco', 'CA',
'94101', '2024-01-10', 220),
(12, 'Mia', 'Taylor', 'mia.t@email.com', '555-432-8765', '909 Redwood Dr', 'Atlanta', 'GA', '30301',
'2024-02-05', 180);









