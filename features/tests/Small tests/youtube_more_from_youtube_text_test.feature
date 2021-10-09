# Created by Trofim Martynchuk at 10/8/2021
Feature: Check "MORE FROM YOUTUBE" text


  Scenario: Check if "MORE FROM YOUTUBE" text is present on side menu
    Given Open YouTube page
    Then Verify "MORE FROM YOUTUBE" text present