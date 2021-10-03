# Created by Trofim Martynchuk at 10/2/2021
Feature: Test "Subscriptions" button


  Scenario: Check "Subscriptions" button on the main page
    Given Open YouTube page
    When Click "Subscriptions" button
    Then Verify "Subscriptions" button working