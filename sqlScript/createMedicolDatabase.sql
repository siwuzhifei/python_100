Create database MedicalPractice
Go
Use MedicalPractice

Create table Patient
(
    Patient_ID int primary key,
    Title NVARCHAR(20),
    FirstName NVARCHAR(50),
    MiddleInitial NCHAR(1),
    LastName NVARCHAR(50),
    HouseUnitLotNum NVARCHAR(5),
    Street NVARCHAR(50),
    Suburb NVARCHAR(50),
    State NVARCHAR(3),
    PostCode NCHAR(4),
    HomePhone NCHAR(10),
    MobilePhone NCHAR(10),
    MedicareNumber NCHAR(16),
    DateOfBirth DATE,
    Gender NCHAR(20)
)

Create table PractitionerType
(
	PractitionerType NVARCHAR(50) primary key
)

Create table WeekDays
(
	WeekDayName NVARCHAR(9) primary key
)

Create table Practitioner
(
    Practitioner_ID int primary key,
    Title NVARCHAR(20),
    FirstName NVARCHAR(50),
    MiddleInitial NCHAR(1),
    LastName NVARCHAR(50),
    HouseUnitLotNum NVARCHAR(5),
    Street NVARCHAR(50),
    Suburb NVARCHAR(50),
    State NVARCHAR(3),
    PostCode NCHAR(4),
    HomePhone NCHAR(8),
    MobilePhone NCHAR(8),
    MedicareNumber NCHAR(16),
	MedicalRegistrationNumber NCHAR(11)
        UNIQUE NOT NULL,
    DateOfBirth DATE,
    Gender NCHAR(20),
	PractitionerType_Ref NVARCHAR(50),
	Constraint FK_PractitionerType_Ref foreign key (PractitionerType_Ref) references PractitionerType(PractitionerType)

)


Create table Availability
(
	WeekDayName_Ref NVARCHAR(9),
	Constraint FK_Availability_WeekDays
	foreign key (WeekDayName_Ref) references WeekDays(WeekDayName),
	Practitioner_Ref INTEGER,
	Constraint FK_Availability_Practitioner
	foreign key (Practitioner_Ref) references Practitioner(Practitioner_ID),
	primary key(WeekDayName_Ref,Practitioner_Ref)
)


Create table Appointment
(
    Practitioner_Ref INTEGER,
	Constraint FK_Appointment_Practitioner
        foreign key (Practitioner_Ref) references Practitioner (Practitioner_ID),
    AppDate DATE NOT NULL,
    AppStartTime TIME NOT NULL,
    Patient_Ref Integer NOT NULL,
	Constraint FK_Appointment_Patient
		FOREIGN KEY (Patient_Ref) REFERENCES Patient (Patient_ID),
    primary key
    (
        Practitioner_Ref,
        AppDate,
        AppStartTime
    ),
    CONSTRAINT UC_Person
        UNIQUE
        (
            AppDate,
            AppStartTime,
            Patient_Ref
        )
)



Insert into Patient
Values
(10000,'Mr','Mackenzie','J','Fleetwood','233','Dreaming Street','Roseville','NSW','2069','298654743','465375486','7253418356478250','2000-03-12','male'),
(10001,'Ms','Jane','P','Killingsworth','34','Southern Road','Yarramundi','NSW','2753','234654345','342134679','9365243640183640','1943-04-08','female'),
(10002,'Mr','Peter','D','Leons','21','Constitution Drive','West Hoxton','NSW','2171','276539183','125364927','1873652945578930','1962-07-08','male'),
(10003,'Mr','Phill','B','Greggan','42','Donn Lane','Killara','NSW','2071','276548709','1234326789','6473645782345670','1971-08-31','male'),
(10004,'Dr','John','W','Ward','332','Tomorrow Road','Chatswood','NSW','2488','4847383848','4838382728','4738294848484830','1978-02-12','male'),
(10005,'Mrs','Mary','D','Brown','Lot23','Johnston Road','Warwick Farm','NSW','2170','297465243','417335224','9356273321176540','1972-03-05','female'),
(10006,'Mr','Terrence','D','Hill','43','Somerland Road','La Perouse','NSW','2987','266645432','365243561','6363525353535350','2005-10-04','male'),
(10007,'Master','Adrian','B','Tamerkand','44','The Hill Road','Macquarie Fields','NSW','2756','276546783','4848473738','9863652527637330','2008-12-12','male'),
(10008,'Ms','Joan','D','Wothers','32','Slapping Street','Mount Lewis','NSW','2343','1294848777','8484737384','9484746125364760','1997-06-12','female'),
(10009,'Mrs','Caroline','J','Barrette','44','Biggramham Road','St Kilda','VIC','4332','384736278','9383827373','1234565725463720','1965-04-04','female'),
(10010,'Mrs','Wendy','J','Pilington','182','Parramatta Road','Lidcombe','NSW','2345','4837383848','8473838383','8483727616273830','1985-09-17','female')

