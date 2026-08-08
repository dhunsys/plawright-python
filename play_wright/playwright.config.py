# playwright.config.py
import pytest


def pytest_configure(config):
    config.option.reporter = [["html", {"outputFolder": "playwright-report"}]]
