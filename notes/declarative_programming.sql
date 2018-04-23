-- Declarative Programming --

-- 1) Cities

create table cities as
	select 38 as latitude, 122 as longitude, "Berkeley" as name union
	select 42,             71,               "Cambridge"        union
	select 45,             93,               "Minneapolis";

-- 2) Parents

create table parents as
	select "abraham" as parent, "barack" as child union
	select "abraham"          , "clinton"         union
	select "delano"           , "herbert"         union
	select "fillmore"         , "abraham"         union
	select "fillmore"         , "delano"          union
	select "fillmore"         , "fillmore"        union
	select "eisenhower"       , "fillmore";

-- 3) Children of abraham

select child from parents where parent = "abraham";

-- 4) Fillmores

select parent from parents where parent > child;
