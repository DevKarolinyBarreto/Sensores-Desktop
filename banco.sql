create database plantas; 
use plantas; 

create table cadastro_plantas (
id int auto_increment primary key,
nome_popular varchar (100) not null,
nome_cientifico varchar (100) not null,
imagem_path text
);

create table dados (
id int auto_increment primary key,
temperatura decimal not null, 
luminosidade int not null, 
umidade decimal not null
);

select * from cadastro_plantas;
select * from dados;	