-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/5QBaql
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "NHES_19_PFI" (
	"id" varchar   NOT NULL,
	"ALLGRADEX" int   NOT NULL,
	"SEGRADES" int   NOT NULL,
	"CENREG" int   NOT NULL,
	"SCH_TYPE" int   NOT NULL,
	"EDCPUB" int   NOT NULL,
	"EDCCAT" int   NOT NULL,
	"EDCREL" int   NOT NULL,
	"EDCPRI" int   NOT NULL,
	"EDCINTK12" int   NOT NULL,
	"EDCHSFL" int   NOT NULL,
	"DISTASSI" int   NOT NULL,
	"SCHRTSCHL" int   NOT NULL,
	"SCHLMAGNET" int   NOT NULL,
	"SPBSCH" int   NOT NULL,
	"SOTHRSCH" int   NOT NULL,
	"STUTR" int   NOT NULL,
	"SOTHSCH" int   NOT NULL,
	"SEENJOY" int   NOT NULL,
	"SEABSNT" int   NOT NULL,
	"FCSCHOOL" int   NOT NULL,
	"FCTEACHR" int   NOT NULL,
	"FCSTDS" int   NOT NULL,
	"FCSUPPRT" int   NOT NULL,
	"FHHOME" int   NOT NULL,
	"FHWKHRS" int   NOT NULL,
	"FOSTORY2X" int   NOT NULL,
	"FOCRAFTS" int   NOT NULL,
	"FOGAMES" int   NOT NULL,
	"FOBUILDX" int   NOT NULL,
	"FOSPORT" int   NOT NULL,
	"FORESPON" int   NOT NULL,
	"FOHISTX" int   NOT NULL,
	"FODINNERX" int   NOT NULL,
	"FOLIBRAYX" int   NOT NULL,
	"FOBOOKSTX" int   NOT NULL,
	"FOCONCRTX" int   NOT NULL,
	"FOMUSEUMX" int   NOT NULL,
	"FOZOOX" int   NOT NULL,
	"FOGROUPX" int   NOT NULL,
	"FOSPRTEVX" int   NOT NULL,
	"HHENGLISH" int   NOT NULL,
	"CSPEAKX" int   NOT NULL,
	"HHTOTALXX" int   NOT NULL,
	"HHPRTNRSX" int   NOT NULL,
	"P1REL" int   NOT NULL,
	"P1SEX" int   NOT NULL,
	"P1MRSTA" int   NOT NULL,
	"P1AGE" int   NOT NULL,
	"P2GUARD" int   NOT NULL,
	"P2AGE" int   NOT NULL,
	"P2REL" int   NOT NULL,
	"P2SEX" int   NOT NULL,
	"P2MRSTA" int   NOT NULL,
	"PAR1EMPL" int   NOT NULL,
	"PAR1FTFY" int   NOT NULL,
	"PAR2FTFY" int   NOT NULL,
	"NUMSIBSX" int   NOT NULL,
	"TTLHHINC" int   NOT NULL,
	"OWNRNTHB" int   NOT NULL,
	"HVINTSPHO" int   NOT NULL,
	"HVINTCOM" int   NOT NULL,
	"INTACC" int   NOT NULL,
	"CHLDNT" int   NOT NULL,
	"LRNCOMP" int   NOT NULL,
	"LRNTAB" int   NOT NULL,
	"LRNCELL" int   NOT NULL,
	CONSTRAINT "pk_NHES_19_PFI" PRIMARY KEY (
	"id"
	)
);

CREATE TABLE "Surveys" (
	"id" varchar   NOT NULL,
	"updated" date   NOT NULL,
	"ALLGRADEX" int   NOT NULL,
	"SEGRADES" int   NOT NULL,
	"CENREG" int   NOT NULL,
	"FOBOOKSTX" int   NOT NULL,
	"FOCONCRTX" int   NOT NULL,
	"FOGAMES" int   NOT NULL,
	"FOLIBRAYX" int   NOT NULL,
	"FOMUSEUMX" int   NOT NULL,
	"FOSTORY2X" int   NOT NULL,
	"FORESPON" int   NOT NULL,
	"FOHISTX" int   NOT NULL,
	"FHHOME" int   NOT NULL,
	"FHWKHRS" int   NOT NULL,
	"SEABSNT" int   NOT NULL,
	"FCSTDS" int   NOT NULL,
	"FCTEACHR" int   NOT NULL,
	"SEENJOY" int   NOT NULL,
	"DISTASSI" int   NOT NULL,
	"SCHLMAGNET" int   NOT NULL,
	"SCHRTSCHL" int   NOT NULL,
	"CHLDNT" int   NOT NULL,
	"LRNCELL" int   NOT NULL
);

CREATE TABLE "Features" (
	"feature" text   NOT NULL,
	"value" float   NOT NULL,
	"group" text   NOT NULL
);

CREATE TABLE "Resources" (
	"id" SERIAL   PRIMARY KEY,
	"RESOURCE" text   NOT NULL,
	"GROUP" text   NOT NULL,
	"DESC" text   NOT NULL
);

CREATE TABLE "Users" (
	"id" SERIAL   PRIMARY KEY,
	"username" text   NOT NULL,
	"email" text   NOT NULL,
	"password_hash" text   NOT NULL
);
