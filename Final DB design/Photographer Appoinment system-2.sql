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
  "id" int PRIMARY KEY,
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

CREATE TABLE "district" (
  "id" int PRIMARY KEY,
  "city" int,
  "name" varchar
);

CREATE TABLE "city" (
  "id" int PRIMARY KEY,
  "name" varchar
);

CREATE TABLE "shoot_plan" (
  "id" int PRIMARY KEY,
  "user_id" int,
  "type_id" int,
  "album_id" int,
  "num_of_concept" int,
  "is_active" boolean,
  "created_at" timestamp,
  "total" int,
  "payment_choice" varchar,
  "is_paid" boolean
);

CREATE TABLE "consept_info" (
  "id" int PRIMARY KEY,
  "number_of_selection" int,
  "price" int
);

CREATE TABLE "album_info" (
  "id" int PRIMARY KEY,
  "type" varchar,
  "price" int
);

CREATE TABLE "consept" (
  "id" int PRIMARY KEY,
  "type_id" int,
  "name" varchar,
  "is_active" boolean
);

CREATE TABLE "photo_consept" (
  "id" int PRIMARY KEY,
  "consept_id" int,
  "url" varchar
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

CREATE TABLE "shoot_time" (
  "id" int PRIMARY KEY,
  "time" varchar
);

CREATE TABLE "shoot_appointment" (
  "id" int PRIMARY KEY,
  "shoot_id" int,
  "appoinment_id" int
);

CREATE TABLE "shoot_concept" (
  "id" int PRIMARY KEY,
  "shoot_id" int,
  "concept_id" int
);

CREATE TABLE "shoot_type" (
  "id" int PRIMARY KEY,
  "name" varchar
);

COMMENT ON COLUMN "appoinment"."appoinment_date" IS 'When order created';

COMMENT ON COLUMN "appoinment"."created_at" IS 'When order created';

COMMENT ON COLUMN "off_days"."off_date" IS 'When order created';

COMMENT ON COLUMN "shoot_time"."time" IS 'create calendar times based on this but dont query that one every time, render pages once it changes and serve them to user';

ALTER TABLE "address" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

ALTER TABLE "address" ADD FOREIGN KEY ("city") REFERENCES "city" ("id");

ALTER TABLE "address" ADD FOREIGN KEY ("district") REFERENCES "district" ("id");

ALTER TABLE "district" ADD FOREIGN KEY ("city") REFERENCES "city" ("id");

ALTER TABLE "shoot_plan" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

ALTER TABLE "shoot_plan" ADD FOREIGN KEY ("type_id") REFERENCES "shoot_type" ("id");

ALTER TABLE "shoot_plan" ADD FOREIGN KEY ("album_id") REFERENCES "album_info" ("id");

ALTER TABLE "shoot_plan" ADD FOREIGN KEY ("num_of_concept") REFERENCES "consept_info" ("id");

ALTER TABLE "consept" ADD FOREIGN KEY ("type_id") REFERENCES "shoot_type" ("id");

ALTER TABLE "photo_consept" ADD FOREIGN KEY ("consept_id") REFERENCES "consept" ("id");

ALTER TABLE "appoinment" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

ALTER TABLE "appoinment" ADD FOREIGN KEY ("time") REFERENCES "shoot_time" ("time");

ALTER TABLE "off_days" ADD FOREIGN KEY ("time") REFERENCES "shoot_time" ("time");

ALTER TABLE "shoot_appointment" ADD FOREIGN KEY ("shoot_id") REFERENCES "shoot_plan" ("id");

ALTER TABLE "shoot_appointment" ADD FOREIGN KEY ("appoinment_id") REFERENCES "appoinment" ("id");

ALTER TABLE "shoot_concept" ADD FOREIGN KEY ("shoot_id") REFERENCES "shoot_plan" ("id");

ALTER TABLE "shoot_concept" ADD FOREIGN KEY ("concept_id") REFERENCES "consept" ("id");
