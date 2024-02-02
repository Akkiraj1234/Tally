# Time Log - Project Tally

**time invested in it......** *started(26 jan) - end(idk when)*\
**time-** `27 hours`\
**by-** akki  ~  insta-[@akki_raj_._](https://www.instagram.com/akki_raj_._/)

## Introduction to Tally

Tally, crafted with Python, revolutionizes accounting simplicity. This versatile software comes in three editions: Family Tally, Business Tally, and Tally Terminal. Tally, your go-to accounting solution, simplifies financial management with ease. From seamless company creation to secure data handling, Tally ensures a streamlined experience. Enjoy password protection, encryption support, and smart cash management. Currently, the Terminal version is in development, catering specifically to business needs. Elevate your financial management with Tally.

## Info about the code

### Stages

There are certain stages in this code that determine the progress of the code and where it has been made till now.

`1st Stage:-`
*The first stage contains the initial screen of the Tally software. Here, we can create a company, open a company, and select a company. While creating a company, only valid data is accepted and stored for later recall. The stage includes password and encryption support, system info updating, and cash handling.*\
\
`2nd Stage:-`
*The second stage involves working on the gateway of Tally, encompassing voucher management, ledger handling, group management, balance sheet computation, profit and loss analysis, and trading account management. This stage also focuses on efficient mass data handling, cash creation, and in-depth data research.*

## Progress Summary

1. **Date:** Sun, 28 Jan 2024
   - **Added JSON file and stopped using `eval`:** *Problem: To improve  security and avoid potential security risks associated with using eval.*
   - **Shortened the code** *To improve efficiency, effectiveness, and speed.*
   - **Fixed password problem** *Fixed the login issue occurring while creating a company.*
2. **Date** Thr, 01 Jan 2024
   - **addedd validation input** *added validation check up so none useless data coude be addedd*
   - **path changed** *companies list path changed C:\users\public\tally to `C:\users\public\tally\company_name`(current path)*
3. **Date** Fri, 02 Jan 2024
   - **validation_input_library:** *created a whole library for taking valid input*
   - **structured the code:** *structured the company creataion function for taking valid input and better readablity also for effective and effective output solved all mager error coude arcued durning creaton companies
   - **structured the whole code for readablity and `stage 1 over`**

## Encountered Errors

- ### Sun, 29 Jan 2024

1. **Encryption Data Issue:** *doesn't encrypting any number nor showing it*
    - Fixed magic numbers (58 to 69 and 80 to 81)
    - Added 0-9 numbers in map
    - Removed extra empty objects using `k.pop(k.index(''))`

2. **Company Creation Flow Issue:**
   - Returned `True` in `create_company` instead of `None`
   - Used `if not res: break` in line 151

## Errors haven't been resolved yet

[x] nothing yet
