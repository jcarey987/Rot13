# Rot13
This is the first project assignment for the [Web Development](https://in.udacity.com/course/web-development--cs253) course with Udacity.
An explanation of what Rot13 is, can be found [here](https://www.youtube.com/watch?v=uMGNwoFHfB4).
I based my solution on this date validation app I built alongside Steve Huffman and applied the same princibles to my solution. You can review the code for the date validation app [here](https://gist.github.com/jcarey987/c1ae85a46329b325f524a7d91f18b9d0#file-rot13-L49-L141). 
At first my Rot 13 solution did not work as intended. That is because under the [Rot13 class, in the post function](https://gist.github.com/jcarey987/c1ae85a46329b325f524a7d91f18b9d0#file-rot13-L1-L48), my string varible needed to read as `string = self.request.get('text')` in lieu of `string = self.request.get('user_input')` and my output varible needed
to be written as `output = rot(str(string))` in lieu of `output = rot(string)`.
The solution that Steve came up with can be viewed [here](https://gist.github.com/jcarey987/c1ae85a46329b325f524a7d91f18b9d0#file-rot13-L142-L241), and [this is a video where he discusses the solution.](https://www.youtube.com/watch?v=NYzMnbSjOWA&t=4s)
