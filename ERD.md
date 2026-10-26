

erDiagram

&#x20;   PATIENT ||--o{ ADMISSION : has

&#x20;   DEPARTMENT ||--o{ ADMISSION : handles

&#x20;   DIAGNOSIS ||--o{ ADMISSION : recorded\_for

&#x20;   ADMISSION ||--o{ ADMISSION\_TEST : includes

&#x20;   TEST ||--o{ ADMISSION\_TEST : requested\_as

&#x20;   ADMISSION ||--o{ ADMISSION\_MEDICATION : includes

&#x20;   MEDICATION ||--o{ ADMISSION\_MEDICATION : recorded\_as



&#x20;   PATIENT {

&#x20;       string patient\_id PK

&#x20;       int age

&#x20;       string gender

&#x20;   }



&#x20;   DEPARTMENT {

&#x20;       int department\_id PK

&#x20;       string department\_name

&#x20;   }



&#x20;   DIAGNOSIS {

&#x20;       int diagnosis\_id PK

&#x20;       string diagnosis\_name

&#x20;   }



&#x20;   ADMISSION {

&#x20;       int admission\_id PK

&#x20;       string patient\_id FK

&#x20;       int department\_id FK

&#x20;       int diagnosis\_id FK

&#x20;       date admission\_date

&#x20;       int length\_of\_stay

&#x20;       decimal billing\_amount

&#x20;   }



&#x20;   TEST {

&#x20;       int test\_id PK

&#x20;       string test\_name

&#x20;   }



&#x20;   ADMISSION\_TEST {

&#x20;       int admission\_id PK, FK

&#x20;       int test\_id PK, FK

&#x20;       date test\_date

&#x20;       string test\_status

&#x20;   }



&#x20;   MEDICATION {

&#x20;       int medication\_id PK

&#x20;       string medication\_name

&#x20;   }



&#x20;   ADMISSION\_MEDICATION {

&#x20;       int admission\_id PK, FK

&#x20;       int medication\_id PK, FK

&#x20;       string recorded\_instructions

&#x20;   }