select * from Patient
SELECT FORMAT(DateOfBirth, 'dd/MM/yyyy') AS formatted_date FROM Patient;

Insert into PractitionerType
Values
('Diagnostic radiographer'),
('Enrolled nurse'),
('Medical Practitioner (Doctor or GP)'),
('Medical radiation practitioner'),
('Midwife'),
('Nurse'),
('Occupational therapist'),
('Optometrist'),
('Osteopath'),
('Physical therapist'),
('Physiotherapist'),
('Podiatrist'),
('Psychologist'),
('Radiation therapist'),
('Registered nurse');

Insert into WeekDays
Values
('Friday'),
('Monday'),
('Thursday'),
('Tuesday'),
('Wednesday');



ALTER TABLE Practitioner
ALTER COLUMN HomePhone NVARCHAR(18);

ALTER TABLE Practitioner
ALTER COLUMN MobilePhone NVARCHAR(18);

Insert into Practitioner
Values
(10000,'Dr','Mark','P','Huston','21','Fuller Street','Sunshine','NSW','2343','287657483','476352638','9878986473892750','63738276173','1975-07-07','male','Medical Practitioner (Doctor or GP)'),
(10001,'Mrs','Hilda','D','Brown','32','Argyle Street','Bonnels Bay','NSW','2264','249756544','318466453','4635278435099920','37876273849','1993-12-03','female','Registered nurse'),
(10002,'Mrs','Jennifer','J','Dunsworth','45','Dora Street','Morriset','NSW','2264','249767574','228484373','7666777833449870','48372678939','1991-06-04','female','Registered nurse'),
(10003,'Mr','Jason','D','Lithdon','43','Fowler Street','Camperdown','NSW','2050','298785645','317896453','487736265377777','12345678901','1989-08-09','male','nurse'),
(10004,'Ms','Paula','D','Yates','89','Tableton Road','Newtown','NSW','2051','289876432','938473625','6637474433222880','84763892834','1982-09-07','female','Midwife'),
(10005,'Dr','Ludo','V','Vergenargen','27','Pembleton Place','Redfern','NSW','2049','9383737627','8372727283','8484737626278880','84737626673','1986-05-15','male','Medical Practitioner (Doctor or GP)'),
(10006,'Dr','Anne','D','Funsworth','4/89','Pacific Highway','St Leonards','NSW','2984','8847362839','8372688949','8477666525173730','36271663788','1991-12-11','female','Psychologist'),
(10007,'Mrs','Leslie','V','Gray','98','Dandaraga Road','Mirrabooka','NSW','2264','4736728288','4837726789','4847473737277270','5958474636','1989-03-11','female','Podiatrist'),
(10008,'Dr','Adam','J','Moody','35','Mullabinga Way','Brightwaters','NSW','2264','8476635678','2736352536','7473636527771180','63635245256','1990-09-23','male','Medical practitioner (Doctor or GP)'),
(10009,'Mr','Leslie','Y','Gray','3','Dorwington Place','Enmore','NSW','2048','8473763678','4484837289','3827284716390980','38277121234','1991-04-11','male','nurse')

select * from Practitioner

Insert into Availability(Practitioner_Ref,WeekDayName_Ref)
Values
(10000,'Friday'),
(10000,'Monday'),
(10000,'Wednesday'),
(10001,'Thursday'),
(10001,'Tuesday'),
(10002,'Thursday'),
(10002,'Tuesday'),
(10003,'Friday'),
(10003,'Monday'),
(10003,'Wednesday'),
(10004,'Friday'),
(10004,'Monday'),
(10005,'Thursday'),
(10005,'Tuesday'),
(10006,'Wednesday'),
(10007,'Thursday'),
(10007,'Tuesday'),
(10008,'Friday'),
(10008,'Monday'),
(10008,'Wednesday');





Insert into Appointment
Values
(10005,'2019-09-17','08:15:00',10000),
(10006,'2019-09-18','10:00:00',10000),
(10006,'2019-09-18','10:15:00',10000),
(10006,'2019-09-18','10:30:00',10000),
(10006,'2019-09-18','10:45:00',10000),
(10006,'2019-09-18','11:00:00',10000),
(10005,'2019-09-17','09:00:00',10002),
(10000,'2019-09-18','08:00:00',10003),
(10005,'2019-09-17','08:30:00',10005),
(10000,'2019-09-18','08:30:00',10005),
(10005,'2019-09-17','14:15:00',10006),
(10008,'2019-09-18','08:30:00',10006),
(10005,'2019-09-17','08:00:00',10008),
(10002,'2019-09-17','08:30:00',10008),
(10005,'2019-09-18','08:00:00',10008),
(10005,'2019-09-17','10:00:00',10009),
(10001,'2019-09-17','08:00:00',10010),
(10005,'2019-09-17','10:15:00',10010),
(10008,'2019-09-18','08:00:00',10010),
(10006,'2019-09-18','09:30:00',10010);

