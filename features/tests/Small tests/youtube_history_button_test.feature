# Created by Trofim Martynchuk at 10/2/2021
Feature: Check "History" button


  Scenario: Check "History" button on the main page
    Given Open YouTube page
    When Click "History" button
    Then Verify "History" button working