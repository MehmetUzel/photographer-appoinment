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
  "group" varchar,
  "album" varchar,
  "num_of_consept" int,
  "is_active" boolean
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
  "name" varchar,
  "is_active" boolean
);

CREATE TABLE "photo_consept" (
  "id" int PRIMARY KEY,
  "consept_id" int,
  "url" varchar
);

CREATE TABLE "payment" (
  "id" int PRIMARY KEY,
  "shoot_id" int,
  "total" int,
  "payment_choice" varchar,
  "is_paid" boolean
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

ALTER TABLE "address" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

ALTER TABLE "address" ADD FOREIGN KEY ("city") REFERENCES "city" ("id");

ALTER TABLE "address" ADD FOREIGN KEY ("district") REFERENCES "district" ("id");

ALTER TABLE "district" ADD FOREIGN KEY ("city") REFERENCES "city" ("id");

ALTER TABLE "shoot_plan" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

ALTER TABLE "photo_consept" ADD FOREIGN KEY ("consept_id") REFERENCES "consept" ("id");

ALTER TABLE "payment" ADD FOREIGN KEY ("shoot_id") REFERENCES "shoot_plan" ("id");

ALTER TABLE "appoinment" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

ALTER TABLE "appoinment" ADD FOREIGN KEY ("time") REFERENCES "shoot_time" ("time");

ALTER TABLE "off_days" ADD FOREIGN KEY ("time") REFERENCES "shoot_time" ("time");

ALTER TABLE "shoot_appointment" ADD FOREIGN KEY ("shoot_id") REFERENCES "shoot_plan" ("id");

ALTER TABLE "shoot_appointment" ADD FOREIGN KEY ("appoinment_id") REFERENCES "appoinment" ("id");

ALTER TABLE "shoot_concept" ADD FOREIGN KEY ("shoot_id") REFERENCES "shoot_plan" ("id");

ALTER TABLE "shoot_concept" ADD FOREIGN KEY ("concept_id") REFERENCES "consept" ("id");

COMMENT ON COLUMN "shoot_plan"."group" IS 'default values';

COMMENT ON COLUMN "shoot_plan"."album" IS 'default values';

COMMENT ON COLUMN "appoinment"."appoinment_date" IS 'When order created';

COMMENT ON COLUMN "appoinment"."created_at" IS 'When order created';

COMMENT ON COLUMN "off_days"."off_date" IS 'When order created';

COMMENT ON COLUMN "shoot_time"."time" IS 'create calendar times based on this but dont query that one every time, render pages once it changes and serve them to user';
