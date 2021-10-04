# Created by Trofim Martynchuk at 10/3/2021
Feature: Check "Movies & Shows" button


  Scenario: Check "Movies & Shows" button on the main page
    Given Open YouTube page
    When Click "Movies & Shows" button on left side
    Then Verify "Movies & Shows" button worked