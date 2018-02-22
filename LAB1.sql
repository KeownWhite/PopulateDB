-- Name: Keown White
-- ID num: 620052848
-- Date: Feb 21, 2018

DROP DATABASE IF EXISTS comp3161Lab1;
CREATE DATABASE comp3161Lab1;
use comp3161Lab1;

create table book(
  bookID int NOT NULL AUTO_INCREMENT,
  bookName varchar(20),
  edition int,
  primary key(bookID)
);

create table member(
  memberID int NOT NULL AUTO_INCREMENT,
  memberFname varchar(20),
  memberLnameRR varchar(20),
  city varchar(50),
  street varchar(50),
  primary key(memberID)
);


create table fine(
  bookID int NOT NULL,
  memberID int NOT NULL,
  unpadFines decimal(8,2),
  primary key(bookID,memberID),
	foreign key(bookID) references book(bookID) on delete cascade on update cascade,
	foreign key(memberID) references member(memberID) on delete cascade on update cascade
);

create table loan(
  bookID int NOT NULL,
  memberID int NOT NULL,
  dateOut DATE,
  returnDate DATE,
  primary key(bookID,memberID),
	foreign key(bookID) references book(bookID) on delete cascade on update cascade,
	foreign key(memberID) references member(memberID) on delete cascade on update cascade
);

-- STEP 1
ALTER TABLE member change memberLnameRR MemberLname varchar(20);
ALTER TABLE loan add column dueDate DATE after dateOut;
-- STEP 2


-- describe book;
-- describe member;
-- describe fine;
-- describe loan;
