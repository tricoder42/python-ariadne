Structure of tests
==================

Going from the top to the bottom, tests are organized into **scenarios**. These
scenarios are very similar to the ones from BDD [1]. They describe *how user
interacts with an application*.

For example one scenario for eshop could be:
"User puts an item into shopping cart." This scenario would proably contain
other not directly related actions like signing up into website which brings
us to the **stories**.

**Stories** are group of related actions. In example above it would be:
sign up and put item into shopping cart. More complex test would consist of
sign up, putting item into cart, sign off and sign up again -- to check that
content of shopping cart is persistent across logins.

Last at the most atomic part are **actions**. These actions describe single
event like visiting a website, filling the form, etc.

Actions, stories and scenarios itself doesn't test anything. Think about
scenarios like of *Ariadne's threads* -- they describe all possible ways through
an application.

The next step is to define **checks** which will be run during execution
of actions. These checks can perform anything from functional tests to
performance tests. In case of web applications, possible checks are:

  - does website work? (Does it returns HTTP 200)
  - does it take too long to render?
  - are there any duplicate or unwanted SQL queries
  - are there all translations?
  - is HTML rendered correctly (compared to last run)


Documenting actions
-------------------

Docstring should contain verbose name and description what
action does. This docsring will be used later either for verbose output during
automatic run or as an instruction during a manual run:

.. code-block:: python

   class VisitLoginPage(actions.Action):
       """ Go to login page.

       Visit login page located at {self.url_full}.
       """

First line of docstring will be verbose name of an action, the rest of docstring
is description.
