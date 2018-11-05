from gmail import GMail, Message

gmail = GMail("anonymus.hchi@gmail.com","hachi123456")

template = "Hi boss, today I will absent from work, because of {{sick}}. The doctor said {{advice}} your employee"
sickness_list = ["headache","stomache","heartache","toothache"]
# import random ==> random.choice()
from random import choice
advice = "take a rest"
content = template.replace("{{sick}}",choice(sickness_list)).replace("{{advice}}",advice)
new_content = '''<p><em>Hi there,</em></p>
<p>Today I will be absent&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-tongue-out.gif" alt="tongue-out" /></p>
<p>I hate to work&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-sealed.gif" alt="sealed" /></p>
<p>Just saying!</p>
<p>See you 2morrow</p>
<p>&nbsp;</p> '''

# message = Message("Xin nghi lam", to="levuhachi.in@gmail.com", text="Om qua sep oi, em bi so mui. Em xin nghi")
message = Message("Xin nghi lam", to="levuhachi.in@gmail.com", html= new_content)

gmail.send(message)