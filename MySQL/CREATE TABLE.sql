CREATE TABLE `transcripts`.`grade` (
  `grade_char` 	VARCHAR(5) NOT NULL,
  `grade_id` 	INT(10),
  PRIMARY KEY (`grade_char`)
);

CREATE TABLE `transcripts`.`student` (
	`student_id` 	VARCHAR(20) NOT NULL,
	`firstname`	VARCHAR(100),
	`lastname`	VARCHAR(100),
	`email`		VARCHAR(100),
	`phone`		VARCHAR(20),
	PRIMARY KEY(`student_id`)
);

CREATE TABLE `transcripts`.`subject` (
	`course_code`	VARCHAR(50) NOT NULL,
	`title`		VARCHAR(20),
	`credit`	INTEGER,
	PRIMARY KEY(`course_code`)
);

CREATE TABLE `transcripts`.`transcript` (
	`id`	BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
	`student_id`	VARCHAR(20),
	`year`		INT(5),
	`semester`	INT(5),
	`course_code`	VARCHAR(50),
	`grade_char`	VARCHAR(5),
	FOREIGN KEY(`course_code`) REFERENCES `subject`(`course_code`),
	FOREIGN KEY(`student_id`) REFERENCES `student`(`student_id`),
	FOREIGN KEY(`grade_char`) REFERENCES `grade`(`grade_char`)
);
