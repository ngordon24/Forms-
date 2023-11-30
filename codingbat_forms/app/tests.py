from django.test import TestCase

# Create your tests here.

from django.test import SimpleTestCase


class TestWarmup(SimpleTestCase):
    def test_Chocolate_2(self):
        response = self.client.get(
            "/warmup-2/front-times/?repeatedtext=Chocolate&timesrepeated=2"
        )
        self.assertContains(response, "ChoCho")

    def test_Chocolate_3(self):
        response = self.client.get(
            "/warmup-2/front-times/?repeatedtext=Chocolate&timesrepeated=3"
        )
        self.assertContains(response, "ChoChoCho")

    def test_ABC_3(self):
        response = self.client.get(
            "/warmup-2/front-times/?repeatedtext=AbcAbcAbc&timesrepeated=3"
        )
        self.assertContains(response, "AbcAbcAbc")


class TestLogic(SimpleTestCase):
    def test_123(self):
        response = self.client.get(
            "/logic-2/no-teen-sum/?numberone=1&numbertwo=2&numberthree=3"
        )
        self.assertContains(response, "6")

    def test_2131(self):
        response = self.client.get(
            "/logic-2/no-teen-sum/?numberone=2&numbertwo=13&numberthree=1"
        )
        self.assertContains(response, "3")

    def test_2114(self):
        response = self.client.get(
            "/logic-2/no-teen-sum/?numberone=2&numbertwo=1&numberthree=14"
        )
        self.assertContains(response, "3")


class TestString(SimpleTestCase):
    def test_Chocolate_2(self):
        response = self.client.get("/string-2/xyz-there/?text=abcxyz")
        self.assertContains(response, True)

    def test_Chocolate_3(self):
        response = self.client.get("/string-2/xyz-there/?text=abc.xyz")
        self.assertContains(response, False)

    def test_ABC_3(self):
        response = self.client.get("/string-2/xyz-there/?text=xyz.abc")
        self.assertContains(response, True)


class TestList(SimpleTestCase):
    def test_1(self):
        response = self.client.get(
            "/list-2/centered-average/?numbers=1%2C+2%2C+3%2C+4%2C+100"
        )
        self.assertContains(response, "3")

    def test_2(self):
        response = self.client.get(
            "/list-2/centered-average/?numbers=1%2C+1%2C+5%2C+5%2C+10%2C+8%2C+7"
        )
        self.assertContains(response, "5")

    def test_3(self):
        response = self.client.get(
            "/list-2/centered-average/?numbers=-10%2C+-4%2C+-2%2C+-4%2C+-2%2C+0"
        )
        self.assertContains(response, "-3")
