# Created by Trofim Martynchuk at 10/3/2021
Feature: Check "Gaming" button


  Scenario: Check "Gaming" button on the main page
    Given Open YouTube page
    When Click "Gaming" button on left side
    Then Verify "Gaming" button worked