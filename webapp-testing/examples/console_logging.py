from playwright.sync_api import sync_playwright

# Example: Capturing console logs during browser automation
# Use this to detect JS errors, warnings, and API failures during UI flows

url = 'http://localhost:3000'  # Replace with your local dev URL

console_logs = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})

    # Set up console log capture BEFORE navigation
    def handle_console_message(msg):
        console_logs.append(f"[{msg.type}] {msg.text}")
        if msg.type in ('error', 'warning'):
            print(f"⚠️  Console {msg.type}: {msg.text}")

    # Capture failed network requests
    def handle_request_failed(request):
        console_logs.append(f"[network-error] {request.method} {request.url} — {request.failure}")
        print(f"❌ Request failed: {request.method} {request.url}")

    page.on("console", handle_console_message)
    page.on("requestfailed", handle_request_failed)

    # Navigate to page
    page.goto(url)
    page.wait_for_load_state('networkidle')

    # Take initial screenshot
    page.screenshot(path='/tmp/console_test_start.png', full_page=True)

    # Perform actions that trigger console output
    # Replace with your actual user flow
    # page.click('text=Book Appointment')
    # page.wait_for_timeout(1000)

    browser.close()

# Save console logs to file
log_output = '\n'.join(console_logs)
with open('/tmp/console.log', 'w') as f:
    f.write(log_output)

errors = [l for l in console_logs if '[error]' in l or '[network-error]' in l]
warnings = [l for l in console_logs if '[warning]' in l]

print(f"\nConsole summary:")
print(f"  Total messages: {len(console_logs)}")
print(f"  Errors:         {len(errors)}")
print(f"  Warnings:       {len(warnings)}")
print(f"  Log saved to:   /tmp/console.log")

# Dharma evidence standard: fail if unexpected errors present
if errors:
    print(f"\n❌ Errors detected — review /tmp/console.log before claiming verify gate passed")
else:
    print(f"\n✅ No console errors — clean run")
