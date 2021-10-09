# Created by Trofim Martynchuk at 10/8/2021
Feature: Check "Browse channels" button


  Scenario: Check "Browse channels" button on the main page
    Given Open YouTube page
    When Click "Browse channels" button on left side
    Then Verify "Browse channels" button worked