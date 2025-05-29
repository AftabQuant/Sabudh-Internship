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
(1, 'John', 'Smith', 'john.smith@email.com', '555-123-4567', '123 Main St', 'Austin', 'TX', '78701','2023-01-15', 250),
(2, 'Emma', 'Johnson', 'emma.j@email.com', '555-234-5678', '456 Elm St', 'Seattle', 'WA', '98101','2023-02-20', 175),
(3, 'Michael', 'Williams', 'michael.w@email.com', '555-345-6789', '789 Oak Ave', 'Chicago', 'IL', '60601','2023-03-10', 320),
(4, 'Sophia', 'Brown', 'sophia.b@email.com', '555-456-7890', '101 Pine Rd', 'New York', 'NY', '10001','2023-04-05', 100),
(5, 'Robert', 'Jones', 'robert.j@email.com', '555-567-8901', '202 Maple Dr', 'Los Angeles', 'CA', '90001','2023-04-12', 280),
(6, 'Olivia', 'Garcia', 'olivia.g@email.com', '555-678-9012', '303 Birch Ln', 'Miami', 'FL', '33101','2023-05-18', 150),
(7, 'William', 'Miller', 'william.m@email.com', '555-789-0123', '404 Cedar Ct', 'Denver', 'CO', '80201','2023-06-22', 90),
(8, 'Ava', 'Davis', 'ava.d@email.com', '555-890-1234', '505 Walnut Pl', 'Portland', 'OR', '97201','2023-07-14', 210),
(9, 'James', 'Rodriguez', 'james.r@email.com', '555-901-2345', '606 Spruce Way', 'Boston', 'MA','02101', '2023-08-08', 170),
(10, 'Isabella', 'Martinez', 'isabella.m@email.com', '555-012-3456', '707 Fir Blvd', 'Phoenix', 'AZ','85001', '2023-09-19', 300),
(11, 'David', 'Anderson', 'david.a@email.com', '555-321-7654', '808 Cypress St', 'San Francisco', 'CA','94101', '2024-01-10', 220),
(12, 'Mia', 'Taylor', 'mia.t@email.com', '555-432-8765', '909 Redwood Dr', 'Atlanta', 'GA', '30301','2024-02-05', 180);

-- Insert data into ProductCategories table
insert into productCategories (category_id, category_name, description,
parent_category_id)
values
(1, 'Electronics', 'Electronic devices and accessories', null),
(2, 'Computers', 'Desktop and laptop computers', 1),
(3, 'Smartphones', 'Mobile phones and accessories', 1),
(4, 'Audio', 'Headphones, speakers, and audio equipment', 1),(5, 'Gaming', 'Video games and gaming equipment', null),
(6, 'Consoles', 'Gaming consoles and accessories', 5),
(7, 'PC Gaming', 'PC gaming hardware and accessories', 5),
(8, 'Home Appliances', 'Household electronic appliances', null),
(9, 'Kitchen', 'Kitchen appliances and equipment', 8);

