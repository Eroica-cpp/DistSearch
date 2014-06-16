## create click table to record users' click history
create table click (
uid varchar(50),
site_id varchar(100),
context text,
time datetime
);

## create index for table sim_doc
create index idx_id12 on sim_doc (id1, id2);

