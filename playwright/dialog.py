import time

from playwright.sync_api import Page, Playwright, expect


def test_verify_alert(page: Page):
    page.goto("https://testingsrc.blogspot.com/")
    # register event listener for single alert
    page.once("dialog", handle_dialog)  # persistent listener
    page.get_by_role("button", name="Show Alert").click()
    page.wait_for_timeout(3000)
    page.close()


def test_verify_prompt_alert(page: Page):
    page.goto("https://testingsrc.blogspot.com/")
    # register event listener for one or more alert
    page.once("dialog", handle_prompt_dialog)  # persistent listener
    #page.on("dialog", handle_dialog)  # persistent listener
    page.get_by_role("button", name="Prompt Alert").click()
    page.wait_for_timeout(3000)
    page.close()


#handle alert using lambda to and 2 alerts prompt->alert
def test_verify_lambda_prompt_alert(page: Page):
    page.goto("https://testingsrc.blogspot.com/")
    # register event listener for one or more alert
    page.once("dialog", lambda dialog: (
        dialog.accept("Playwright User")
    ))
    # Handle the alert that appears after prompt
    page.once("dialog", lambda dialog: (
        dialog.accept()
    ))
    #page.on("dialog", handle_dialog)  # persistent listener
    page.get_by_role("button", name="Multiple Alert").click()
    time.sleep(5)
    page.close()


# function to handle dialog
def handle_dialog(dialog):
    assert dialog.type == "alert"
    assert dialog.message == "Form Submitted!"
    dialog.accept()


# function to handle dialog
def handle_prompt_dialog(dialog):
    assert dialog.type == "prompt"
    assert dialog.message == "Please enter your name:"
    dialog.accept("Shahabuddin")