-- Insert data into Products table
insert into products (product_id, product_name, description, category_id,
price, stock_quantity, manufacturer, release_date, is_active)
values
(101, 'UltraBook Pro', '15-inch laptop with high performance', 2, 1299.99, 50, 'TechCorp', '2023-03-15',true),
(102, 'SmartPhone X', 'Latest smartphone with advanced features', 3, 899.99, 120, 'MobiTech','2023-05-20', true),
(103, 'Noise Cancelling Headphones', 'Premium headphones with noise cancellation', 4, 249.99, 85,'AudioMax', '2023-02-10', true),
(104, 'Gaming Console Pro', 'Next-gen gaming console', 6, 499.99, 30, 'GameTech', '2023-11-05',true),
(105, 'Smart Watch', 'Fitness and notification tracker', 1, 199.99, 75, 'MobiTech', '2023-07-14', true),
(106, 'Bluetooth Speaker', 'Portable bluetooth speaker with 20hr battery', 4, 129.99, 60, 'AudioMax','2023-08-22', true),
(107, 'Desktop Computer', 'High-performance desktop for professionals', 2, 1599.99, 25, 'TechCorp','2023-09-30', true),
(108, 'Tablet Pro', '12-inch tablet with stylus support', 1, 699.99, 40, 'MobiTech', '2023-10-15', true),
(109, 'Wireless Gaming Mouse', 'High precision gaming mouse', 7, 89.99, 100, 'GameTech','2023-04-18', true),
(110, 'Coffee Maker', 'Programmable coffee maker with timer', 9, 149.99, 35, 'HomeElectronics','2023-06-25', true),
(111, 'Microwave Oven', 'Digital microwave with multiple cooking modes', 9, 179.99, 30,'HomeElectronics', '2023-07-05', true),
(112, 'Gaming Keyboard', 'Mechanical RGB gaming keyboard', 7, 129.99, 45, 'GameTech', '2023-08-10',true),
(113, 'Wireless Earbuds', 'True wireless earbuds with charging case', 4, 159.99, 90, 'AudioMax','2023-09-18', true),
(114, 'External Hard Drive', '2TB portable external hard drive', 2, 119.99, 70, 'DataStore', '2023-05-28',true),
(115, 'Smartphone Y', 'Mid-range smartphone with excellent camera', 3, 599.99, 65, 'MobiTech','2023-10-25', true),
(116, 'Ultra HD Monitor', '27-inch 4K monitor for professionals', 2, 349.99, 55, 'ViewTech','2023-11-15', true),
(117, 'Smart Blender', 'Programmable blender with multiple speeds', 9, 89.99, 40, 'HomeElectronics','2023-12-10', false),
(118, 'Gaming Headset', 'Surround sound gaming headset with mic', 7, 149.99, 60, 'GameTech','2024-01-05', true),
(119, 'Wireless Router', 'High-speed dual-band wireless router', 1, 129.99, 50, 'NetConnect','2024-02-12', true),
(120, 'Portable Power Bank', '20000mAh fast charging power bank', 3, 49.99, 80, 'PowerTech','2024-03-20', true);

-- Insert data into Orders table
insert into orders (order_id, customer_id, order_date, total_amount,
shipping_address, shipping_city, shipping_state, shipping_zip_code,
status, payment_method)
values
(1001, 1, '2023-05-10 14:30:00', 1549.98, '123 Main St', 'Austin', 'TX', '78701', 'Delivered', 'Credit Card'),
(1002, 2, '2023-05-15 10:15:00', 899.99, '456 Elm St', 'Seattle', 'WA', '98101', 'Delivered', 'PayPal'),
(1003, 3, '2023-06-02 09:45:00', 379.98, '789 Oak Ave', 'Chicago', 'IL', '60601', 'Delivered', 'Credit Card'),
(1004, 4, '2023-06-10 16:20:00', 499.99, '101 Pine Rd', 'New York', 'NY', '10001', 'Delivered', 'Debit Card'),
(1005, 5, '2023-07-05 11:30:00', 329.98, '202 Maple Dr', 'Los Angeles', 'CA', '90001', 'Delivered', 'Credit Card'),
(1006, 1, '2023-07-20 14:45:00', 699.99, '123 Main St', 'Austin', 'TX', '78701', 'Delivered', 'Credit Card'),
(1007, 6, '2023-08-08 13:10:00', 449.98, '303 Birch Ln', 'Miami', 'FL', '33101', 'Delivered', 'PayPal'),
(1008, 7, '2023-08-25 15:25:00', 1599.99, '404 Cedar Ct', 'Denver', 'CO', '80201', 'Shipped', 'Credit Card'),
(1009, 8, '2023-09-12 10:05:00', 249.99, '505 Walnut Pl', 'Portland', 'OR', '97201', 'Delivered', 'Debit Card'),
(1010, 9, '2023-09-30 17:40:00', 219.98, '606 Spruce Way', 'Boston', 'MA', '02101', 'Delivered', 'Credit Card'),
(1011, 10, '2023-10-15 09:30:00', 1099.98, '707 Fir Blvd', 'Phoenix', 'AZ', '85001', 'Shipped', 'PayPal'),
(1012, 11, '2023-11-05 14:15:00', 679.97, '808 Cypress St', 'San Francisco', 'CA', '94101', 'Processing','Credit Card'),
(1013, 12, '2023-11-20 11:50:00', 279.98, '909 Redwood Dr', 'Atlanta', 'GA', '30301', 'Shipped', 'Debit Card'),
(1014, 3, '2023-12-10 16:05:00', 849.98, '789 Oak Ave', 'Chicago', 'IL', '60601', 'Delivered', 'Credit Card'),
(1015, 5, '2023-12-28 13:40:00', 399.98, '202 Maple Dr', 'Los Angeles', 'CA', '90001', 'Delivered','PayPal'),
(1016, 2, '2024-01-15 10:25:00', 1129.98, '456 Elm St', 'Seattle', 'WA', '98101', 'Shipped', 'Credit Card'),
(1017, 8, '2024-02-02 15:10:00', 459.98, '505 Walnut Pl', 'Portland', 'OR', '97201', 'Processing', 'Debit Card'),
(1018, 1, '2024-02-20 09:55:00', 349.99, '123 Main St', 'Austin', 'TX', '78701', 'Processing', 'Credit Card'),
(1019, 4, '2024-03-08 12:30:00', 279.98, '101 Pine Rd', 'New York', 'NY', '10001', 'Pending', 'PayPal'),
(1020, 6, '2024-03-25 14:20:00', 549.98, '303 Birch Ln', 'Miami', 'FL', '33101', 'Pending', 'Credit Card');

