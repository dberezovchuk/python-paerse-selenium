Parser example using python and selenium.

You must install selenium:

>>> pip install selenium


You must install WebDriver. This parser uses ChromeDriver.
Cromedriver should be in the project folder or you must specify the path to it in the code (driver = webdriver.Chrome(../your folder)) 

If you use Windows:
1. You must open environment variables window in your machine. To do this, click on Start menu. Then right click on Computer and select Properties option.
2. Click on Advanced System Settings option.
3. Open the System Properties window. Now from the Advanced Tab, click on Environment Variables button.
4. Check that there is a variable named Path under System variables section.
5. Select the Path variable and click on Edit button. Now move to the end of the Variable value field, then add a semi colon (;) and then ChromeDriver’s folder location (for example – C:\Drivers\)
6. Click OK buttons to close all the windows.
