CREATE TABLE "grade" (
	`grade_char`	TEXT NOT NULL,
	`grade_id`	TEXT NOT NULL,
	PRIMARY KEY(`grade_char`)
);

CREATE TABLE "student" (
	`student_id`	TEXT NOT NULL,
	`firstname`	TEXT NOT NULL,
	`lastname`	TEXT NOT NULL,
	`email`	TEXT NOT NULL,
	`phone`	TEXT NOT NULL,
	PRIMARY KEY(`student_id`)
);

CREATE TABLE "subject" (
	`course_code`	TEXT NOT NULL,
	`title`	TEXT NOT NULL,
	`credit`	INTEGER NOT NULL,
	PRIMARY KEY(`course_code`)
);

CREATE TABLE "transcript" (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`student_id`	TEXT NOT NULL,
	`year`	INTEGER NOT NULL,
	`semester`	INTEGER NOT NULL,
	`course_code`	TEXT NOT NULL,
	`grade_char`	TEXT NOT NULL,
	FOREIGN KEY(`course_code`) REFERENCES "subject"(`course_code`),
	FOREIGN KEY(`student_id`) REFERENCES "student"(`student_id`),
	FOREIGN KEY(`grade_char`) REFERENCES "grade"(`grade_char`)
);

CREATE TABLE sqlite_sequence(name,seq);
