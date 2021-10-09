# Created by Trofim Martynchuk at 10/8/2021
Feature: Check "YouTube Premium" button


  Scenario: Check "YouTube Premium" button on the main page
    Given Open YouTube page
    When Click "YouTube Premium" button on left side
    Then Verify "YouTube Premium" button worked