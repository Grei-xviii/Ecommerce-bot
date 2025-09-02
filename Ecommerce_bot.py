import asyncio
import logging
from playwright.async_api import async_playwright
import random

# Configure logging
logging.basicConfig(
    filename="logs/warmup.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        try:
            # Open e-commerce site
            logging.info("Opening e-commerce site...")
            await page.goto("https://automationexercise.com")

            # Navigate to Signup/Login
            logging.info("Navigating to Signup/Login page...")
            await page.click("a[href='/login']")

            # Fill signup form with uniqaue username and email
            random_number = random.randint(1000, 9999)
            username = f"testuser_{random_number}"
            email = f"{username}@example.com"
            logging.info(f"Signing up with username={username}, email={email}...")
            await page.fill("input[data-qa='signup-name']", username)
            await page.fill("input[data-qa='signup-email']", email)
            await page.click("button[data-qa='signup-button']")

            # Fills in account details
            logging.info("Filling in account details...")
            await page.check("input[id='id_gender1']")
            await page.fill("input[id='password']", "TestPassword123")
            await page.select_option("select[id='days']", "10")
            await page.select_option("select[id='months']", "5")
            await page.select_option("select[id='years']", "1995")
            await page.fill("input[id='first_name']", "John")
            await page.fill("input[id='last_name']", "Doe")
            await page.fill("input[id='address1']", "123 Test Street")
            await page.fill("input[id='state']", "Lagos")
            await page.fill("input[id='city']", "Ikeja")
            await page.fill("input[id='zipcode']", "100001")
            await page.fill("input[id='mobile_number']", "+2348012345678")
            await page.click("button[data-qa='create-account']")

            logging.info("Account successfully created!")

            #  Searches for an item
            try:
                logging.info("Searching for an item...")
                await page.goto("https://automationexercise.com/products")

                # Wait for search input
                await page.wait_for_selector("input[id='search_product']", timeout=10000)
                await page.fill("input[id='search_product']", "shirt")
                await page.click("button[id='submit_search']")

                logging.info("Search completed successfully!")
            except Exception as e:
                logging.error(f"Failed during search: {e}")
                await browser.close()
                return

            # Closes browser after a short delay
            await asyncio.sleep(5)  # delays to see results
            await browser.close()

        except Exception as e:
            logging.error(f"Automation failed: {e}")
            await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
