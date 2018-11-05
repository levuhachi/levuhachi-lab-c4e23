from gmail import GMail, Message

gmail = GMail("anonymus.hchi@gmail.com","hachi123456")

template = "Hi boss, today I will absent from work, because of {{sick}}. The doctor said {{advice}} your employee"
sickness = "headache"
advice = "take a rest"
content = template.replace("{{sick}}",sickness).replace("{{advice}}",advice)

# message = Message("Xin nghi lam", to="levuhachi.in@gmail.com", text="Om qua sep oi, em bi so mui. Em xin nghi")
message = Message("Xin nghi lam", to="levuhachi.in@gmail.com", text=content)

gmail.send(message)

