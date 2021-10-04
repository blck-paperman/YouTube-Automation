# Created by Trofim Martynchuk at 10/3/2021
Feature: Check "Fashion & Beauty" button


  Scenario: Check "Fashion & Beauty" button on the main page
    Given Open YouTube page
    When Click "Fashion & Beauty" button on left side
    Then Verify "Fashion & Beauty" button worked