-- Insert data into OrderItems table
insert into orderItems (order_item_id, order_id, product_id, quantity, unit_price, discount)
values
(2001, 1001, 101, 1, 1299.99, 0.00),
(2002, 1001, 103, 1, 249.99, 0.00),
(2003, 1002, 102, 1, 899.99, 0.00),
(2004, 1003, 103, 1, 249.99, 0.00),
(2005, 1003, 106, 1, 129.99, 0.00),
(2006, 1004, 104, 1, 499.99, 0.00),
(2007, 1005, 105, 1, 199.99, 0.00),
(2008, 1005, 106, 1, 129.99, 0.00),
(2009, 1006, 108, 1, 699.99, 0.00),
(2010, 1007, 109, 1, 89.99, 0.00),
(2011, 1007, 113, 1, 159.99, 0.00),
(2012, 1007, 110, 1, 149.99, 0.00),
(2013, 1008, 107, 1, 1599.99, 0.00),
(2014, 1009, 103, 1, 249.99, 0.00),
(2015, 1010, 109, 1, 89.99, 0.00),
(2016, 1010, 120, 1, 49.99, 0.00),
(2017, 1010, 114, 1, 119.99, 40.00),
(2018, 1011, 115, 1, 599.99, 0.00),
(2019, 1011, 116, 1, 349.99, 0.00),
(2020, 1011, 119, 1, 129.99, 0.00),
(2021, 1012, 118, 1, 149.99, 0.00),
(2022, 1012, 116, 1, 349.99, 0.00),
(2023, 1012, 120, 2, 49.99, 0.00),
(2024, 1013, 113, 1, 159.99, 0.00),
(2025, 1013, 120, 1, 49.99, 0.00),
(2026, 1013, 109, 1, 89.99, 20.00),
(2027, 1014, 102, 1, 899.99, 50.00),
(2028, 1015, 110, 1, 149.99, 0.00),
(2029, 1015, 111, 1, 179.99, 0.00),
(2030, 1015, 120, 1, 49.99, 0.00),
(2031, 1016, 101, 1, 1299.99, 200.00),
(2032, 1016, 109, 1, 89.99, 0.00),
(2033, 1016, 120, 1, 49.99, 0.00),
(2034, 1017, 118, 1, 149.99, 0.00),
(2035, 1017, 113, 1, 159.99, 0.00),
(2036, 1017, 120, 3, 49.99, 0.00),
(2037, 1018, 116, 1, 349.99, 0.00),
(2038, 1019, 113, 1, 159.99, 0.00),
(2039, 1019, 120, 1, 49.99, 0.00),
(2040, 1019, 106, 1, 129.99, 60.00),
(2041, 1020, 104, 1, 499.99, 0.00),
(2042, 1020, 120, 1, 49.99, 0.00);

