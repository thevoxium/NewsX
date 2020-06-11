from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
from cfonts import render, say
import click



output = render('NewsX', colors=['white', 'yellow'], align='center')
print(output)

opts=Options()
opts.set_headless()
assert opts.headless
browser=Firefox(options=opts)


def print_edt():

    browser.get("https://theprint.in/")
    click.echo(click.style("Wait For a Little Time, It May Take a Minute\n", fg="bright_red", bold=True, blink=True))
    click.echo(click.style("✓ SITE OPENED\n", fg="bright_cyan", bold=True))

    time.sleep(3)
    print("")
    editorial_but=browser.find_elements_by_class_name('sf-with-ul')

    editorial_but[4].click()
    time.sleep(4)

    editorial_list=browser.find_elements_by_class_name("item-details")
    click.echo(click.style("✓ EDTITORIALS FOUND\n", fg="bright_cyan", bold=True))
    for i in range(len(editorial_list)):
        click.echo(click.style("--------------------------------------------------", fg="bright_green"))
        print(editorial_list[i].text)

        if i==5:
            break


    click.echo(click.style("Enter the Editorial number you want to read: ", fg="bright_blue", bold=True))
    ednum=int(input())
    readmore_but=browser.find_elements_by_class_name("td-read-more")

    readmore_but[ednum-1].click()
    print("\n")
    click.echo(click.style("✓ EDITORIAL OPENED", fg="bright_yellow", blink=True, bold=True))
    time.sleep(4)

    content=browser.find_elements_by_class_name("td-post-content")

    f= open("editorial_print_news.txt","w+")
    f.write(content[0].text)
    f.close()
    browser.close()



print_edt()
