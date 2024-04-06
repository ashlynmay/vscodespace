-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Find id and description for the CS50 duck report.
SELECT id, description FROM crime_scene_reports WHERE month = 7 AND day = 28;

SELECT id, transcript FROM interviews WHERE month = 7 AND day = 28;

SELECT name, transcript FROM interviews WHERE id = 161 OR id = 162 OR id = 163;

SELECT license_plate FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 25 AND activity IS "exit";

SELECT * FROM bakery_security_logs JOIN people ON people.license_plate = bakery_security_logs.license_plate WHERE month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 25 AND activity IS "exit";

SELECT person_id FROM bank_accounts JOIN atm_transactions ON bank_accounts.account_number = 