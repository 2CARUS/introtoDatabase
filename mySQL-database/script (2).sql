-- CREATE SCHEMA IF NOT EXISTS not_the_home_depot;

CREATE TABLE address(
	address_id INT(9) NOT NULL,
    building_number INT(9) NOT NULL,
    street VARCHAR(30) NOT NULL,
    apartment VARCHAR(15),
    city VARCHAR(30) NOT NULL,
    state VARCHAR(30) NOT NULL,
    country VARCHAR(30) NOT NULL,
    zip VARCHAR(5) NOT NULL,
    PRIMARY KEY(address_id)
);

CREATE TABLE supplier(
	supplier_id INT(9) NOT NULL,
    supplier_name VARCHAR(30) NOT NULL,
    supplier_phone VARCHAR(10) NOT NULL,
    PRIMARY KEY(supplier_ID)
);

CREATE TABLE store(
	store_id INT(9) NOT NULL,
    store_name VARCHAR(20) NOT NULL,
    store_phone INT(10) NOT NULL,
    store_email varchar(30) NOT NULL,
    store_address_id INT(9) NOT NULL,
    PRIMARY KEY(store_id),
    FOREIGN KEY(store_address_id) REFERENCES address(address_id)
);

CREATE TABLE IF NOT EXISTS department(
	department_id INT(9) NOT NULL,
    dep_store_id INT(9) NOT NULL,
    department_name varchar(30) NOT NULL,
    PRIMARY KEY(department_id),
    FOREIGN KEY(DEP_store_id) REFERENCES store(store_id)
);

CREATE TABLE product(
	product_id INT(9) NOT NULL,
    product_name VARCHAR(25) NOT NULL,
    product_price DECIMAL(13, 2) NOT NULL,
    product_desc VARCHAR(100),
    product_supplier_id INT(9) NOT NULL,
    PRIMARY KEY(product_id),
    FOREIGN KEY(product_supplier_id) REFERENCES supplier(supplier_id)
);

CREATE TABLE customer(
	customer_id INT(9) NOT NULL,
    payment_method VARCHAR(30) NOT NULL,
    customer_name VARCHAR(50) NOT NULL,
    customer_phone INT(10) NOT NULL,
    customer_email VARCHAR(30) NOT NULL,
    customer_address_id INT(9) NOT NULL,
    PRIMARY KEY (customer_id),
    FOREIGN KEY (customer_address_id) REFERENCES address(address_id)
);

CREATE TABLE order_contents(
    order_id INT(16) NOT NULL,
    product_id INT(9) NOT NULL,
    order_quantity INT(5) NOT NULL,
    cumulitive_price DECIMAL(13, 2) NOT NULL,
    PRIMARY KEY(order_id),
    FOREIGN KEy(product_id) REFERENCES product(product_id)
);

CREATE TABLE customer_order(
	order_id INT(16) NOT NULL,
    cust_id INT(9) NOT NULL,
    order_status varchar(15) NOT NULL,
    order_date DATETIME NOT NULL,
    PRIMARY KEY(order_id,cust_id),
    FOREIGN KEY(cust_id) REFERENCES customer(customer_id),
    FOREIGN KEY(order_id) REFERENCES order_contents(order_id)
);

CREATE TABLE inventory(
	product_id INT(9) NOT NULL,
    store_id INT(9) NOT NULL,
    amount INT(5) NOT NULL,
    PRIMARY KEY (product_id, store_id),
    FOREIGN KEY(product_id) REFERENCES product(product_id),
    FOREIGN KEY(store_id) REFERENCES store(store_id)
);
