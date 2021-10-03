# Created by Trofim Martynchuk at 10/2/2021
Feature: Check "Library" button


  Scenario: Check "Library" button on the main page
    Given Open YouTube page
    When Click "Library" button
    Then Verify "Library" button working
