

## "Shift Heroes" Challenge: Automating Shift Reservations

This repository contains my personal solution to the challenge posed by the YouTuber Harry Jmg. The challenge involved automating the process of shift scheduling and reservations using the [!Shift Heroes](https://shiftheroes.fr/videos) API. In this document, I will present my solution, explain how it works, and describe how it tackles the challenge.

## Introduction

"Shift Heroes" challenge provided me with the opportunity to tackle a real-world problem using my programming skills. The goal was to create a Python script capable of interacting with the Shift Heroes API to automate the reservation of available shifts.

## My Solution

The script I developed performs the following steps:

Retrieving the available planning IDs based on the specified planning type (daily, weekly).

Getting a dictionary of available shift IDs for each planning ID.

Identifying shifts that have not been reserved yet.

Automatically reserving these available shifts.

To achieve these tasks, I used the requests library to make API requests and interact with the Shift Heroes data.


## How the Script Works

I began by importing the requests library and necessary functions.

The script starts by fetching the available planning IDs based on the specified type (daily or weekly).

Using these planning IDs, the script retrieves the available shift IDs for each planning.

The script identifies shifts that haven't been reserved by comparing them with shifts that have been reserved.

Finally, the script makes reservations for the available shifts that haven't been reserved.

## Conclusion

Participating in Harry Jmg's "Shift Heroes" challenge was a rewarding experience that allowed me to apply my programming skills to solve a real problem. I hope my solution proves useful to others seeking to automate similar processes.