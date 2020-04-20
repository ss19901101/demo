create database demo;

create table device
(
	id bigint auto_increment,
	esn varchar(255) null,
	device_name varchar(255) null,
	device_type int null,
	status tinyint null,
	deleted tinyint not null default 0,
	constraint table_name_id_uindex
		unique (id)
);

alter table device
	add primary key (id);

create table interface
(
	id bigint auto_increment,
	device_id bigint not null,
	interface_type tinyint null,
	ip varchar(32) null,
    deleted tinyint not null default 0,
	constraint interface_id_uindex
		unique (id),
	constraint interface_device_id_fk
		foreign key (deviceId) references device (id)
			on update cascade on delete cascade
);

alter table interface
	add primary key (id);
