-- -----------------------------------------------------
-- Schema airplane
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS airline_system;

-- -----------------------------------------------------
-- Table `admins`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS admins (
  user_name VARCHAR(50) NOT NULL,
  passward CHAR(6) NULL DEFAULT NULL,
  PRIMARY KEY (user_name)
 );

-- -----------------------------------------------------
-- Table `flight`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS flight (
  flight_id CHAR(5),
  dept_time DATETIME,
  arrival_time DATETIME,
  dept_airport VARCHAR(3),
  arrival_airport VARCHAR(3),
  -- flight_date DATE,
  -- fare VARCHAR(10),
  fare INT,
  Airplane VARCHAR(7),
  PRIMARY KEY (flight_id)
);



-- -----------------------------------------------------
-- Table `passenger`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS passenger (
  Passport_num CHAR(5),
  f_name VARCHAR(50),
  l_name VARCHAR(50),
  address VARCHAR(255),
  phone_num CHAR(9),
  Nationality VARCHAR(255),
  PRIMARY KEY (Passport_num)
);

-- -----------------------------------------------------
-- Table `receptionist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS receptionist (
  user_name VARCHAR(50),
  passward VARCHAR(6),
  PRIMARY KEY (user_name)
);

-- -----------------------------------------------------
-- Table `ticket`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS ticket (
  Passport_num CHAR(5),
  flight_id CHAR(5),
  PRIMARY KEY (Passport_num, flight_id),

  CONSTRAINT FK_Passport_num FOREIGN KEY (Passport_num)
  REFERENCES passenger(Passport_num)
  ON UPDATE CASCADE
  ON DELETE CASCADE,

  CONSTRAINT FK_flight_id FOREIGN KEY (flight_id)
  REFERENCES flight(flight_id)
  ON UPDATE CASCADE
  ON DELETE CASCADE
);

-- -----------------------------------------------------
-- INSERTING VALUES
-- -----------------------------------------------------
INSERT INTO passenger
VALUES
    ("01010","Clark","Kent","00, Street 1, Nowhere","190078601","Kryptonian"),
    ("12121","Tony","Stark","01, Stark Tower, Hidden","000000000","American"),
    ("23232","Steve","Rogers","02, Avengers Facility, Finished","111111111","American"),
    ("34343","Arthur","Fleck","03, Arkham Asylum, Gotham","222222222","DarkWorld"),
    ("45454","Stevan","Strange","04, Bleecker Street, Newyork","333333333","British"),
    ("56565","Peter","Parker","05, Far From Home, Titan","444444444","Queens"),
    ("67676","Bruce","Wayne","06, Mountain Drive, BatCave","555555555","Scottish"),
    ("78787","Baby","Thanos","07, Purple Tan, Garden","666666666","Titanian"),
    ("89898","Bruce","Banner","08, Dump Garden, Sakar","777777777","Sakarian"),
    ("90909","Loki","Laufeyson","09, SpaceStone, Asgard","888888888","Asgardian");
    
INSERT INTO flight
VALUES
    ("PAK01", "2019-01-25 22:30", "2019-01-26 01:00", "LHR", "ISL", 6000, "PIA-111"),
    ("PAK02", "2019-01-26 08:00", "2019-01-26 11:30", "KHI", "GIL", 15000, "PIA-222"),
    ("PAK03", "2019-01-26 12:00", "2019-01-26 06:00", "PSH", "DUB", 20000, "PIA-333"),
    ("IND04", "2019-01-26 15:30", "2019-01-26 21:30", "KOL", "QUE", 50000, "IAA-444"),
    ("AFG05", "2019-01-26 19:00", "2019-01-26 23:30", "KAB", "ISL", 34500, "AFA-555"),
    ("CHI06", "2019-01-27 01:30", "2019-01-27 05:30", "XON", "MUZ", 19500, "ALC-666"),
    ("PAK07", "2019-01-27 06:00", "2019-01-27 08:30", "KHI", "LHR", 13500, "PIA-777"),
    ("BRA08", "2019-01-27 23:45", "2019-01-28 02:45", "RIO", "MOS", 4550, "BIA-888"),
    ("NZL09", "2019-01-28 15:00", "2019-01-28 20:30", "BRI", "ADE", 9500, "NIA-999"),
    ("CAN10", "2019-01-28 20:30", "2019-01-28 23:30", "QWE", "TRY", 3800, "CIA-915");
    
INSERT INTO admins
VALUES
    ("admin1", "qwerty");

INSERT INTO receptionist
VALUES
    ("recep1", "tokyo1");

INSERT INTO ticket
VALUES
    ("01010", "PAK01"),
    ("12121", "PAK02"),
    ("23232", "PAK03"),
    ("34343", "IND04"),
    ("45454", "AFG05"),
    ("56565", "CHI06"),
    ("67676", "PAK07"),
    ("78787", "BRA08"),
    ("89898", "NZL09"),
    ("90909", "CAN10");