create database MIC;
use mic;

create table empresa (
idEmpresa int primary key auto_increment,
email VARCHAR (60),
senha VARCHAR (30),
nomeEmp VARCHAR (45),
CNPJ CHAR (18),
telefoneEmp CHAR (8),
qntSetores INT,
qntMaquinas INT
)auto_increment = 01;

create table analista (
idAnalista INT PRIMARY KEY AUTO_INCREMENT, 
fkEmpresa int,
foreign key (fkEmpresa) references empresa (idEmpresa),
nomeAnalista VARCHAR (45),
emailAnalista VARCHAR (60),
senhaAnalista VARCHAR (45)
);

create table maquina (
idMaquina INT PRIMARY KEY AUTO_INCREMENT, 
PA INT, 
Setor INT,
CPU DECIMAL(4,1),
RAM DECIMAL(4,1),
Disco DECIMAL(4,1),
Rede DECIMAL(4,1),
SistemaOperacional VARCHAR (45),
VersaSO VARCHAR (45),
serialMaq VARCHAR (45)
);


create table maquinaSim (
idMaquinaSim INT PRIMARY KEY auto_incremenT, 
nomeMaq VARCHAR (45)
);

create table leitura (
idMetricas int primary key auto_increment,
fkMaquina INT, 
foreign key (fkMaquina) references maquinaSim (idMaquinaSim),
DataHora VARCHAR(20),
PrcntCPU DECIMAL(4,1),
PortasLogicas varchar(2),
PrcntRAM DECIMAL(4,1),
TotalVirtual INT,
PrcntDisco DECIMAL(4,1),
Upload DECIMAL(4,1),
Download DECIMAL(4,1),
DropDown DECIMAL(4,1),
DropUp DECIMAL(4,1)
);


insert into maquinaSim (nomeMaq) values ('maquina 1'),
										('maquina 2'),
                                        ('maquina 3');



select * from leitura where fkmaquinaSim = 1;
select * from leitura where fkmaquinaSim = 2;
select * from leitura where fkmaquinaSim = 3;


select * from maquinaSim;
select * from leitura;

truncate table leitura;

drop table leitura;
drop table maquinaSim;

drop database mic;