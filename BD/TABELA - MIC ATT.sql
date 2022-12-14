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
Setor VARCHAR (45),
CPU VARCHAR (45),
RAM VARCHAR (45),
Disco VARCHAR (45),
Rede VARCHAR (45),
SistemaOperacional VARCHAR (45),
VersaSO VARCHAR (45),
serialMaq VARCHAR (45)
);

create table leitura (
idMetricas int primary key auto_increment,
fkMaquina INT, 
foreign key (fkMaquina) references maquina (idMaquina),
DataHora varchar(19),
PrcntCPU varchar(6),
FreqCPU varchar(6),
PortasLogicas varchar(2),
TotalRAM varchar(6),
PrcntRAM varchar(6),
TotalVirtual varchar(6),
TotalDisco varchar(6),
PrcntDisco varchar(6),
Upload varchar(6),
Download varchar(6),
DropDown varchar(6),
DropUp varchar(6)
);

create table maquinaSim (
idMaquinaSim INT PRIMARY KEY auto_incremenT, 
nomeMaq VARCHAR (45)
);

create table leitura (
idLeituraSim INT PRIMARY KEY AUTO_INCREMENT,
fkmaquinaSim INT,
foreign key (fkMaquinaSim) references maquinaSim (idMaquinaSim),
cpuLeitura DECIMAL,
discoLeitura DECIMAL, 
memoriaLeitura DECIMAL
); 

insert into maquinaSim (nomeMaq) values ('maquina 1'),
										('maquina 2'),
                                        ('maquina 3');



select * from leitura where fkmaquinaSim = 1;
select * from leitura where fkmaquinaSim = 2;
select * from leitura where fkmaquinaSim = 3;

select * from maquina;
select * from analista;
select * from empresa;

select * from maquinaSim;
select * from leitura;

truncate table leitura;

drop table leitura;
drop table maquinaSim;

drop database mic;