-- Insert data into Employees table
insert into employees (employee_id, first_name, last_name, email, phone, hire_date, job_title, department, manager_id, salary)
values
(501, 'Thomas', 'Wilson', 'thomas.w@techmart.com', '555-111-2222', '2022-01-15', 'CEO', 'Executive',null, 250000.00),
(502, 'Sarah', 'Johnson', 'sarah.j@techmart.com', '555-222-3333', '2022-02-20', 'CTO', 'Executive', 501,200000.00),
(503, 'Daniel', 'Brown', 'daniel.b@techmart.com', '555-333-4444', '2022-03-10', 'CFO', 'Executive', 501,200000.00),
(504, 'Jessica', 'Smith', 'jessica.s@techmart.com', '555-444-5555', '2022-04-05', 'IT Manager', 'IT', 502,120000.00),
(505, 'Andrew', 'Davis', 'andrew.d@techmart.com', '555-555-6666', '2022-05-12', 'Sales Manager','Sales', 501, 110000.00),
(506, 'Lisa', 'Miller', 'lisa.m@techmart.com', '555-666-7777', '2022-06-18', 'Marketing Manager','Marketing', 501, 110000.00),
(507, 'Robert', 'Taylor', 'robert.t@techmart.com', '555-777-8888', '2022-07-22', 'HR Manager', 'HR',501, 105000.00),
(508, 'Emily', 'Anderson', 'emily.a@techmart.com', '555-888-9999', '2022-08-14', 'IT Specialist', 'IT',504, 85000.00),
(509, 'Michael', 'Clark', 'michael.c@techmart.com', '555-999-0000', '2022-09-08', 'IT Specialist', 'IT',504, 85000.00),
(510, 'Amanda', 'Wright', 'amanda.w@techmart.com', '555-000-1111', '2022-10-19', 'SalesRepresentative', 'Sales', 505, 65000.00),
(511, 'Joshua', 'Garcia', 'joshua.g@techmart.com', '555-111-3333', '2022-11-10', 'Sales Representative','Sales', 505, 65000.00),
(512, 'Melissa', 'Martinez', 'melissa.m@techmart.com', '555-222-4444', '2022-12-05', 'MarketingSpecialist', 'Marketing', 506, 70000.00),
(513, 'Christopher', 'Lee', 'christopher.l@techmart.com', '555-333-5555', '2023-01-15', 'HR Specialist','HR', 507, 65000.00),
(514, 'Nicole', 'Harris', 'nicole.h@techmart.com', '555-444-6666', '2023-02-20', 'IT Support', 'IT', 504,60000.00),
(515, 'Brian', 'Young', 'brian.y@techmart.com', '555-555-7777', '2023-03-18', 'Sales Representative','Sales', 505, 65000.00);

-- Insert data into Reviews table
insert into reviews (review_id, product_id, customer_id, rating, comment, review_date)
values
(3001, 101, 1, 5, 'Excellent laptop, very fast and reliable', '2023-05-20 15:30:00'),
(3002, 102, 2, 4, 'Great phone but battery life could be better', '2023-05-25 10:45:00'),
(3003, 103, 3, 5, 'Amazing sound quality, best headphones I\'ve owned', '2023-06-10 09:20:00'),
(3004, 104, 4, 3, 'Good console but lacks some features compared to competitors', '2023-06-18 14:10:00'),
(3005, 105, 5, 4, 'Nice smart watch, tracks fitness well', '2023-07-12 11:25:00'),
(3006, 106, 6, 5, 'Incredible sound for such a small speaker', '2023-07-28 16:40:00'),
(3007, 107, 7, 4, 'Powerful desktop, great for my work needs', '2023-09-05 13:15:00'),
(3008, 108, 8, 5, 'The tablet is perfect for my design work', '2023-09-20 10:30:00'),
(3009, 109, 9, 4, 'Responsive gaming mouse, comfortable to use', '2023-10-08 17:50:00'),
(3010, 110, 10, 5, 'Makes great coffee and easy to program', '2023-10-25 09:10:00'),
(3011, 111, 11, 3, 'Works well but a bit noisy', '2023-11-12 12:45:00'),
(3012, 112, 12, 5, 'Keys feel great, RGB lighting is awesome', '2023-11-30 15:20:00'),
(3013, 113, 1, 4, 'Good sound quality but fit is a bit loose', '2023-12-15 14:35:00'),
(3014, 101, 3, 4, 'Good performance but runs hot under heavy load', '2023-12-28 11:55:00'),
(3015, 102, 5, 5, 'Camera quality is exceptional!', '2024-01-10 10:15:00'),
(3016, 104, 7, 4, 'Great gaming experience', '2024-01-25 16:30:00'),
(3017, 105, 9, 3, 'Battery life is shorter than advertised', '2024-02-08 13:40:00'),
(3018, 108, 11, 5, 'Perfect for both work and entertainment', '2024-02-22 09:25:00'),
(3019, 113, 2, 4, 'Sound quality is great, battery life could be better', '2024-03-10 14:50:00'),
(3020, 116, 4, 5, 'Amazing display quality, perfect for my graphic design work', '2024-03-28 11:05:00');

