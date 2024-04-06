-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Find id and description for the CS50 duck report.
SELECT id, description FROM crime_scene_reports WHERE month = 7 AND day = 28;

SELECT id, transcript FROM interviews WHERE month = 7 AND day = 28;

SELECT name, transcript FROM interviews WHERE id = 161 OR id = 162 OR id = 163;

SELECT activity, license_plate FROM bakery_security_logs WHERE month = 7 AND day = 28 AND 
