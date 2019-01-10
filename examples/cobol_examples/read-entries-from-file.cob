IDENTIFICATION DIVISION.
PROGRAM-ID.  SeqWriteRead.

ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
    SELECT IN-FILE ASSIGN TO "example.dat"
		ORGANIZATION IS LINE SEQUENTIAL.

DATA DIVISION.
FILE SECTION.
FD IN-FILE. *> File Description statement, requried for each SELECT statement
01 ClientRec.
   88  EndOfIN-FILE  VALUE HIGH-VALUES.
   02  AcctNumber         PIC 9(7).
   02  ClientName.
       03 Surname        PIC X(8).
       03 FirstName       PIC X(10).
   02  DateOfBirth.
       03 YOBirth        PIC 9(4).
       03 MOBirth        PIC 9(2).
       03 DOBirth        PIC 9(2).
   02  StreetAddr.
       03 Street       PIC A(30).
       03 City         PIC A(15).
       03 State        PIC X(2).
       03 ZipCode      PIC 9(5).
   02  Gender            PIC X.


WORKING-STORAGE SECTION.

01 SWITCHES.
    05 EOF-SWITCH     PIC X VALUE "N".
01 COUNTERS.
    05 REC-COUNTER    PIC 9(3) VALUE 0.
  
PROCEDURE DIVISION.

000-MAIN.
    PERFORM 100-INITIALIZE.
    PERFORM 200-PROCESS-RECORDS
      UNTIL EOF-SWITCH = "Y".
    PERFORM 300-TERMINATE.
    STOP RUN.



100-INITIALIZE.

    OPEN INPUT IN-FILE.
    READ IN-FILE
      AT END
        MOVE "Y" TO EOF-SWITCH 
      NOT AT END
        COMPUTE REC-COUNTER = REC-COUNTER + 1
    END-READ.


200-PROCESS-RECORDS.

  DISPLAY "ACCTNUMBER >>>> " AcctNumber.
  DISPLAY "ClientName >>>> " ClientName.
  DISPLAY "DateOfBirth. >>>> " DateOfBirth.
  DISPLAY "Address.  >>>> " StreetAddr.
  DISPLAY "Gender >>>> "  Gender.

    READ IN-FILE
      AT END
        MOVE "Y" TO EOF-SWITCH 
      NOT AT END
        COMPUTE REC-COUNTER = REC-COUNTER + 1
    END-READ.

300-TERMINATE.
  DISPLAY "NUM OF RECS >>>> " REC-COUNTER.
CLOSE IN-FILE.