-- Insert data into Promotions table
insert into promotions (promotion_id, promotion_name, description, discount_percentage, start_date, end_date, is_active)
values
(401, 'Summer Sale', 'Annual summer discount event', 15.00, '2023-06-01', '2023-06-30', false),
(402, 'Back to School', 'Discounts on electronics for students', 10.00, '2023-08-01', '2023-08-31',false),
(403, 'Black Friday', 'Biggest sale of the year', 25.00, '2023-11-24', '2023-11-27', false),
(404, 'Holiday Season', 'End of year holiday promotions', 20.00, '2023-12-15', '2023-12-31', false),
(405, 'New Year Sale', 'Start the year with savings', 15.00, '2024-01-01', '2024-01-15', false),
(406, 'Winter Clearance', 'Clearing inventory for new products', 30.00, '2024-02-01', '2024-02-28',false),
(407, 'Spring Tech Fest', 'Discounts on latest technology products', 12.00, '2024-03-15', '2024-04-15',true);

-- Insert data into ProductPromotions table
insert into productPromotions (product_id, promotion_id)
values
(101, 402), -- UltraBook Pro in Back to School promotion
(102, 401), -- SmartPhone X in Summer Sale
(103, 401), -- Noise Cancelling Headphones in Summer Sale
(104, 403), -- Gaming Console Pro in Black Friday
(105, 401), -- Smart Watch in Summer Sale
(106, 402), -- Bluetooth Speaker in Back to School
(107, 403), -- Desktop Computer in Black Friday
(108, 404), -- Tablet Pro in Holiday Season
(109, 402), -- Wireless Gaming Mouse in Back to School
(110, 404), -- Coffee Maker in Holiday Season
(111, 405), -- Microwave Oven in New Year Sale
(112, 403), -- Gaming Keyboard in Black Friday
(113, 402), -- Wireless Earbuds in Back to School
(114, 401), -- External Hard Drive in Summer Sale
(115, 404), -- Smartphone Y in Holiday Season
(116, 405), -- Ultra HD Monitor in New Year Sale
(118, 406), -- Gaming Headset in Winter Clearance
(119, 406), -- Wireless Router in Winter Clearance
(120, 407), -- Portable Power Bank in Spring Tech Fest(101, 407), -- UltraBook Pro in Spring Tech Fest
(102, 407), -- SmartPhone X in Spring Tech Fest
(103, 407), -- Noise Cancelling Headphones in Spring Tech Fest
(104, 407); -- Gaming Console Pro in Spring Tech Fest

-- SQL Challenges

alter table customers
add column full_name varchar(30) not null;

update customers
set customers.full_name = concat(first_name, " ", last_name);


-- 1. Display all products that cost more than $500 and have at least 50 items in stock, sorted by price from highest to lowest.
select * from products where
price > 500 and stock_quantity >= 50
order by price desc;

-- 2. Find all customers who have registered in 2023 and have more than 200 loyalty points. Show their full name as a single column, email, and city. 
select concat(first_name, " ", last_name) as full_name, email, city from customers
where year(registration_date) = '2023' and loyalty_points > 200;

-- 3. Update the loyalty points for customers in Texas by adding 50 points to their current total.
SET SQL_SAFE_UPDATES = 0;
update customers 
set loyalty_points = loyalty_points + 50;

select * from customers;

