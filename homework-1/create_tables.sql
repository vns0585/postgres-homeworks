-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(255) NOT NULL,
	birth_date date,
	notes text
);

CREATE TABLE customers
(
	customer_id char(5) PRIMARY KEY,
	company_name varchar(255) NOT NULL,
	contact_name varchar(200) NOT NULL
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id char(5) NOT NULL,
	employee_id int NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(100) NOT NULL,
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
	FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);