# Created by Trofim Martynchuk at 10/2/2021
Feature: Test YouTube Main page


  Scenario: Main page test
    Given Open YouTube page
    Then Verify that YouTube page opened


  Scenario: Check "YouTube" button on the main page
    Given Open YouTube page
    When Click "YouTube" button
    Then Verify "YouTube" button working


  Scenario: Check "Home" button on the main page
    Given Open Explore YouTube page
    When Click "Home" button
    Then Verify "Home" button working


  Scenario: Check "Explore" button on the main page
    Given Open YouTube page
    When Click "Explore" button
    Then Verify "Explore" button working


  Scenario: Check "Subscriptions" button on the main page
    Given Open YouTube page
    When Click "Subscriptions" button
    Then Verify "Subscriptions" button working


  Scenario: Check "Library" button on the main page
    Given Open YouTube page
    When Click "Library" button
    Then Verify "Library" button working


  Scenario: Check "History" button on the main page
    Given Open YouTube page
    When Click "History" button
    Then Verify "History" button working


  Scenario: Check "Sign in" button on the main page, side menu
    Given Open YouTube page
    When Click "Sign in" button on left side
    Then Verify "Sign in" button worked


  Scenario: Check "Music" button on the main page
    Given Open YouTube page
    When Click "Music" button on left side
    Then Verify "Music" button worked


  Scenario: Check "Sports" button on the main page
    Given Open YouTube page
    When Click "Sports" button on left side
    Then Verify "Sports" button worked


  Scenario: Check "Gaming" button on the main page
    Given Open YouTube page
    When Click "Gaming" button on left side
    Then Verify "Gaming" button worked


  Scenario: Check "Movies & Shows" button on the main page
    Given Open YouTube page
    When Click "Movies & Shows" button on left side
    Then Verify "Movies & Shows" button worked


  Scenario: Check "News" button on the main page
    Given Open YouTube page
    When Click "News" button on left side
    Then Verify "News" button worked