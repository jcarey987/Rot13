import webapp2
import string
import cgi

def rot(word):
    rot13 = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
                     "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    return string.translate(word, rot13)

def escape_html(s):
        return cgi.escape(s, quote=True)

page="""
<!DOCTYPE html>
<html>
	<head>
		<title>Lesson 2 - ROT13</title>
	</head>
	<body>
		<h2>Enter some text to ROT13:</h2>
		<form method="post">
			<textarea name="text" value="user_input" style="height: 100px;width: 400px;">%(user_input)s</textarea>
			<br>
			<input type="submit">
		</form>
	</body>
</html>
"""

class Rot13(webapp2.RequestHandler):
	def write_page(self, user_input=""):
		self.response.out.write(page % {"user_input": escape_html(user_input)})

	def get(self):
		self.write_page()

	def post(self):
		string = self.request.get("text")
		output = rot(str(string))

		self.write_page(output)

def rot(word):
    rot13 = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
                     "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    return string.translate(word, rot13)

def escape_html(s):
        return cgi.escape(s, quote=True)

app = webapp2.WSGIApplication([('/unit2/rot13', Rot13)], debug=True)
