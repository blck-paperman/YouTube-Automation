# Created by Trofim Martynchuk at 10/3/2021
Feature: Check "Music" button


  Scenario: Check "Music" button on the main page
    Given Open YouTube page
    When Click "Music" button on left side
    Then Verify "Music" button worked