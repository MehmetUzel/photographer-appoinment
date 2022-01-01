CREATE TABLE "user" (
  "id" SERIAL PRIMARY KEY,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "phone" varchar,
  "password" varchar,
  "created_at" timestamp
);

CREATE TABLE "address" (
  "code" int PRIMARY KEY,
  "user_id" int,
  "name" varchar,
  "city" varchar,
  "district" varchar,
  "street" varchar,
  "neighbourhood" varchar,
  "building_num" varchar,
  "flat_num" varchar,
  "instructions" varchar
);

CREATE TABLE "order_items" (
  "order_id" int,
  "product_id" int,
  "quantity" int DEFAULT 1
);

CREATE TABLE "order" (
  "id" int PRIMARY KEY,
  "user_id" int,
  "status" varchar,
  "created_at" varchar
);

CREATE TABLE "product" (
  "id" int PRIMARY KEY,
  "name" varchar,
  "description" varchar,
  "price" int,
  "is_active" boolean
);

CREATE TABLE "payment" (
  "id" int PRIMARY KEY,
  "order_id" int,
  "total" int,
  "payment_choice" varchar
);

CREATE TABLE "photo" (
  "id" int PRIMARY KEY,
  "url" varchar,
  "product_id" int
);

CREATE TABLE "appoinment" (
  "id" int PRIMARY KEY,
  "user_id" int,
  "appoinment_date" varchar,
  "time" varchar,
  "created_at" varchar
);

CREATE TABLE "off_days" (
  "id" int PRIMARY KEY,
  "off_date" varchar,
  "time" varchar
);

CREATE TABLE "cart_items" (
  "id" int PRIMARY KEY,
  "cart_id" int,
  "product_id" int,
  "quantity" int DEFAULT 1
);

CREATE TABLE "cart" (
  "id" int PRIMARY KEY,
  "user_id" int,
  "created_at" varchar
);

ALTER TABLE "address" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

ALTER TABLE "order_items" ADD FOREIGN KEY ("order_id") REFERENCES "order" ("id");

ALTER TABLE "order_items" ADD FOREIGN KEY ("product_id") REFERENCES "product" ("id");

ALTER TABLE "order" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

ALTER TABLE "payment" ADD FOREIGN KEY ("order_id") REFERENCES "order" ("id");

ALTER TABLE "photo" ADD FOREIGN KEY ("product_id") REFERENCES "product" ("id");

ALTER TABLE "appoinment" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

ALTER TABLE "cart_items" ADD FOREIGN KEY ("cart_id") REFERENCES "cart" ("id");

ALTER TABLE "cart_items" ADD FOREIGN KEY ("product_id") REFERENCES "product" ("id");

ALTER TABLE "cart" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

COMMENT ON COLUMN "order"."created_at" IS 'When order created';

COMMENT ON COLUMN "appoinment"."appoinment_date" IS 'When order created';

COMMENT ON COLUMN "appoinment"."time" IS 'morning - noon - evening';

COMMENT ON COLUMN "appoinment"."created_at" IS 'When order created';

COMMENT ON COLUMN "off_days"."off_date" IS 'When order created';

COMMENT ON COLUMN "off_days"."time" IS 'morning - noon - evening - all_day';

COMMENT ON COLUMN "cart"."created_at" IS 'When cart created,  it will be reset when order is created';
