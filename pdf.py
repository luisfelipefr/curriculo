import asyncio
from pyppeteer import launch

async def main():
  pdfName = 'curriculo.pdf'
  browser = await launch(
    heandless=True,
    executablePath='/usr/bin/chromium-browser',
    args=[
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      '--disable-gpu'
    ],
    handleSIGINT=False,  
    handleSIGTERM=False,
    handleSIGHUP=False,
  )
  page = await browser.newPage()
  await page.goto('https://luisfelipefr.github.io/curriculo/', waitUntil='networkidle0')
  await page.pdf({'path': pdfName,'format': 'A4'})
  await browser.close()
  print(f"PDF gerado em {pdfName}")

asyncio.run(main())