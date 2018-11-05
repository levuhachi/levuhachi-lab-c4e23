from gmail import GMail, Message
from datetime import datetime

gmail = GMail("anonymus.hchi@gmail.com","hachi123456")

sickness_list = ["headache","stomache","heartache","toothache"]

from random import choice

advice = ["nghỉ ngơi","đi nghỉ dưỡng","tránh xa loài người"]

template = '''<p>Ch&agrave;o sếp, <img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cool.gif" alt="cool" />&nbsp;</p>
<p>Em l&agrave; <em><strong>H&agrave; Chi</strong></em></p>
<p>H&ocirc;m nay em xin ph&eacute;p nghỉ v&igrave; em bị {{sick}}&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
<p>B&aacute;c sĩ bảo em n&ecirc;n {{advice}}&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-sealed.gif" alt="sealed" /></p>
<p><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-laughing.gif" alt="laughing" />&nbsp;Cảm ơn sếp rất nhiều!&nbsp;</p>
<p><em>Nh&acirc;n vi&ecirc;n gương mẫu&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cool.gif" alt="cool" /></em></p> '''

content = template.replace("{{sick}}",choice(sickness_list)).replace("{{advice}}",choice(advice))

message = Message("Đơn xin nghỉ làm", to="levuhachi.in@gmail.com", html = content)

while True:
    time = datetime.now().strftime("%I:%M %p")
    if  "07:00 AM" < time < "08:00 AM":
        gmail.send(message)