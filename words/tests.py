from unittest import TestCase

from django.test import TestCase as DjangoTestCase
from django.urls import reverse

from words.concordance import Concordance

TEXT = ("Given an arbitrary text document written in English, "
        "write a web application that will generate a concordance, "
        "i.e. an alphabetical list of all word occurrences, labeled "
        "with word frequencies. Bonus: label each word with the "
        "sentence numbers in which each occurrence appeared.")

TEST_CONCORDANCE = ["a {2:1,1}", "all {1:1}", "alphabetical {1:1}",
                    "an {2:1,1}", "appeared {1:2}",
                    "application {1:1}", "arbitrary {1:1}",
                    "bonus {1:2}", "concordance {1:1}",
                    "document {1:1}", "each {2:2,2}", "english {1:1}",
                    "frequencies {1:1}", "generate {1:1}",
                    "given {1:1}", "i.e. {1:1}", "in {2:1,2}",
                    "label {1:2}", "labeled {1:1}", "list {1:1}",
                    "numbers {1:2}", "occurrence {1:2}",
                    "occurrences {1:1}", "of {1:1}", "sentence {1:2}",
                    "text {1:1}", "that {1:1}", "the {1:2}",
                    "web {1:1}", "which {1:2}", "will {1:1}",
                    "with {2:1,2}", "word {3:1,1,2}", "write {1:1}",
                    "written {1:1}"]


class ConcordanceTests(TestCase):

    """ Tests for concordance class methods."""

    def test_concordance(self):
        concordance = Concordance(TEXT).concordance()
        for index, row in enumerate(TEST_CONCORDANCE):
            self.assertEqual(row, str(concordance[index][1]))


class IncesViewTests(DjangoTestCase):

    """ Tests for main application view.
    """

    def test_no_value(self):
        response = self.client.post(reverse("words:index"), {"run": "Run"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Please provide some text.",
                      response.content.decode("utf-8"))

    def test_submit(self):
        response = self.client.post(reverse("words:index"),
                                    {"data": TEXT, "run": "Run"})
        self.assertEqual(response.status_code, 200)
        for index, row in enumerate(TEST_CONCORDANCE):
            self.assertIn(row, response.content.decode("utf-8"))
