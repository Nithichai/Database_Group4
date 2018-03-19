CREATE TABLE "grade" (
	`grade_char`	TEXT NOT NULL,
	`grade_id`	TEXT,
	PRIMARY KEY(`grade_char`)
);

CREATE TABLE "student" (
	`student_id`	TEXT NOT NULL,
	`firstname`	TEXT,
	`lastname`	TEXT,
	`email`		TEXT,
	`phone`		TEXT,
	PRIMARY KEY(`student_id`)
);

CREATE TABLE "subject" (
	`course_code`	TEXT NOT NULL,
	`title`		TEXT,
	`credit`	INTEGER,
	PRIMARY KEY(`course_code`)
);

CREATE TABLE "transcript" (
	`id`	BIGSERIAL NOT NULL PRIMARY KEY UNIQUE,
	`student_id`	TEXT,
	`year`		INTEGER,
	`semester`	INTEGER,
	`course_code`	TEXT,
	`grade_char`	TEXT,
	FOREIGN KEY(`course_code`) REFERENCES "subject"(`course_code`),
	FOREIGN KEY(`student_id`) REFERENCES "student"(`student_id`),
	FOREIGN KEY(`grade_char`) REFERENCES "grade"(`grade_char`)
);

CREATE TABLE sqlite_sequence(name,seq);
