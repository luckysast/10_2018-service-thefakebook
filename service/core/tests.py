import re
from hashlib import sha1, md5

from django.test import TestCase


def sha1_md5(d):
    s = str(d)
    return sha1(s.encode("utf-8")).hexdigest(), md5(s.encode("utf-8")).hexdigest()


class StaticFilesCheck(TestCase):
    def test_check_static_files(self):
        urls = ["/static/noimage.jpg", "/static/record.css", "/static/style.css"]
        for url in urls:
            response = self.client.get(url)
            self.assertNotEqual(response.status_code, 404)


class VisitPagesWithoutAuthTestClass(TestCase):
    def test_visit_wa_pages(self):
        title = "<title>Thefakebook | Welcome to Thefakebook!</title>"
        urls = ["/index", "/schools_supported", "/contact_us", "/terms_of_use", "/register"]
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertInHTML(title, response.content.decode("utf-8"))

    def test_visit_pages_with_no_access(self):
        urls = ["/profile", "/profile/edit", "/profile/pic_edit", "/search",
                "/friends", "/friends/requests", "/messages"]
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)


class VisitPagesAfterAuthTestClass(TestCase):
    def setUp(self):
        data = {"name": "user1", "pass": "pass", "terms": 1, "status": 1, "email": "user1@example.com"}
        response = self.client.post("/register", data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/index")

    def test_visit_aa_pages(self):
        title = "<title>Thefakebook | Welcome to Thefakebook!</title>"
        urls = ["/index", "/profile", "/profile/edit", "/profile/pic_edit", "/search",
                "/friends", "/friends/requests", "/messages"]
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertInHTML(title, response.content.decode("utf-8"))


class SigninSignoutActionsTestClass(TestCase):
    def setUp(self):
        data = {"name": "user2", "pass": "pass", "terms": 1, "status": 1, "email": "user2@example.com"}
        response = self.client.post("/register", data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/index")

    def test_signin_signout(self):
        data = {"email": "user1@example.com", "pass": "pass"}
        response = self.client.post("/login", data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/index")
        response = self.client.get("/logout")
        self.assertEqual(response["Location"], "/index")


class AvatarUploadingTestClass(TestCase):
    def setUp(self):
        data = {"name": "user3", "pass": "pass", "terms": 1, "status": 1, "email": "user3@example.com"}
        response = self.client.post("/register", data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/index")

    def test_upload_an_image(self):
        test_file = 'core/static/image_test.png'

        with open(test_file, 'rb') as data:
            response = self.client.post("/profile/pic_edit", {'picture': data})
            self.assertEqual(response.status_code, 302)

        request = self.client.get("/profile")
        image_url = re.findall(r'<img width="150pt" src="(.+?)">', request.content.decode("utf-8"))
        self.assertIsNotNone(image_url)
        request = self.client.get(image_url[0])
        self.assertEqual(request.status_code, 200)


class CheckFriendshipFunctionalityTestClass(TestCase):
    def send_friendship_request(self):
        self.client.get(self.add_fr_page.format(id=self.user4_id))
        response = self.client.get(self.profile_page.format(id=self.user4_id))
        html_text = response.content.decode("utf-8")
        self.assertInHTML("You're sent friendship request", html_text)

    def accept_friendship_request(self):
        self.client.get("/logout")
        self.client.post("/login", data={"email": "user4@example.com", "pass": "pass"})

        self.client.get(self.add_fr_page.format(id=self.user5_id))
        response = self.client.get(self.profile_page.format(id=self.user5_id))

        html_text = response.content.decode("utf-8")
        self.assertInHTML("It's your friend", html_text)

    def remove_from_friend(self):
        self.client.get(self.remov_fr_page.format(id=self.user5_id))
        response = self.client.get(self.profile_page.format(id=self.user5_id))

        html_text = response.content.decode("utf-8")
        self.assertInHTML("Just another user in web", html_text)

    def test_friendship_functionality(self):
        self.profile_page = "/profile/{id}"
        self.add_fr_page = "/profile/{id}/add_to_friend"
        self.remov_fr_page = "/profile/{id}/remove_from_friend"

        data_mapping = [
            {"name": "user4", "pass": "pass", "terms": 1, "status": 1, "email": "user4@example.com"},
            {"name": "user5", "pass": "pass", "terms": 1, "status": 1, "email": "user5@example.com"}
        ]

        for data in data_mapping:
            response = self.client.post("/register", data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response["Location"], "/index")

        response = self.client.get("/search")

        html_text = response.content.decode("utf-8")
        id_set = set(int(uid) for uid in re.findall(r'href="/profile/(\d+)"', html_text))

        self.user5_id = max(id_set)
        self.user4_id = self.user5_id - 1

        self.send_friendship_request()
        self.accept_friendship_request()
        self.remove_from_friend()


class MessagesFunctionalityTestClass(TestCase):
    def send_message(self, uid, email):
        self.client.get("/logout")
        self.client.post("/login", data={"email": email, "pass": "pass"})
        s, m = sha1_md5(uid)
        data = {"subject": s[:30], "text": m[:30]}
        self.sended_messages.append([s[:30], m[:30]])
        self.client.post(self.message_send.format(id=self.user9_id), data=data)

    def get_messages(self):
        self.client.get("/logout")
        self.client.post("/login", data={"email": "user9@example.com", "pass": "pass"})

        response = self.client.get(self.message_page)
        html_text = response.content.decode("utf-8")

        messages_s = re.findall(r'<br> <b>"(\w{30})"</b>', html_text)
        messages_m = re.findall(r'<br> (\w{30})', html_text)

        for s, m in self.sended_messages:
            self.assertIn(s, messages_s)
            self.assertIn(m, messages_m)

    def check_count_limit(self):
        response = self.client.get(self.message_page+"?count=1")
        html_text = response.content.decode("utf-8")
        count_mess = int(re.findall(r'Messages from (\d) last people', html_text)[0])
        self.assertEqual(count_mess, 1)

    def test_message_functionality(self):
        self.message_send = "/messages/{id}"
        self.message_page = "/messages"

        self.sended_messages = list()

        data_mapping = [
            {"name": "user6", "pass": "pass", "terms": 1, "status": 1, "email": "user6@example.com"},
            {"name": "user7", "pass": "pass", "terms": 1, "status": 1, "email": "user7@example.com"},
            {"name": "user8", "pass": "pass", "terms": 1, "status": 1, "email": "user8@example.com"},
            {"name": "user9", "pass": "pass", "terms": 1, "status": 1, "email": "user9@example.com"},
        ]

        for data in data_mapping:
            response = self.client.post("/register", data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response["Location"], "/index")

        response = self.client.get("/search")

        html_text = response.content.decode("utf-8")
        id_set = set(int(uid) for uid in re.findall(r'href="/profile/(\d+)"', html_text))

        self.user9_id = max(id_set)

        for i, e in enumerate(range(self.user9_id-1, self.user9_id-4, -1)):
            self.send_message(8-e, data_mapping[i]["email"])

        self.get_messages()
        self.check_count_limit()
