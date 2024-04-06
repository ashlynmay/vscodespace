-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Find id and description for the CS50 duck report.
SELECT id, description FROM crime_scene_reports WHERE month = 7 AND day = 28;


-- Get interview transcripts and id's
SELECT id, transcript FROM interviews 
WHERE month = 7 AND day = 28;


-- Whittle down transcripts that mention the bakery and get names of people.
SELECT name, transcript FROM interviews 
WHERE id = 161 OR id = 162 OR id = 163;


-- Investigate Ruth's claims that she saw the theif drive away 10 minutes after the theft and get names of people based off of license plate numbers..
SELECT * FROM bakery_security_logs JOIN people ON people.license_plate = bakery_security_logs.license_plate 
WHERE month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 25 AND activity IS "exit";
-- Suspects: Vanessa, Bruce, Barry, Luca, Sofia, Iman, Diana, and Kelsey


-- Investigate Eugene's claim that he saw the thief at the ATM on Leggett St the morning of the theft, and compare suspect with prior claims.
SELECT person_id FROM bank_accounts JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number 
WHERE month = 7 AND day = 28 AND atm_location IS "Leggett Street";
-- Suspects: Bruce, Luca, Iman, and Diana



-- Investigate Raymond's claim that he saw the theif call someone for less than 1 minute after the crime and compare to prior data.
SELECT * FROM people JOIN phone_calls ON people.phone_number = phone_calls.caller 
WHERE duration < 60 AND day = 28 AND month = 7;
-- Callers at Bakery: Sofia, Kelsey, Bruce, Kelsey, Diana
SELECT name FROM people WHERE phone_number IS [receiver number]; -- repeat this for each receiver
SELECT name FROM people WHERE phone_number IS "(996) 555-8899";
-- Callers Possible accomplices: Sofia: Jack, Kelsey 1: Larry, Bruce: Robin, Kelsey 2: Melissa, Diana: Phillip   
SELECT name FROM people JOIN phone_calls ON people.phone_number = phone_calls.receiver 
WHERE duration < 60 AND day = 28 AND month = 7;
-- Receivers at Bakery: NULL
-- Suspects: Bruce & Robin, and Diana & Phillip



-- Investigate Raymond's calim that the thief is taking the earliest flight out of Fiftyville the following morning.
SELECT id FROM airports WHERE city IS "Fiftyville";
-- Fiftville's id: 8
SELECT id FROM flights WHERE origin_airport_id = 8 AND month = 7 AND day = 29 ORDER BY hour, minute ASC;
-- Earliest flight id: 36
SELECT * FROM passengers JOIN people ON passengers.passport_number = people.passport_number WHERE flight_id = 36;
-- Diana nor Phillip are registered as being on the flight, so the thief must be Bruce, with the accomplice Robin.
SELECT city FROM  FROM flights WHERE id = 36;