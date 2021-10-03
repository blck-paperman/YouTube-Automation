# Created by Trofim Martynchuk at 10/3/2021
Feature: Check "YouTube" button


  Scenario: Check "YouTube" button on the main page
    Given Open YouTube page
    When Click "YouTube" button
    Then Verify "YouTube" button working