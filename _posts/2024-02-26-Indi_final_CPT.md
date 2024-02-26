---
toc: True
comments: True
layout: post
title: Tri 2 Final Individual
description: Tri 2 completion of stuff
courses: {'compsci': {'week': 23}}
type: hacks
---

# Project Overview:
The value of money is not being seen in today's society and people should be more aware on what to invest in, instead of investing into products that don't last a lifetime. To build wealth needs investment and for that our team have built some money simulating software that imitate the stock market and crypto market. Using my knowledge from the spotchecks and the information learnt in class, I needed to learn how the backend and frontend are connected and how they impact each other. For this, I have decided to implement something that uses an input and databases in order to store information. 

# My feature:

My feature is creating a fake crypto/stock called AtlasCoin in which there is a crypto cap limit of 1 million coins and each user is limited to 100 coins to buy in order to give a fair chance to everybody. With this, people can invest "fake money" to see how a real crypto market is imitated if they don't want to invest real money just yet. Because this is a simulation, we are assuming a bunch of people are selling and buying crypto so the price changes dramatically for every transaction. 


# Component A:

## Instructions of input for one of the following:

<img src = "{{site.baseurl}}/images/image.png" width = "800" height = "300">

- I have an input in which people can buy a certain amount of crypto coins. 

## Use of list or any other data type to represent a collection of data:
<img src = "{{site.baseurl}}/images/image-1.png" width = "500" height = "500">

- For every time someone buys coins, every transaction is stored in an sqlite database which contains the information. 

## At least one procedure that contributes to the program’s intended purpose, where you have defined:
<img src = "{{site.baseurl}}/images/image-2.png" width = "500" height = "500">

- In this procedure I used a post method in whihc the information related to the crypto price. I used js fetch in order to use these methods and post the information in the crypto price tab. 

## An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure:
<img src = "{{site.baseurl}}/images/image-3.png" width = "500" height = "500">

- Using the update data function inside of the fetchData function in order to retreive information for user transactions. It is currently not working, but I am still working on it to retreive data, but this is something I implemented from this requirement. 

## Calls to your student-developed procedure:
<img src = "{{site.baseurl}}/images/image-4.png" width = "500" height = "500">

- Here when the button gets clicked for transactions, the price changes and I made sure the function is being processed everytime the button is clicked. 

## Instructions for output (tactile, audible, visual, or textual) based on input and program functionality
<img src = "{{site.baseurl}}/images/image-5.png" width = "500" height = "500">

- Here the output is based on the transaction value and for each transaction the output changes which is the crypto price per coin. 


# Component B:
- All the requirements in the pdf are met except the 1 minute requirement. I believe the cause of this was because I was a bit too slow when switching between tabs (showing the database and prices). I will try changing this so it meets the 1 minute requirement. 