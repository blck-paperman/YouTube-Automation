# Created by Trofim Martynchuk at 10/2/2021
Feature: Check "Sign in" button, side menu


  Scenario: Check "Sign in" button on the main page side menu
    Given Open YouTube page
    When Click "Sign in" button on left side
    Then Verify "Sign in" button worked