-- 4. Create a query to identify products that need restocking (stock_quantity less than 30).
select product_name, stock_quantity from products 
where products.stock_quantity <= 30;

-- 5. Calculate the average price of products in each category, but only include categories where the average price is greater than $200. 
select productcategories.category_name, avg(products.price) as avg_price from productcategories
join products
on productcategories.category_id = products.category_id
group by productcategories.category_name
having avg_price >= 200;

-- 6. Find all customers who haven't placed any orders yet.
select customers.first_name, count(orders.order_id) as total_order from customers
left join orders
on customers.customer_id = orders.customer_id
group by customers.first_name
having  total_order is null;

-- 7. Display the top 5 customers who have spent the most money on purchases, showing their name and total amount spent. 
select customers.full_name, sum(orders.total_amount) as total_amount from customers
join orders
on customers.customer_id = orders.customer_id
group by customers.full_name
order by total_amount desc limit 5;

-- 8. For each product, show its name, price, and the average rating it has received.
select products.product_name, products.price, avg(reviews.rating) as avg_rating from products
left join
reviews 
on products.product_id = reviews.product_id
group by products.product_name, products.price
order by avg_rating desc;

-- 9. Find all products that were ordered in February 2024, along with the customers who ordered them. 
select customers.full_name, products.product_name, orders.order_date from products
join orderitems
on products.product_id = orderitems.product_id
join orders
on orderitems.order_id = orders.order_id                                                                                                                                                                           
join customers
on customers.customer_id = orders.customer_id
where year(orders.order_date) = '2024' and month(orders.order_date) = 2;

-- 10. List all employees along with their direct manager's name (if they have one). 
select concat(employees.first_name, " ", employess.last_name) from employees
where count(employees.manager_id) > 0;

-- 11. Find all products that have never been reviewed by any customer.
select products.product_id, products.product_name, count(reviews.review_id) as review from products
left join reviews
on products.product_id = reviews.product_id
group by products.product_id, products.product_name
having review = 0;

-- 12. Identify customers who have purchased products from at least 3 different product categories.
select customers.full_name, count(productcategories.category_id) as category from customers
left join orders on customers.customer_id = orders.customer_id
join orderitems on orders.order_id = orderitems.order_id
join products on orderitems.product_id = products.product_id
join productcategories on products.category_id = productcategories.category_id
group by customers.full_name
having   category >= 3
order by category desc;

-- 13. Find all products that are not currently part of any active promotion.
select products.product_id, products.product_name, promotions.is_active from products
left join productpromotions
on products.product_id = productpromotions.product_id
join promotions
on productpromotions.promotion_id = promotions.promotion_id
where promotions.is_active = 0; 

-- 14. List customers who have purchased the same product more than once across different orders.
select customers.full_name, count(distinct orders.order_id) as total_order from customers
join orders on customers.customer_id = orders.customer_id
group by customers.full_name
having total_order >=1
order by total_order desc;

-- 15. Find departments with more than 3 employees, showing the department name and the number of employees.  
select employees.department, count(employees.employee_id) as total_employee from employees
group by employees.department
having total_employee >= 3
order by total_employee desc;

-- 16. Calculate the total revenue generated for each month in 2023, sorted chronologically.
select monthname(orders.order_date) as month_name, sum(orders.total_amount) as revenue from orders
where year(orders.order_date) = '2023'
group by month(orders.order_date), month_name
order by month(orders.order_date);
 
-- 17. Find the most popular product category based on the number of orders placed.
select productcategories.category_name, count(orders.order_id) as total_order from productcategories
left join products on productcategories.category_id = products.category_id
join orderitems on orderitems.product_id = products.product_id
join orders on orderitems.order_id = orders.order_id
group by productcategories.category_name
order by total_order desc limit 1;

alter table employees
add column full_name varchar(50) not null;

update employees
set full_name = concat(employees.first_name , " " , employees.last_name);

-- 18. Identify the employees who earn a salary higher than the average salary of their department.
select e1.full_name as full_name, e1.salary from employees as e1
where e1.salary > ( select avg(e2.salary) as avg_salary 
from employees as e2 
where e1.department = e2.department);

-- 19. Calculate the percentage of reviews that are 4 stars or higher for each product that has at least 2 reviews. 



















 