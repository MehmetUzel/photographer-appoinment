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

ALTER TABLE "address" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

ALTER TABLE "appoinment" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

COMMENT ON COLUMN "appoinment"."appoinment_date" IS 'When order created';

COMMENT ON COLUMN "appoinment"."time" IS 'morning - noon - evening';

COMMENT ON COLUMN "appoinment"."created_at" IS 'When order created';

COMMENT ON COLUMN "off_days"."off_date" IS 'When order created';

COMMENT ON COLUMN "off_days"."time" IS 'morning - noon - evening - all_day';
