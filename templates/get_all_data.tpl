<html>
<body>
[ <a href="/goods">Goods</a> | <a href="/tasks">Tasks</a> | <a href="/add_goods">Add Goods</a> | <a href="/add_tasks">Add Tasks</a> | 
<a href="/my_goods">My Goods</a> | <a href="/my_tasks">My Tasks</a> ] 
<form action="/{{title}}/" method='GET'>
  <input type='text' name='q' size='15' maxlength='60'/>&nbsp;
  <input type='submit' VALUE="Search">
</form>
%if title == 'goods' or title == 'tasks': 
  <form method="POST" action="/add_my_{{title}}">
%end
<h1>{{title.capitalize()}}</h1>
<table border="1">
%for h in headers:
  <th>{{h.capitalize().replace('_', ' ')}}</th>
%end
<th>Y/N</th>
%for row in rows:
  <tr>
  %for h in headers:
    <td>{{row[h]}}</td>
  %end
  <td><input name="{{row['id']}}" type="text" value="0" size='3' maxlength='3'></td>
%end
</tr> 
</table>
<br>
%if title == 'goods' or title == 'tasks': 
  <input name='submit' type=submit value="Add to my {{title}}">
%end 
</form>
</body>
</html>
