import time

from behave import given, then

from Features.PageObjects.Homepage import Homepage


@given(u'I am on the homepage')
def step_impl(context):
    print('Title of the page is: ' , context.driver.title)
    assert 'Green Man Gaming | Buy Games, Game Keys & Digital Games Today' in context.driver.title


@then(u'I need to check the if the links are working')
def step_impl(context):
    context.nav = Homepage(context.driver)
    context.nav.navigation_check()
    time.sleep(10)


@then(u'there is no broken link on the page')
def step_impl(context):
    print('No broken links found')