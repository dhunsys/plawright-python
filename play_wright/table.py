from playwright.sync_api import Page, Playwright, expect


def test_static_table_demo(page: Page):
    # Navigate to the page
    page.goto("https://testingsrc.blogspot.com/")

    # Scroll table into view
    page.locator("#dataTable").scroll_into_view_if_needed()

    # Locate the table body
    table = page.locator("#dataTable > tbody")
    # Assert table is visible
    expect(table).to_be_visible()
    # Get all rows
    rows = table.locator("tr").all()
    # Skip header row (index 0) and print each row's full cell texts
    for row in rows[1:]:
        cell_texts = row.locator("td").all_inner_texts()
        print(cell_texts)
        # show table row and col wise
        # Skip header row (index 0)
        for i in range(1, len(rows)):
            # Get all columns (td) in the current row
            columns = rows[i].locator("td").all()
            for j in range(len(columns)):
                # Print each cell's inner text
                print("text in row", i, "and", "col", j, "is", columns[j].inner_text())

        # Print all 2nd column data (index 1 because it's zero-based)
        print("Print all 2nd column data")
        for i in range(1, len(rows)):  # skip header row
            print(rows[i].locator("td").nth(1).inner_text())

        # Verify row count
        assert len(rows) == 3

        # Verify number of columns in 2nd row (index 1)
        all_tds = rows[1].locator("td").all()
        assert len(all_tds) == 2
