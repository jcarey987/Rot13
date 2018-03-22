# Rot13
This is the first project assignment for the [Web Development](https://in.udacity.com/course/web-development--cs253) course with Udacity.
An explanation of what Rot13 is, can be found [here](https://www.youtube.com/watch?v=uMGNwoFHfB4).
I based my solution on this date validation app I built alongside Steve and applied the same princibles to my solution. You can review
the code [here](https://gist.github.com/jcarey987/c1ae85a46329b325f524a7d91f18b9d0#file-rot13-L49-L141). 
At first my solution did not work as intended, that is because my string varible in this [gist](https://gist.github.com/jcarey987/c1ae85a46329b325f524a7d91f18b9d0#file-rot13-L1-L48)
needed to read as `string = self.request.get('text')` in lieu of `string = self.request.get('user_input')` and my output varible needed
to be written as `output = rot(str(string))` in lieu of `output = rot(string)`.
