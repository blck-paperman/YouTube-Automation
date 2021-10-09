# Created by Trofim Martynchuk at 10/8/2021
Feature: Check "360° Video" button


  Scenario: Check "360° Video" button on the main page
    Given Open YouTube page
    When Click "360° Video" button on left side
    Then Verify "360° Video" button worked