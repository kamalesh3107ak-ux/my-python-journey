"""from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")
    print("Page Title:", page.title())
    page.screenshot(path="example.png")
    browser.close()"""

"""from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.fill("#username", "student")
    page.fill("#password", "Password123")
    page.click("#submit")

    page.wait_for_timeout(5000)  # 5 seconds wait
    print("Login Completed!")

    # Remove browser.close() temporarily
    input("Press Enter to close browser...")

    browser.close()"""


"""from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open your YouTube Channel
    page.goto("https://www.youtube.com/@kamalesh333")

    input("Press Enter to close browser...")
    browser.close()"""

"""from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.google.com")

    print("Browser opened!")

    input("Press Enter to close...")
    browser.close()"""


"""from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request = p.request.new_context()

    response = request.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()

    print("Status:", response.status)
    print("Title:", data["title"])"""

"""from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request = p.request.new_context()

    response = request.get("https://example.com/file.pdf")

    with open("file.pdf", "wb") as f:
        f.write(response.body())

    print("File downloaded!")"""

"""from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)
    page = browser.new_page()

    page.goto("https://www.tamilprinthd.art/")

    # Example: Click first movie link
    first_movie = page.locator("a").first
    first_movie.click()

    print("Movie page opened.")
    input("Press Enter to exit...")"""

"""from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=80)
    page = browser.new_page()

    page.goto("https://www.tamilprinthd.art/")
    page.click("text=Tamil")   # Tamil movies section
    page.click("text=2025")    # Year filter
    page.click("text=All In One Folder")
    page.click("text=Kumki 2 (2025)")
    page.click("text=Kumki 2 (2025) PreDVD")
    page.click("text=Kumki 2 (2025) PreDVD Tamil Print")
    page.click("text=TamilPrint - Kumki 2 (2025) Tamil PreDVD Print 720pHD.mkv")

    print("IMDb Tamil 2025 movies section opened!")
    input("Press Enter to exit...") """



"""from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=80)
    page = browser.new_page()

    page.goto("https://demo.testfire.net/login.jsp")

    page.fill("#uid", "admin")
    page.fill("#passw", "admin")
    page.click("input[value='Login']")

    page.wait_for_selector("text=Hello Admin")
    print("Login done!")

    input("Press Enter to exit...")"""




from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=80)
    page = browser.new_page()

    page.goto("https://shop.polymer-project.org/")
    page.click("text=Outerwear")
    page.click("text=Men's Tech Shell Full-Zip")
    page.click("text=ADD TO CART")
    page.click("text=VIEW CART")


    input("Press Enter to exit...")


