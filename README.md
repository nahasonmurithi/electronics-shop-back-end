# electronics-shop-back-end

// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

// Table bar {
//   id integer [primary key]
//   name varchar
//   description varchar
//   address varchar
//   created_at timestamp 
// }

Table tables {
  id integer [primary key]
  table_number int
  staff_id int (FK)
  capacity int
  status varchar
}

Table customers {
  id integer [primary key]
  username varchar
  email varchar
  phone_number int
  status varchar
}

Table orders {
  id integer [primary key]
  customer_id integer (FK)
  table_id integer (FK)
  order_date timestamp
  total_amount int
  status varchar
}

Table menuItems {
  item_id integer [primary key]
  name varchar
  description varchar
  price int
  category_id integer (FK)
}

Table category {
  id integer [primary key]
  name varchar
}

Table staff {
  id integer [primary key]
  first_name varchar
  last_name varchar
  role varchar
  hire_date timestamp
}

Table reservations {
  id integer [primary key]
  customer_id int (FK)
  table_id int (FK)
  reservation_date timestamp
  reservation_time timestamp
  party_size int
}

Table reviews {
  id integer [primary key]
  customer_id int (FK)
  table_id int (FK)
  rating int
  comment varchar
} 

Table payments {
  id integer [primary key]
  order_id int (FK)
  payment_method varchar

}



Ref: menuItems.category_id > category.id
Ref: payments.order_id > orders.id
Ref: reservations.customer_id > customers.id
Ref: reservations.table_id > tables.id
Ref: orders.customer_id > customers.id
Ref: orders.table_id > tables.id
Ref: reviews.customer_id > customers.id
Ref: reviews.table_id > tables.id
Ref: tables.staff_id > staff.id
// Ref: posts.user_id > users.id // many-to-one

// Ref: users.id < follows.following_user_id

// Ref: users.id < follows.followed_user_id
