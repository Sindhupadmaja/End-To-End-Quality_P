from playwright.sync_api import Page, expect

def test_transaction_ui_loads(page: Page):
    page.goto("http://127.0.0.1:8501")
    expect(page.get_by_text("Transaction Release Quality Demo")).to_be_visible()

def test_transaction_form_is_present(page: Page):
    page.goto("http://127.0.0.1:8501")
    expect(page.get_by_text("Create transaction")).to_be_visible()
    expect(page.get_by_role("button", name="Submit transaction")).to_be_visible()
