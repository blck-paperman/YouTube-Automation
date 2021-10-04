# Created by Trofim Martynchuk at 10/2/2021
Feature: Test YouTube Main/Home page


  Scenario: Whole "Main/Home" page test
      #  Main page test
    Given Open YouTube page
    Then Verify that YouTube page opened
      #  Check "YouTube" button on the main page
    Given Open YouTube page
    When Click "YouTube" button
    Then Verify "YouTube" button working
      #  Check "Home" button on the main page
    Given Open Explore YouTube page
    When Click "Home" button
    Then Verify "Home" button working
      # Check "Explore" button on the main page
    Given Open YouTube page
    When Click "Explore" button
    Then Verify "Explore" button working
      #  Check "Subscriptions" button on the main page
    Given Open YouTube page
    When Click "Subscriptions" button
    Then Verify "Subscriptions" button working
      #  Check "Library" button on the main page
    Given Open YouTube page
    When Click "Library" button
    Then Verify "Library" button working
      #  Check "History" button on the main page
    Given Open YouTube page
    When Click "History" button
    Then Verify "History" button working
      #  Check "Sign in" button on the main page side menu
    Given Open YouTube page
    When Click "Sign in" button on left side
    Then Verify "Sign in" button worked
      #  Check "Sign in" button on the main page, side menu
    Given Open YouTube page
    When Click "Sign in" button on left side
    Then Verify "Sign in" button worked
      #  Check "Music" button on the main page
    Given Open YouTube page
    When Click "Music" button on left side
    Then Verify "Music" button worked