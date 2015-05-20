Writing scenarios
=================

Let's start with testing simple story -- user wants to log in:

  1. User come to login page
  2. They fill in the username and password and submit the form

Actions
-------

The most atomic part of stories are actions. In this case, each line is one
action:

  1. :py:class:`actions.Visit` -- go to page specified by URL
  2. :py:class:`actions.FillForm` -- fill in form and submit it

We can use predefined actions (see :doc:`Reference </reference/actions>`) and
initialize them with custom parameters:

.. code-block:: python

  from ariadne import actions

  visit_login = actions.Visit(url='/login')

  credentials = {
    'username': 'admin',
    'password': 'secret',
  }
  fill_credentials = actions.FillForm(data=credentials, submit='#btn-submit')


Stories
-------

Once we have ``actions`` defined, we can groups them into stories and specify
in which order these actions should be executed:

.. code-block:: python

  from ariadne import stories

  login_process = stories.Simple([
    visit_login,
    fill_credentials
  ])

:py:class:`stories.Simple` is just wrapper around set of actions, which
executes them serially one after another.

Scenarios
---------

The last step is to define scenarios. It usually consists of several stories,
but sometimes is scenario as simple as story itself. We can use simple shortcut
in such case:

.. code-block:: python

  user_login = login_process.as_scenario()

The main difference between scenario and stories is context. Each scenario
is executed with isolated context, while stories pass context from one to
another. In unittest scenario would be single test case.

Now we are ready to run our scenario in browser.
