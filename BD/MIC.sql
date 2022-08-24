create database MIC;
use mic;

create table leitura (
idMetricas int primary key auto_increment,
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

select * from leitura;
truncate table leitura;
drop table leitura;