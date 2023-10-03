from robocorp.tasks import task
from robocorp import browser

@task
def minimal_task():
    """Insert the sales data for the week and export it as a PDF"""
    browser.configure(
        slowmo=1000,
    )
    open_the_intranet_website() #function responsible to access the intranet

def open_the_intranet_website():
    """Navigates to the given URL"""
    browser.goto("https://robotsparebinindustries.com/")