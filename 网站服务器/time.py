from datetime import datetime
print('''\
<html>
<head>
<meta charset='UTF-8'>
</head>
<body>
<p>当前时间： {0}</p>
</body>
</html>'''.format(datetime.now()))