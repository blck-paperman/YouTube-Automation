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